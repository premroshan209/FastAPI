# Import this module in main.py
# This database.py file handles all JSON file operations for shipments
# It loads data from shipments.json into a dictionary on startup
# and provides a save function to write updates back to the JSON file.

import json

shipments = {}

with open("shipments.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
    for item in data:
        shipments[item["id"]] = item

# print("Shipments data loaded from shipments.json")
# print(shipments)

# print(type(shipments))

def save():
    with open("shipments.json", "w") as json_file:
        # json.dump(data -> file)
        json.dump(list(shipments.values()), json_file)