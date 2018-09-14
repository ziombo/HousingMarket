class Address:
    def __init(self, city, district, street, street_number):
        self.City = city,
        self.District = district,
        self.Street = street,
        self.Street_Number = street_number

    def to_dict(self):
        return {
            'city': self.City,
            'district': self.District,
            'street': self.Street,
            'street_number': self.Street_Number
        }


class Offer:
    def __init__(self, url, title, region, price, area, rooms):
        self.Url = url
        self.Title = title
        self.Region = region
        self.Price = price
        self.Area = area
        self.Rooms = rooms

    def to_dict(self):
        return {
            'url': self.Url,
            'title': self.Title,
            'region': self.Region,
            'price': self.Price,
            'area': self.Area,
            'rooms': self.Rooms
        }