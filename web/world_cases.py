from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound
from .world_covid_scraper import WorldCovidScraper

WORLDWIDE_BLUEPRINT = Blueprint('worldwide', __name__,
                        template_folder='templates')

@WORLDWIDE_BLUEPRINT.route('/worldwide')
def worldwide():
    try:
        wcs = WorldCovidScraper()
        return render_template(
            'worldwide.html', title='COVID-19 Cases Worldwide',
            affected_countries=wcs.get_affected_countries()
            )
    except TemplateNotFound:
        abort(404)