import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos) 
    print("message retain flag=",message.retain)
########################################
broker_address="localhost" 
#broker_address="iot.eclipse.org"
 
client = mqtt.Client("sub") #create new instance
client.on_message=on_message #attach function to callback  
 
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

client.subscribe("house/bulbs/bulb1")

time.sleep(10) # wait
client.loop_stop() #stop the loop