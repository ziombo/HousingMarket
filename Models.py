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
    def __init__(self, url, title, city, district, street, price, area, rooms):
        self.Url = url
        self.Title = title
        self.City = city
        self.District = district
        self.Street = street
        self.Price = price
        self.Area = area
        self.Rooms = rooms

    def __str__(self):
        return f'Title: {self.Title}\n Price: {self.Price}\n\n'

    def to_dict(self):
        return {
            'url': self.Url,
            'title': self.Title,
            'city': self.City,
            'district': self.District,
            'street': self.Street,
            'price': self.Price,
            'area': self.Area,
            'rooms': self.Rooms
        }