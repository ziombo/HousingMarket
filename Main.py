from OtoDomOperations import OtodomOperations

url = 'https://www.otodom.pl/wynajem/mieszkanie/warszawa/'

od_controller = OtodomOperations()
offers = od_controller.download_otodom_offers(no_of_pages=3, delay=5)

# print(*offers, '\n')
# with DbHelper() as db:
# db.ClearOffersTable()
# db.save_offers(offers)
