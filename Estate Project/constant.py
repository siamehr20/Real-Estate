from Supervisor_main import Run_Supervisor_Mood
from Agent_main import Run_Agent_Mood
from Profile import ApartmentRental, ApartmentPurchase, HouseRental, HousePurchase


SUPERVISER_CREDENTIALS = [{
    'username': 'admin',
    'password': '1234'
}]
RUNNNIG_MOOD = {
    '0' : Run_Agent_Mood,
    '1' : Run_Supervisor_Mood
}
AGENTS_FILE_PATH = 'D:\projects\Estate Project\Fixtures\Agents_data.json'

PROFILE_MAPPER = {
    ('house' , 'rental') : HouseRental ,
    ('house' , 'purchase') :HousePurchase ,
    ('apartment' , 'rental') : ApartmentRental,
    ('apartment' , 'purchase') : ApartmentPurchase
}