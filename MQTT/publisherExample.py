import paho.mqtt.client as mqtt  # import the client1
import time

############
 
########################################
broker_address = "localhost"
# broker_address="iot.eclipse.org"

client = mqtt.Client("pub")  # create new instance

client.connect(broker_address)  # connect to broker

client.publish("house/bulbs/bulb1", "OFF")
