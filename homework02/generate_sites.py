import json
import random

site_data = {"sites": []}


for i in range(1,6):
    latitude = round(random.uniform(16.0, 18.0), 6)
    longitude = round(random.uniform(16.0, 18.0), 6)
    composition = random.choice(["stony", "iron", "stony-iron"])

    site = { 
        "site_id": i,
        "latitude": latitude,
        "longitude": longitude,
        "composition": composition
    }


    site_data["sites"].append(site)

with open("landing_sites.json", "w") as r:
    json.dump(site_data, r, indent=2)


    





