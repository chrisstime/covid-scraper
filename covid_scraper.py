import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class CovidScraper:
    def __init__(self):
        worldometers_page = requests.get('https://www.worldometers.info/coronavirus/')
        self.worldometers_soup = BeautifulSoup(worldometers_page.content, 'html.parser')

        self.aus_gov_site = 'https://data.nsw.gov.au/data/api/3/action/datastore_search_sql?sql=SELECT'
        self.aus_gov_resource_id = '21304414-1ff1-4243-a5d2-f52778048b29'

    def get_affected_countries(self):
        country_tags = self.worldometers_soup.find_all(attrs={ "class": "mt_a"})
        countries = []
        for country in country_tags:
            countries.append(country.get_text())

        return countries

    def get_cases_by_postcode(self, postcode):
        sql_api_query = '''{} notification_date AS case_report_date,
            lhd_2010_name AS region, 
            lga_name19 AS council FROM "{}" WHERE postcode={}'''.format(
            self.aus_gov_site, self.aus_gov_resource_id, int(postcode)
            )
        results = requests.get(sql_api_query)
        
        return results.json()

cs = CovidScraper()
print('Type in a postcode:')
postcode = input()
print(cs.get_cases_by_postcode(postcode))