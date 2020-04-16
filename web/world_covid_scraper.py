import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class WorldCovidScraper:
    def __init__(self):
        worldometers_page = requests.get('https://www.worldometers.info/coronavirus/')
        self.worldometers_soup = BeautifulSoup(worldometers_page.content, 'html.parser')

    def get_affected_countries(self):
        country_tags = self.worldometers_soup.find_all(attrs={ "class": "mt_a"})
        countries = []
        for country in country_tags:
            countries.append(country.get_text())
        set_countries = set(countries)
        
        return set_countries
    
    def get_worldwide_cases(self):
        main_counter = self.worldometers_soup.find_all(attrs={ "class": "maincounter-number"})
        cases_tally = {}
        cases_tally['cases'] = main_counter[0].get_text()
        cases_tally['deaths'] = main_counter[1].get_text()
        cases_tally['recovered'] = main_counter[2].get_text()

        return cases_tally
