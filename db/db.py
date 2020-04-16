import os
import sqlite3
from sqlite3 import Error
import pandas as pd
from pandas import DataFrame
import click
from flask import current_app, g
from flask.cli import with_appcontext

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def init_db():
    db = get_db()

    with current_app.open_resource(os.path.join(APP_ROOT, 'schema.sql')) as f:
        db.executescript(f.read().decode('utf8'))
    
    db.commit()
    populate_db()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            os.path.join(APP_ROOT, 'covid_cases_nsw.db'),
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def populate_db():
    # CREATE CONNECTION TO SQLITE DB. IT WILL CREATE IF NONE EXISTS.
    conn = get_db()

    # Update repo_path with local repo location.
    repo_path = '/home/christine/Repos/covid_scraper'

    # Import data from the data_dumps.
    cases_by_loc_csv = pd.read_csv(
        '{}/data_dumps/covid-19-cases-by-notification-and-location.csv'.format(repo_path))
    cases_by_loc_csv.to_sql('cases_by_loc', conn, if_exists='append', index=False)

    cases_by_age_csv = pd.read_csv(
        '{}/data_dumps/covid-19-cases-by-notification-date-and-age-range.csv'.format(repo_path))
    cases_by_age_csv.to_sql('cases_by_age', conn, if_exists='append', index=False)

    cases_by_infection_source_csv = pd.read_csv(
        '{}/data_dumps/covid-19-cases-by-notification-date-and-likely-source-of-infection.csv'.format(repo_path))
    cases_by_infection_source_csv.to_sql(
        'cases_by_infection_source', conn, if_exists='append', index=False)

    close_db()