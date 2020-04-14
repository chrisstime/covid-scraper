from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound
from .db import create_connection
from .nsw_covid_scraper import NswCovidScraper
from .world_covid_scraper import WorldCovidScraper
from .helper import calculate_percentage

INDEX_BLUEPRINT = Blueprint('index', __name__,
                        template_folder='templates')
ABOUT_BLUEPRINT = Blueprint('about', __name__,
                        template_folder='templates')

@INDEX_BLUEPRINT.route('/', methods=['GET'])
def index():
    try:
        conn = create_connection('covid_cases_nsw.db')
        nsw_cs = NswCovidScraper(conn)
        world_cs = WorldCovidScraper()
        return render_template(
            'index.html', 
            councils=nsw_cs.get_available_councils(),
            world_cases = world_cs.get_worldwide_cases(),
            percentage = calculate_percentage
            )
    except TemplateNotFound:
        abort(404)

@ABOUT_BLUEPRINT.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)
