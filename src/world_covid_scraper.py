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

        return countries
