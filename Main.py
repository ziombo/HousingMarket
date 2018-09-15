import requests
from bs4 import BeautifulSoup
from OtoDomScraper import get_offers_from_html, scrape_next_page
from DbHelper import DbHelper

url = 'https://www.otodom.pl/wynajem/mieszkanie/warszawa/'

r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')
offers = get_offers_from_html(html_soup)

print(*offers, '\n')
with DbHelper() as db:
#     # db.ClearOffersTable()
    db.save_offersd(offers)

url = scrape_next_page(html_soup)
