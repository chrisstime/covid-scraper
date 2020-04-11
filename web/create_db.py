import sqlite3
import pandas as pd
from pandas import DataFrame

# CREATE CONNECTION TO SQLITE DB. IT WILL CREATE IF NONE EXISTS.
conn = sqlite3.connect('covid_cases_nsw.db')
c = conn.cursor()

# CREATE TABLES
# RUN THE CODE BELOW WHEN CREATING THE TABLES FOR THE FIRST TIME. OTHERWISE COMMENT OUT.

c.execute('''CREATE TABLE cases_by_loc
            ([id] INTEGER PRIMARY KEY, [notification_date] datetime, [postcode] int,
            [local_health_district_code] text, [local_health_district] text, 
            [local_gov_area_code] int, [local_gov_area] text)''')

c.execute('''CREATE TABLE cases_by_age
            ([id] INTEGER PRIMARY KEY, [notification_date] datetime, [age_group] text)''')

c.execute('''CREATE TABLE cases_by_infection_source
            ([id] INTEGER PRIMARY KEY, [notification_date] datetime, [likely_source] text)''')

conn.commit()
# END CREATE TABLES

# Update repo_path with local repo location.
repo_path = '/home/$USER/Repos/covid_scraper'

# Import data from the data_dumps.
cases_by_loc_csv = pd.read_csv(
    '{}/data_dumps/covid-19-cases-by-notification-and-location.csv'.format(repo_path))
cases_by_loc_csv.to_sql('cases_by_loc', conn, if_exists='replace', index=False)

cases_by_age_csv = pd.read_csv(
    '{}/data_dumps/covid-19-cases-by-notification-date-and-age-range.csv'.format(repo_path))
cases_by_age_csv.to_sql('cases_by_age', conn, if_exists='replace', index=False)

cases_by_infection_source_csv = pd.read_csv(
    '{}/data_dumps/covid-19-cases-by-notification-date-and-likely-source-of-infection.csv'.format(repo_path))
cases_by_infection_source_csv.to_sql(
    'cases_by_infection_source', conn, if_exists='replace', index=False)
