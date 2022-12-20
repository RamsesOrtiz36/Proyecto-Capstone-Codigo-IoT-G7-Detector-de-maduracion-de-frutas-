import cv2                                  #Biblioeca
import urllib.request                       #Biblioeca
import numpy as np                          #Biblioeca
from paho.mqtt import client as mqtt_client # Bilbioteca para comunicación por MQTT
import random                               #Bilbioteca de numero aleatorio
def nothing(x):
    pass


#change the IP address below according to the
#IP shown in the Serial monitor of Arduino code
url='http://192.168.1.70/cam-lo.jpg'                        #Declara el valor de url con la dirección en donde se envia la info el ESP32CAM 
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)   #Construye la ventana  de la imagen campturada desde la ESP32CAM

"""
broker = '192.168.1.67'                                     #Datoa para la comunicación por MQTT
port = 1883
topic = "codigoIoT/mqtt/python"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
 
#Conexion al broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Suscripción
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message
"""

cv2.namedWindow("Tracking")                                     #Construye la ventana de las barras deslizantes de las variables        
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)           #Construye las barras deslizantes de las variables
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
 


while True:                                                         #Ejecuta el codigo continuamente dentro del while
    img_resp=urllib.request.urlopen(url)                            #Abre la url donde el ESP32CAM envia la imagen
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)       #Lee la imagen en formato de array con la biblioteca de numpy= np
    frame=cv2.imdecode(imgnp,-1)                                    #Crea la imagen con el array 
    cv2.imwrite("/home/ramses/ImagenPythonOriginal.png",frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                    #Convierte la imagen del array BGR a HSV= hue, saturation y value brigthness
 
    l_h = cv2.getTrackbarPos("LH", "Tracking")                      #toma el valor minimo de la barra de deslizamiento como valor minimo del parametro h    
    l_s = cv2.getTrackbarPos("LS", "Tracking")                      #valor minimo de s
    l_v = cv2.getTrackbarPos("LV", "Tracking")                      #valor minimo de v    
 
    u_h = cv2.getTrackbarPos("UH", "Tracking")                      #Valor maximo de h
    u_s = cv2.getTrackbarPos("US", "Tracking")                      #valor maximo de s
    u_v = cv2.getTrackbarPos("UV", "Tracking")                      #valor maximo de v
 
    l_b = np.array([l_h, l_s, l_v])                                 #Construye el arreglo de valores minimos
    u_b = np.array([u_h, u_s, u_v])                                 #Construye el array de valores maximos
    
    mask = cv2.inRange(hsv, l_b, u_b)                               #De la imagen (array) hsv selecciona los elementos dentro del rango minimo y maximo 
    res = cv2.bitwise_and(frame, frame, mask=mask)                  #Aplica la exclusion de la "mask" en el array "frame" y da imagen "res"
    
    cv2.imshow("live transmission", frame)                          #Muestra la ventana construida de frame nombre de ventana "live transmission"
    cv2.imshow("mask", mask)                                        #Muestra la ventana mask nombre "mask"    
    cv2.imshow("res", res)                                          #Muestra ventana res nombre "res"
    cv2.imwrite("/home/ramses/ImagenPythonMask.png",mask)
    cv2.imwrite("/home/ramses/ImagenPythonRes.png",res)
    key=cv2.waitKey(5)                                              #espera cada 5 milisegundos la interrucion de una tecla
    if key==ord('q'):                                               #Si la tecla fue 'q' salir del ciclo while 
        break
    
cv2.destroyAllWindows()                                             #borra todas las ventanas        