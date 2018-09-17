import dataset


class  DbHelper:
    CONNECT_STRING = 'sqlite:///HousingMarketDB.db'

    def __init__(self):
        self.db = dataset.connect(self.CONNECT_STRING)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def save_offers(self, offers):
        print("Now saving", len(offers), "offers")
        [self.save_offer(offer) for offer in offers]
        print("Offers saved successfully")

    def save_offer(self, offer):
        # Using upsert to prevent saving same offers. Based on url and title
        self.db['offers'].upsert(offer.to_dict(), ['url', 'title'])

    def clear_offers_table(self):
        if self.db['offers'].exists:
            self.db['offers'].delete()
