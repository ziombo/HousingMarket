import requests
from bs4 import BeautifulSoup
from time import sleep

from DbHelper import DbHelper
from OtoDomScraper import get_offers_from_soup, scrape_next_page


class BaseController():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    def __init__(self):
        self.session = requests.Session()

    def get_html_soup(self, url):
        r = self.session.get(url, headers=self.headers)
        self.headers['referer'] = url

        return BeautifulSoup(r.text, 'html.parser')


class OtodomOperations(BaseController):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://www.otodom.pl/wynajem/mieszkanie/warszawa/'

    def get_all_otodom_offers(self, delay=0):
        """
        Returns list of all offers from otodom for Warsaw.
        Each request is made with 2 seconds delay.

        :param delay: seconds to wait between each request
        :return: list of offers
        """
        url = self.base_url
        offers = list()

        while url:
            new_offers, next_page = self.get_otodom_page_offers(url)
            offers.extend(new_offers)
            url = next_page

            sleep(delay)

        return offers

    def get_otodom_offers(self, no_of_pages=1, delay=0):
        """
        Returns list of offers from otodom for Warsaw from number of pages

        :param no_of_pages: number of pages to crawl through
        :param delay: seconds to wait between each request
        :return: list of offers
        """

        url = self.base_url
        offers = list()
        counter = 0

        while url and counter < no_of_pages:
            new_offers, next_page = self.get_otodom_page_offers(url)

            offers.extend(checked_offer for checked_offer in new_offers if
                          not any(checked_offer.Url == o.Url and checked_offer.Title ==
                                  o.Title for o in
                                  offers))

            url = next_page
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
        return get_offers_from_soup(page_soup), scrape_next_page(page_soup)
