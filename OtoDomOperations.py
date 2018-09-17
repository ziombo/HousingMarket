import requests
from bs4 import BeautifulSoup
from time import sleep

from DbHelper import DbHelper
from OtoDomScraper import get_offers_from_soup, scrape_next_page


class BaseController():
    @staticmethod
    def get_html_soup(url):
        r = requests.get(url)
        return BeautifulSoup(r.text, 'html.parser')


class OtodomOperations(BaseController):
    def __init__(self):
        self.base_url = 'https://www.otodom.pl/wynajem/mieszkanie/warszawa/'

    def get_all_otodom_offers(self):
        """
        Returns list of all offers from otodom for Warsaw.
        Each request is made with 2 seconds delay.

        :return: list of offers
        """
        url = self.base_url
        offers = list()

        while url:
            offers.extend(self.get_otodom_page_offers(url))
            url = self._get_next_page(url)
            sleep(2)

        return offers

    def get_otodom_offers(self, no_of_pages=1, delay=0):
        """
        Returns list of offers from otodom for Warsaw from number of pages

        :param no_of_pages: number of pages to crawl through
        :return: list of offers
        """

        url = self.base_url
        offers = list()
        counter = 0
        while url and counter < no_of_pages:
            offers.extend(self.get_otodom_page_offers(url))
            url = self._get_next_page(url)

            counter += 1
            sleep(delay)

        return offers

    def download_otodom_offers(self, no_of_pages=1, delay=0):
        offers = self.get_otodom_offers(no_of_pages, delay)

        with DbHelper() as db:
            db.save_offers(offers)

        return offers

    def get_otodom_page_offers(self, url):
        print("Requesting page:", url)
        page_soup = self.get_html_soup(url)
        return get_offers_from_soup(page_soup)

    def _get_next_page(self, url):
        page_soup = self.get_html_soup(url)
        return scrape_next_page(page_soup)
