from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound
from .world_covid_scraper import WorldCovidScraper
from .helper import calculate_percentage

INDEX_BLUEPRINT = Blueprint('index', __name__,
                        template_folder='templates')

@INDEX_BLUEPRINT.route('/', methods=['GET'])
def index():
    try:
        world_cs = WorldCovidScraper()
        return render_template(
            'index.html', title='COVID-19 Scraper',
            world_cases = world_cs.get_worldwide_cases(),
            percentage = calculate_percentage
            )
    except TemplateNotFound:
        abort(404)
