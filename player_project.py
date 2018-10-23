from item_project import *
from map_project import rooms

inventory = []
#For example: item_id

# Start game at the reception
current_room = rooms["Reception"]

#====================================
# Player status
energy_min = 0
#Minimum energyof player

energy_max = 100
#Maximum energy of player

project_process = 0
#Original project process

project_process_max = 100
#Maximum project process
