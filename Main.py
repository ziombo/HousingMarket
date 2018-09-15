from OtoDomController import OtodomController

url = 'https://www.otodom.pl/wynajem/mieszkanie/warszawa/'

od_controller = OtodomController()
offers = od_controller.get_otodom_offers(no_of_pages=3)

print("Found", len(offers), "offers total")
# print(*offers, '\n')
# with DbHelper() as db:
# db.ClearOffersTable()
# db.save_offers(offers)
