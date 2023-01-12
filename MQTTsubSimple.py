 
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import numpy as np
import json
import cv2
import urllib.request

port=1883
host= 'localhost'

def nothing(x):                                                             
    pass

while True:                                                                                  #biri ciclo while para que se mantenga rebizando la coneccion a MQTT                       
    url='http://192.168.1.69/cam-lo.jpg'                                            #Asigna la URL a la cual se conecta para capturar la imagen 
    ##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)                   #Construye la ventana de visualización de la imagen captada de la url   
    img_resp=urllib.request.urlopen(url)                                    #Abre la imagen de la URL            
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)               #contruye una imagen con formato unit8 desde la anterior
    frame=cv2.imdecode(imgnp,-1)                                            #construye la imagen "frame"             
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

    msg = subscribe.simple("codigoIoT/mqtt/Detector/Min_Max_HSV", hostname='localhost')         #Establece la subscripciona  tema de MQTT
    print("%s %s" % (msg.topic, msg.payload))                                               #Imprime el tema y elcontenido del msg.payload
    datos_calibracion = json.loads(msg.payload)                                             #Variable datos_calibración contiene un json del msg.payload
    l_h = datos_calibracion["Hmin"]                                             #pasa el contenido del msg.payload a variables individuales
    l_s = datos_calibracion["Smin"]  
    l_v = datos_calibracion["Vmin"]                                             #Valores de parametros HSV minimos                                                                                      
    u_h = datos_calibracion["Hmax"]
    u_s = datos_calibracion["Smax"]
    u_v = datos_calibracion["Vmax"]                                             #Valores de parametros HSV maximos
  
    l_b = np.array([l_h, l_s, l_v])                                         #construye un array con los valores minimos de hsv
    u_b = np.array([u_h, u_s, u_v])                                         #construye un array con los valores maximos de hsv
  
                           #convierte "frame" de BGR a HSV
    mask = cv2.inRange(hsv, l_b, u_b)                                       #construye la imagen mascara con los array minimos y maximos de hsv    
    res = cv2.bitwise_and(frame, frame, mask=mask)                          #Aplica una comparación AND elemento a elemento de las matrices de imagen frame y mask
       
    #cv2.imshow("live transmission", frame)                                  #Crea ventana para ver imagen original "frame"
    #cv2.imshow("mask", mask)                                                #crea ventana para ver la imagen de filtro construido "mask"
    #cv2.imshow("res", res)                                                  #crea ventana para ver imagen resultante despues del filtro "res" 
    cv2.imwrite("/home/ramses/ImagenPythonMask.png",mask)
    cv2.imwrite("/home/ramses/ImagenPythonRes.png",res)
    cv2.imwrite("/home/ramses/ImagenPythonOriginal.png",frame)

    key=cv2.waitKey(5)
    if key==ord('q'):
        break

cv2.destroyAllWindows()