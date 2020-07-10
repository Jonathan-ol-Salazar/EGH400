import paho.mqtt.client as mqtt  # import the client1
import time
import json

# Purpose of this class is to generate fight paths with basic parameteres
# Duration = 10 seconds
# Distance = 1 meter
# Altitude = 1 meter


# Parameters
duration = 10  # Seconds
distance = 1  # Meters
altitude = 1  # Meters

# Example Times, ISO-8601
startTime = "2020-07-29T00:00:00Z"
endTime =   "2020-07-29T00:00:10Z"

locationAMSL = "42,-70,0' AMSL" 
radius = "1m" 
height = "1m"

points = [[1,1], [1,2]]

dictJSON = {"start_time": startTime, "expire_time": endTime, "location": locationAMSL, "points": points, "altitude":altitude}


# Dictionary to hold JSON data
# dictJSON =  { "Duration": duration, "Distance":distance, "Altitude": altitude}
dictJSON_BC = {"start_time": startTime, "expire_time": endTime, "location": locationAMSL, "radius": radius, "height":height}


# Convert dictionary to a string for publishing
stringJSON = json.dumps(dictJSON, indent=2)
print(stringJSON)

stringJSON_BC = json.dumps(dictJSON_BC, indent=2)
print(stringJSON_BC)

########################################
broker_address = "localhost"

client = mqtt.Client("FlightPlan_Publisher")  # create new instance

client.connect(broker_address)  # connect to broker

client.publish("Flight_Plans", stringJSON)  # Send message to the Topic
