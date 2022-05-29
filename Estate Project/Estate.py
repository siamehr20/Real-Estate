from unittest import result


# from Agent import Superviser


class Baseproperty:
    def __init__(self, area, room_number, parking, address, **kwargs):
        self.area = area
        self.room_number = room_number
        self.parking = parking
        self.address = address

    @classmethod
    def prompt(cls, **kwargs):
        cls.area = input('enter Area :')
        cls.room_number = input("Enter Rooms: ")
        cls.parking = input('Has parking: ')
        cls.address = input('Enter address: ')

        # Baseproperty( area= cls.area, room_number = cls.room_number, parking=cls.parking, address = cls.address)

        result = {
            'Area': cls.area,
            'Room_number': cls.room_number,
            'Parking': cls.parking,
            'Address': cls.address
        }
        return result


class Apartment(Baseproperty):

    def __init__(self, floor, elevator, balcony, **kwargs):
        super().__init__(**kwargs)
        self.floor = floor
        self.elevator = elevator
        self.balcony = balcony

    @classmethod
    def prompt(cls):
        floor = input('Which floor: ')
        elevator = input('Has elevator or not?')
        balcony = input('Has balvony or not?')

        result = {
            'floor ': floor, 'balcony': balcony
            , 'elevator': elevator
        }

        result.update(Baseproperty.prompt())

        return result


class House(Baseproperty):
    def __init__(self, pool, yard, **kwargs):
        super().__init__(**kwargs)
        self.pool = pool
        self.yard = yard

    @classmethod
    def propmt(cls):
        pool = input('Has pool ? ')
        yard = input('Has Yard? ')
        result = {
            'pool': pool, 'yard': yard
        }
        return result


class Rental:

    def __init__(self, pre_paid, monthly, **kwargs):
        super().__init__(**kwargs)
        self.pre_paid = pre_paid
        self.monthly = monthly

    @classmethod
    def prompt(cls):
        pre_paid = input('Enter Pre_paid Amount: ')
        monthly = input('Enter Monthly Amount: ')

        result = {
            'pre_paid': pre_paid, 'monthly': monthly
        }
        return result


class Purchasable:
    def __init__(self, cost, **kwargs):
        super().__init__(**kwargs)
        self.cost = cost

    @classmethod
    def prompt(cls):
        return {' cost': input('Enter the Cost ')}
