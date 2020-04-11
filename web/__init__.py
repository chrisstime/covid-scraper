import sqlite3
from sqlite3 import Error
from flask import Flask
from web.index import index
from web.nsw_covid_scraper import NswCovidScraper

app = Flask(__name__)
app.register_blueprint(index)

def create_connection(db_file):
        """create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

if __name__ == '__main__':
    conn = create_connection('covid_cases_nsw.db')
    cs = NswCovidScraper(conn)
    app.run()
