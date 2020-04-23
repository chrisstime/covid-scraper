from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from .scrapers.nsw_covid_scraper import NswCovidScraper

AUSTRALIA_BLUEPRINT = Blueprint('australia', __name__,
                        template_folder='templates')
NCS = NswCovidScraper()

@AUSTRALIA_BLUEPRINT.route('/cases_in_australia', methods=['GET'])
def australia():
    try:
        results = NCS.get_cases_by_postcode('2126')

        return render_template(
            'australia.html', title='COVID-19 Cases in Australia',
            location='in Australia',
            councils=NCS.get_available_councils(),
            results=results,
            total_cases_nsw=NCS.get_total_cases()
            )
    except TemplateNotFound:
        abort(404)