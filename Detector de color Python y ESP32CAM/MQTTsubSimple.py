 
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import numpy as np
import json
import cv2

port=1883
host= 'localhost'

url='http://192.168.1.70/cam-lo.jpg'                                            #Asigna la URL a la cual se conecta para capturar la imagen 
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)                   #Construye la ventana de visualización de la imagen captada de la url    


while True:
    msg = subscribe.simple("codigoIoT/mqtt/Detector/Min_Max_HSV", hostname='localhost')
    print("%s %s" % (msg.topic, msg.payload))

    key=cv2.waitKey(5)
    if key==ord('q'):
        break