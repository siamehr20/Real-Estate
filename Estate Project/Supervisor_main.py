import sys
from Estate import Apartment
from utils import check_credentials
from Agent import Superviser , Agent
from Profile import ApartmentRental, ApartmentPurchase, HouseRental, HousePurchase
from Store import save_to_file , load_data
# from constant import AGENTS_FILE_PATH
# if __name__ == '__main__':

    # sys.argv.append('admin')
    # sys.argv.append('123')

    # print(sys.argv[2])
def Run_Supervisor_Mood():
    pass

    if check_credentials(sys.argv):
        print('correct info...')
        exit = None
        while exit != '1':
            agent = Superviser.create_agent()
            from constant import AGENTS_FILE_PATH
            exit = input('Continue(0) _Exit(1)')
            if exit =='1':
                save_to_file(AGENTS_FILE_PATH , Superviser.agent_data())

    else:
        print('Wrong user or pass')



# ap  = Apartment.prompt()
# print(pr1.area)
