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



dataJSON =  '{ "name":"John", "age":30, "city":"New York"}'

########################################
broker_address = "localhost"

client = mqtt.Client("pub")  # create new instance

client.connect(broker_address)  # connect to broker

client.publish("Flight_Plans", dataJSON)
