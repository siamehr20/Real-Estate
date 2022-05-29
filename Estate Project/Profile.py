
from unittest import result
from Estate import Apartment, Rental, Purchasable, House

class ApartmentRental(Apartment, Rental):
    @classmethod
    def prompt (cls):
        result = Apartment.prompt()
        result.update(Rental.prompt())
        return result


class ApartmentPurchase(Apartment, Purchasable):
    @classmethod
    def prompt (cls):
        result = Apartment.prompt()
        result.update(Purchasable.prompt())
        return result


class HouseRental(House, Rental):
    @classmethod
    def prompt (cls):
        result = House.prompt()
        result.update(Rental.prompt())
        return result


class HousePurchase(House, Purchasable):
    @classmethod
    def prompt (cls):
        result = House.prompt()
        result.update(Purchasable.prompt())
        return result






