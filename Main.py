


url = 'https://www.otodom.pl/wynajem/mieszkanie/warszawa/'

r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')
offers = ScrapingHelper.GetOffersFromHtml(html_soup)

#offers_html = html_soup.find_all('article', class_='offer-item')

#offers = list()
#for offer in offers_html:
    #offers.append(ScrapingHelper.ScrapeOffer(offer))


with DbHelper() as db:
    #db.ClearOffersTable()
    db.SaveOffers(offers)

url = ScrapingHelper.ScrapeNextPage(html_soup)