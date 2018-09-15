import dataset


class  DbHelper:
    CONNECT_STRING = 'sqlite:///OtoDomOffers.db'

    def __init__(self):
        self.db = dataset.connect(self.CONNECT_STRING)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def save_offers(self, offers):
        print("Now saving", len(offers), "offers")
        # Using upsert to prevent saving same offers. Based on url and title
        [self.db['offers'].upsert(offer.to_dict(), ['url', 'title']) for offer in offers]
        print("Offers saved successfully")

    def clear_offers_table(self):
        if self.db['offers'].exists:
            self.db['offers'].delete()
