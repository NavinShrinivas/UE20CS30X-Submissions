#!/usr/bin/env python3


import json 
import sys
import math


distance = float(sys.argv[1])
source_lat = float(sys.argv[2])
source_lon = float(sys.argv[3])

output = ""

for line in sys.stdin :
    try :
        json_obj = json.loads(line.strip())
    except:
        continue
    humidity = float(json_obj["humidity"])
    if math.isnan(humidity) == False and humidity > 48 and humidity < 54 :
        temperature = float(json_obj["temperature"])
        if math.isnan(temperature) == False and temperature > 20 and temperature < 24: 
            timestamp = json_obj["timestamp"]
            dest_lat = float(json_obj["lat"])
            dest_lon = float(json_obj["lon"])
            euc_dist = math.sqrt(math.pow((dest_lat-source_lat),2)+math.pow((dest_lon-source_lon),2))
            if euc_dist < distance:
                output += timestamp+"\n"
print(output)

