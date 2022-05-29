

import sys
from Estate import Apartment
from utils import check_credentials
from Agent import Superviser , Agent
from Profile import ApartmentRental, ApartmentPurchase, HouseRental, HousePurchase
from Store import save_to_file , load_data


def Auth():
    pass



def Run_Agent_Mood():
    from constant import AGENTS_FILE_PATH
    agents_data = load_data(AGENTS_FILE_PATH)
    a = [ Agent(**d) for d in agents_data]
    agent =None
    print('***** Agent Login *****')
    while agent is None:
        username = input(' Enter Your Username: ')
        Superviser.search(username)
        if agent is None:
            print(f' {username} Not Found!  ')

    password = input(' Enter Your Password: ')
    if agent.check_password(password):
        print(f'**** Welcome {agent.username} **** ')
        agent.create_new()

    else:
        print('Wrong user or pass')