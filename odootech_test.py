import os
from os.path import join, getsize
import json

class cars:
    def __init__(self,dict1):
        self.__dict__.update(dict1)

class bikes:
    def __init__(self,dict1):
        self.__dict__.update(dict1)

vehicle_list = []

def from_file_json_to_object_list():
    for root, dirs, files in os.walk('data'):
        for name in files:
            filename = os.path.join(root, name)
            print("Opening file :" + str(name))
            with open(filename) as task_dat:
                print("Creating ID : name key : value pair for entry")
                full_dict = {"ID": name}
                print("Getting contents from :" + str(name))
                contents = json.loads(task_dat.read())
                if contents["type"] == "bicikli":
                    print("instantiating bikes")
                    full_dict.update(contents)
                    bicikli = bikes(full_dict)
                    print("appending bikes instance found in current iteration of loop to vehicles_list")
                    vehicle_list.append(bicikli)
                elif contents["type"] == "auto":
                    print("instantiating cars")
                    full_dict.update(contents)
                    car = cars(full_dict)
                    print("appending cars instance found in current iteration of loop to vehicles_list")
                    vehicle_list.append(car)
    return vehicle_list

def object_list_elements_formatted_listing(list_containing_vehicles):
    print("listing entries of vehicle_list:")
    for vehicle in list_containing_vehicles:
        #print(vehicle.__dict__)
        vehicle_id = vehicle.ID
        vehicle_type = vehicle.type
        vehicle_marka = vehicle.marka
        if vehicle_type == "bicikli":
            vehicle_weight_limit = vehicle.terhelhetoseg
            print(f"""{vehicle_id}'s properties :
            \tVehicle's type: {vehicle_type}
            \tVehicle's weight limit: {vehicle_weight_limit}
            \tVehicle's brand: {vehicle_marka}""")
        elif vehicle_type == "auto":
            vehicle_ajtok_szama = vehicle.ajtok_szama
            print(f"""{vehicle_id}'s properties :
            \tVehicle's type: {vehicle_type}
            \tVehicle's number of doors: {vehicle_ajtok_szama}
            \tVehicle's brand: {vehicle_marka}""")

object_list_elements_formatted_listing(from_file_json_to_object_list())
