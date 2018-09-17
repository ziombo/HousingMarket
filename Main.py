from OtoDomOperations import OtodomOperations

# TODO: Wywalić adres do innej tabeli (City/District/Street/Street_Number)
# TODO: Przenieść sprawdzanie czy oferty są w liśćie na wyższy poziom

url = 'https://www.otodom.pl/wynajem/mieszkanie/warszawa/'

od_controller = OtodomOperations()
offers = od_controller.download_otodom_offers(no_of_pages=20, delay=5)


# print(*offers, '\n')
# with DbHelper() as db:
# db.ClearOffersTable()
# db.save_offers(offers)
