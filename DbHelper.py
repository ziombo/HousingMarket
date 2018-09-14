import dataset

class DbHelper:
    CONNECT_STRING = 'sqlite:///OtoDomOffers.db'

    def __init__(self):
        self.db = dataset.connect(self.CONNECT_STRING)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def SaveOffers(self, offers):
        print("Now saving", len(offers), "offers")
        # Using upsert to prevent saving same offers. Based on URL
        [self.db['offers'].upsert(offer.ToDict(), ['url', 'title']) for offer in offers]
        print("Offers saved successfully")

    def ClearOffersTable(self):
        if self.db['offers'].exists:
            self.db['offers'].delete()