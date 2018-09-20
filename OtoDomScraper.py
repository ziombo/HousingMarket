from urllib.parse import urldefrag
from Models import Offer


def get_offers_from_soup(html_soup):
    offers_soup = html_soup.find_all('article', class_='offer-item')
    return scrape_offers(offers_soup)


def scrape_offers(offers_soup):
    offers = list()
    for offer_soup in offers_soup:
        offer = scrape_offer(offer_soup)
        if not any(offer.Url == o.Url and offer.Title == o.Title for o in offers):
            offers.append(offer)

    print("Found:", len(offers), "offers")
    return offers


def scrape_offer(offer_soup):
    offer_url = urldefrag(offer_soup['data-url'])[0]

    offer_title = offer_soup.find(class_='offer-item-title').get_text(strip=True)

    offer_region = offer_soup.find('p', class_=['text-nowrap hidden-xs']).get_text(
        strip=True)
    # Getting rid of "Mieszkanie na wynajem: " and splitting offer_region to parts
    offer_region = \
        list(map(str.strip, offer_region[offer_region.index(':') + 2:].split(',')))
    city, district, street = _get_address_parts_from_region(offer_region)

    offer_price = offer_soup.find(class_='offer-item-price').get_text(strip=True)
    # Getting rid of currency
    offer_price = offer_price[:offer_price.index('zł')]

    offer_area = offer_soup.find(class_='offer-item-area').get_text(strip=True)
    # Getting rid of square meters sign
    offer_area = offer_area[:offer_area.index('m')]

    offer_rooms = offer_soup.find(class_='offer-item-rooms').get_text(strip=True)[0]

    return Offer(offer_url, offer_title, city, district, street,
                 offer_price,
                 offer_area,
                 offer_rooms)


def scrape_next_page(page_soup):
    next_page_soup = page_soup.select('li.pager-next > a')
    return next_page_soup[0]['href'] if len(next_page_soup) > 0 else None


def _get_address_parts_from_region(region):
    if len(region) < 3:
        region.append('')
        return _get_address_parts_from_region(region)
    else:
        return region
