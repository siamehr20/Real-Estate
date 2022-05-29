from Estate import Baseproperty, Rental, Purchasable, Apartment, House
from Profile import ApartmentRental, ApartmentPurchase, HouseRental, HousePurchase


class BaseUser:

    def __init__(self, username, password, first_name, last_name, email, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def prompt(cls):
        print(' Add Agent ')
        username = input('Enter Username ? ')
        passsword = input('enter password ')
        first_name = input('Enter first_Name: ')
        last_name = input('Enter lastname: ')
        email = input('enter Email: ')

        result = {
            'username': username,
            'password': passsword,
            'first_name': first_name,
            'last_name': last_name, 'email': email
        }
        return result


class Superviser(BaseUser):
    agents_list = []
    properties_list = {}
    deal_list = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def create_agent():
        agent_data = Agent.prompt()
        agent = Agent(**agent_data)
        return agent

    @classmethod
    def agent_data(cls):
        tmp = []
        for agent in cls.agents_list:
            tmp.append(agent.serializer())
        return tmp

    @classmethod
    def search(cls, username):
        for agent in cls.agents_list:
            if agent.username == username:
                return agent
            else:
                return None


class Agent(BaseUser):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        Superviser.agents_list.append(self)
        self.properties_list = []
        self.deal_list = []
        self.__has_access = False

    @classmethod
    def prompt(cls):
        return BaseUser.prompt()

    def serializer(self):
        data = self.__dict__
        data.pop('properties_list')
        data.pop('deal_list')
        data.pop('_Agent__has_access')
        return data

    def check_password(self, password):
        check = bool(self.password == password)
        if check:
            self.__has_access = True
        return check

    def has_access(self):
        return self.__has_access

    def check_access(func):
        def wrapper(self):
            if self.has_access():
                # print('Has Access ')
                func(self)
            else:
                print('Agent has No Access...! ')

        return wrapper

    @check_access
    def create_new(self):
        pr_type = input('Enter the type with two word: ').lower()
        from constant import PROFILE_MAPPER
        ProfileClasss = PROFILE_MAPPER[tuple(tp for tp in pr_type.split())]
        prop_data = ProfileClasss.prompt()
        self.properties_list.append(prop_data)
        Superviser.properties_list[self.username] = prop_data

    def search_deal():
        pass
