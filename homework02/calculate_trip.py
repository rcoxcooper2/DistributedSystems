import json
import math
#Great circle formula: 
#d = rcos-1[cos a cos b cos(x-y) + sin a sin b]

def greatCircle(lat1, lon1, lat2, lon2):
    #convery degrees to radians
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(math.radians, [lat1, lon1, lat2, lon2])
    change_in_lon = lon2_rad - lon1_rad
    innermath = math.sin(lat1_rad) * math.sin(lat2_rad) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(change_in_lon)
    distance = math.acos(innermath)
    planet_radius = 3389.5  # Mars radius in kilometers
    distance *= planet_radius
    return distance


def calc_trip(site_info):
    start = {"latitude": 16.0, "longitude": 82.0}
    speed = 10
    time_elapsed = 0

    number_of_legs = len(site_info)

    #iterate through each site
    for i in range(number_of_legs):
        site = site_info[i]
        dist_to_site = greatCircle(start["latitude"], start["longitude"], site["latitude"], site["longitude"])
        
        travelTime = dist_to_site / speed


        #stop for samples
        composition = site["composition"]
        if composition == "stony":
            sampleTime = 1
        elif composition == "iron":
            sampleTime = 2
        elif composition == "stony-iron":
            sampleTime = 3
        else:
            sampleTime = 0           
        
        print(f"Leg = {i + 1}, Travel Time = {travelTime:.2f} hours, Sample Time = {sampleTime} hours")
        time_elapsed += (travelTime + sampleTime)

        # new start point for the next leg
        start["latitude"] = site["latitude"]
        start["longitude"] = site["longitude"]
    
    print("*" * 30)
    print(f"Number of Legs = {number_of_legs}, Total Time = {time_elapsed:.2f} hr")




with open('landing_sites.json', 'r') as r:
    site_data = json.load(r)

calc_trip(site_data['sites'])