from urllib.parse import urldefrag
from Models import Offer


def get_offers_from_html(html_soup):
    offers_html = html_soup.find_all('article', class_='offer-item')
    offers = scrape_offers(offers_html)

    return offers


def scrape_offers(offers_html):
    offers = list()
    for offer_html in offers_html:
        offer = scrape_offer(offer_html)
        if not any(offer.Url == o.Url and offer.Title == o.Title for o in offers):
            offers.append(offer)

    return offers


def scrape_offer(offer_html):
    offer_url = urldefrag(offer_html['data-url'])[0]

    offer_title = offer_html.find(class_='offer-item-title').get_text(strip=True)

    # TODO: Wywalić adres do innej tabeli? City/District/Street/Street_Number
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


def scrape_next_page(page_html):
    next_page_html = page_html.select('li.pager-next > a')
    return next_page_html[0] if len(next_page_html) > 0 else None
