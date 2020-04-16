from flask import Blueprint, render_template, abort, url_for
from jinja2 import TemplateNotFound
from .nsw_covid_scraper import NswCovidScraper

AUSTRALIA_BLUEPRINT = Blueprint('australia', __name__,
                        template_folder='templates')

@AUSTRALIA_BLUEPRINT.route('/cases_in_australia')
def australia():
    try:
        acs = NswCovidScraper()
        return render_template(
            'australia.html', title='COVID-19 Cases in Australia',
            councils=acs.get_available_councils()
            )
    except TemplateNotFound:
        abort(404)