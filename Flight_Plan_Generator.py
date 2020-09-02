import paho.mqtt.client as mqtt  # import the client1
import time
import json

# Purpose of this class is to generate fight paths with basic parameteres
# Duration = 10 seconds
# Distance = 1 meter
# Altitude = 1 meter


# Initial Parmeters (10 seconds, 1 meter, 1 meter)
duration = 10  
distance = 1  
altitude = 1  

# Maximum Parmeters (600 seconds (10 mins), 1 km, 20m)
duration = 600  
distance = 1000
altitude = 20  

# Start Coords (Only X, because Y = altitude)
startX = 0

# Example Times, ISO-8601
startTime = "2020-07-29T00:00:00Z"
endTime =   "2020-07-29T00:10:00Z"

locationAMSL = "42,-70,0' AMSL" 
radius = "1m" 
height = "20m"

# Spacing between points
spacing = 20

# For loop to make a list of tuples containing coords. X will be 'distance' split into 20m increments, Y is altitude
points = [(startX, altitude)]
# Check distance is not 0
if distance != 0:
    for i in range(1, int(distance/spacing)+1):
        points.append((i*spacing, altitude))



# points = [[1,1], [1,2]]

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
