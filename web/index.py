from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .db import create_connection
from .nsw_covid_scraper import NswCovidScraper

INDEX_BLUEPRINT = Blueprint('index', __name__,
                        template_folder='templates')

@INDEX_BLUEPRINT.route('/')
def index():
    try:
        conn = create_connection('covid_cases_nsw.db')
        nsw_cs = NswCovidScraper(conn)
        return render_template('index.html', nsw_cs=nsw_cs)
    except TemplateNotFound:
        abort(404)
