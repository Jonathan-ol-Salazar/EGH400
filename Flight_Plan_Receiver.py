import paho.mqtt.client as mqtt #import the client1
import time
import json




def on_message(client, userdata, msg):
    print('got a message')
    data = str(msg.payload.decode("utf-8", "ignore"))
    dataJSON = json.loads(data)  # decode json data
    print(dataJSON)



########################################
broker_address="localhost" 
 
client = mqtt.Client("sub") #create new instance
client.on_message=on_message #attach function to callback  
 
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

client.subscribe("Flight_Plans")

time.sleep(10) # wait
client.loop_stop() #stop the loop