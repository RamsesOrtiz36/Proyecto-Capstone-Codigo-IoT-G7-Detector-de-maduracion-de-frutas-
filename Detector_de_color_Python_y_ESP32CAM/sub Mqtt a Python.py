 
import paho.mqtt.client as mqtt
import numpy as np
import json

port=1883
host= 'localhost'
 
 
def on_connect(client, userdata, flags_dict, rc):
    print("Conectado a mqtt" + str(rc))
    client.subscribe("codigoIoT/mqtt/Detector/Min_Max_HSV") # Suscríbete a la prueba temática
 
def on_message(client, userdata, msg):
    #print (msg.topic+" "+str(msg.payload))
    datos_json= json.loads(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost",1883,60)
client.loop_forever()
