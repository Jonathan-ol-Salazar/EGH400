import paho.mqtt.client as mqtt  # import the client1
import time
import json

# Purpose of this class is to generate fight paths with basic parameteres 
# Duration = 10 seconds 
# Distance = 1 meter
# Altitude = 1 meter 


# Parameters
duration = 10
distance = 1
altitude = 1


# Dictionary to hold JSON data
dictJSON =  { "Duration": duration, "Distance":distance, "Altitude": altitude}
# Convert dictionary to a string for publishing
stringJSON = json.dumps(dictJSON)


########################################
broker_address = "localhost"

client = mqtt.Client("FlightPlan_Publisher")  # create new instance

client.connect(broker_address)  # connect to broker

client.publish("Flight_Plans", stringJSON) # Send message to the Topic
