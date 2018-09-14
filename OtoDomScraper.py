import requests
from urllib.parse import quote, quote_plus, urljoin, urlparse, urldefrag
from bs4 import BeautifulSoup
from IPython.display import display
from Models import Offer


class ScrapingHelper:
    @staticmethod
    def GetOffersFromHtml(html_soup):
        offers_html = html_soup.find_all('article', class_='offer-item')
        offers = list()
        for offer_html in offers_html:
            offer = ScrapingHelper.ScrapeOffer(offer_html)
            if not any(offer.Url == o.Url and offer.Title == o.Title for o in offers):
                offers.append(offer)

        return offers

    @staticmethod
    def ScrapeOffer(offer_html):
        offer_url = urldefrag(offer_html['data-url'])[0]

        offer_title = offer_html.find(class_='offer-item-title').get_text(strip=True)

        # Wywalić adres do innej tabeli? City/District/Street/Street_Number
        offer_region = offer_html.find('p', class_=['text-nowrap hidden-xs']).get_text(
            strip=True)
        # Getting rid of "Mieszkanie na wynajem: "
        offer_region = offer_region[offer_region.index(':') + 2:]

        offer_price = offer_html.find(class_='offer-item-price').get_text(strip=True)
        # Getting rid of currency
        offer_price = offer_price[:offer_price.index('zł')]

        offer_area = offer_html.find(class_='offer-item-area').get_text(strip=True)
        # Getting rid of square meters sign
        offer_area = offer_area[:offer_area.index('m')]

        offer_rooms = offer_html.find(class_='offer-item-rooms').get_text(strip=True)[0]

        return Offer(offer_url, offer_title, offer_region, offer_price, offer_area,
                     offer_rooms)

    @staticmethod
    def ScrapeNextPage(page_html):
        next_page_html = page_html.select('li.pager-next > a')
        if len(next_page_html) > 0:
            return next_page_html[0]['href']
        
        return None