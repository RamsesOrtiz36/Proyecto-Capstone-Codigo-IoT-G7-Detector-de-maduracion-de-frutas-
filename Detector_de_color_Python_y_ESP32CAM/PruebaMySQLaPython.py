import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import mysql.connector                                                              #Biblioteca para establecer comunicación a MySQL        
import numpy as np                                                                  #Biblioteca para manejar arreglos
import json                                                                         #Biblioteca para manejar JSON
import cv2
import urllib.request

conexion1=mysql.connector.connect(host="localhost",                                 #Establece la conexión a MySQL
                                  user="Ramses",                                    #Nombre de usuario con permiso para acceder
                                  passwd="Tanis36",                                 #Contraseña para acceder a MySQL de forma remota
                                  database="Detector_de_maduracion_de_frutas")      #Nombre de la base de datos a la cual se quiere ingresar
cursor1=conexion1.cursor()                                                          #Crea el "cursor" que se usa para ingresar comandos de MySQL
def nothing(x):                                                             
    pass

global AreaMax
#AreaMax=0


msg = subscribe.simple("codigoIoT/NodeRed/Python/Medicion", hostname='localhost')         #Establece la subscripciona  tema de MQTT
print("%s %s" % (msg.topic, msg.payload))                                               #Imprime el tema y elcontenido del msg.payload
Mediciones = json.loads(msg.payload)      #Variable datos_calibración contiene un json de la base de datos MySQL 
NombreFrutaPy = Mediciones["NombreFruta"]
print(NombreFrutaPy)
if Mediciones!="":
    cursor1.execute("SELECT id, HSV FROM Calibraciones WHERE fruta='"+NombreFrutaPy+"'")    #Petición a MySQL para tomar los valores de los registros de la tabla que cumplen los requisitos
    DatosID=cursor1.fetchall()                                                  #Todos los registros de calibracion para esa fruta se almacenana en una variable tip arreglo de python
    #print(DatosID[id][2])                                                       #Visualizamos los datos que tiene la variable 
    #datos_calibracionBD = json.loads(DatosID[id][2])                            #Toma el valor de HSV de un registro y lo guarda como JSON en datos_calibración
    i=0
    for i in DatosID[0][i]:                                                        #biri ciclo while para que se mantenga rebizando la coneccion a MQTT                       
        url='http://192.168.1.69/cam-lo.jpg'                                    #Asigna la URL a la cual se conecta para capturar la imagen 
        ##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
        cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)               #Construye la ventana de visualización de la imagen captada de la url   
        img_resp=urllib.request.urlopen(url)                                    #Abre la imagen de la URL            
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)               #contruye una imagen con formato unit8 desde la anterior
        frame=cv2.imdecode(imgnp,-1)                                            #construye la imagen "frame"             
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                            #convierte "frame" de BGR a HSV
        datos_calibracionBD = json.loads(DatosID[0][i])                        #Toma el valor de HSV de un registro y lo guarda como JSON en datos_calibración

        """
        print(datos_calibracionBD["Hmin"])                                                  #Visualiza el contenido de datos_calibración
        print(datos_calibracionBD["Vmin"]) 
        print(datos_calibracionBD["Smin"]) 
        print(datos_calibracionBD["Hmax"])
        print(datos_calibracionBD["Vmax"])
        print(datos_calibracionBD["Smax"])"""
        l_h = datos_calibracionBD["Hmin"]                  #pasa el contenido del msg.payload a variables individuales
        l_s = datos_calibracionBD["Smin"]  
        l_v = datos_calibracionBD["Vmin"]                  #Valores de parametros HSV minimos                                                                                      
        u_h = datos_calibracionBD["Hmax"]
        u_s = datos_calibracionBD["Smax"]
        u_v = datos_calibracionBD["Vmax"]                  #Valores de parametros HSV maximos

        l_b = np.array([l_h, l_s, l_v])                                         #construye un array con los valores minimos de hsv
        u_b = np.array([u_h, u_s, u_v])                                         #construye un array con los valores maximos de hsv

        mask = cv2.inRange(hsv, l_b, u_b)                                       #construye la imagen mascara con los array minimos y maximos de hsv    
        res = cv2.bitwise_and(frame, frame, mask=mask)                          #Aplica una comparación AND elemento a elemento de las matrices de imagen frame y mask

        cnts, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #Encuentra los contornos de las areas que cumplen con la mascara, devuelve dos cosas, los contornos y la jerarquia de contrnos

        for c in cnts:                                                          #cnt es un arrelo que contiene el contorno, para cada c en el arreglo
            area=cv2.contourArea(c)                                             #determina el area de cada contoruno
            print(area) 
            if AreaMax<area:
                AreaMax=area
                IDdeMax=DatosID[0][i]
                print(IDdeMax)









conexion1.close()                                                                   #cerramos la conexión a la base de datos

