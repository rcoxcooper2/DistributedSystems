# Generating landing site data and calculating travel time between sites


## Overview
In this project I sought to generate 5 landing landing sites on mars and simulate the travel time between each site.

 

## Script Descriptions
generate_sites.py: generates 5 "sites" with randomly generated latitudes, longitudes, and a composition type of the meteorite (randomly chosen from 3 different types). A json file is then created and populated with the data

calculate_trip.py: uses the latitudes, longitudes, an composition times of each site/meteorite to calculate the travel time between the sites and the total travel time to visit all 5. This is done using the great-circle distance algorithm: d = rcos-1[cos a cos b cos(x-y) + sin a sin b]

## Instructions: 
-Simply execute generate_sites.py and the json file will be created and populated
-Next, execute calculate_trip.py to be outputted the travel details
