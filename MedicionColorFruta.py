"""
Programa creado por Ramses Ortiz Castro
Fecha: 08 de Enero de 2023

Este programa es para la medicion de color de las frutas, 
toma el nombre de la fruta para buscar en base de datos las calibraciones
de colores y su maduración.

Toma la calibración 1, genera mascara filtro, detecta cuanta area tiene ese filtro, guarda el area mas alta, 
toma la siguiente calibración,repite proceso hasta terminar con todas las calibraciones disponibles de esa fruta
y en cada una compara el area encontrada, guarda solo el area mas alta y su id de registro, 
al final usa el id de registro para tomar el valor de dias restantes de ese registro 
y lo entrega como resultado

Usa comunicación URL, Analisis de imagen, MQTT, MySQL y guarda archivo local.
Desde Node-red se ejecuta el programa de python, node-red envia mensaje MQTT con nombre de fruta,
Python toma el nombre y lo usa para buscar en MySQL la tabla Calibraciones y toma los registros con el nombre de la fruta.
Python toma imagen de URL, la transforma de RGB a HSV, aplica filtros y calcula areas.
Python procesa datos y devuelve valor resultado
"""
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import numpy as np
import json
import cv2
import urllib.request
import mysql.connector
import argparse

#MySQL
port=1883
host= 'localhost'
conexion1=mysql.connector.connect(host="localhost",                                 #Establece la conexión a MySQL
                                  user="Ramses",                                    #Nombre de usuario con permiso para acceder
                                  passwd="Tanis36",                                 #Contraseña para acceder a MySQL de forma remota
                                  database="Detector_de_maduracion_de_frutas")      #Nombre de la base de datos a la cual se quiere ingresar
cursor1=conexion1.cursor()                                                          #Crea el "cursor" que se usa para ingresar comandos de MySQL

def nothing(x):                                                             
    pass

#Argumentos desde Node-Red
# Parser
parser = argparse.ArgumentParser()
parser.add_argument("NombreFruta", help="Nombre de la fruta seleccionada desde Node red")
args = parser.parse_args()
Fruta = args.NombreFruta

#Adquiere la imagen desde URL
#while True:                                                            #ciclo while para que se mantenga rebizando la coneccion a MQTT                       
url='http://192.168.1.69/cam-lo.jpg'                                    #Asigna la URL a la cual se conecta para capturar la imagen 
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)               #Construye la ventana de visualización de la imagen captada de la url   
img_resp=urllib.request.urlopen(url)                                    #Abre la imagen de la URL            
imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)               #construye una imagen con formato unit8 desde la anterior
frame=cv2.imdecode(imgnp,-1)                                            #construye la imagen "frame"             
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                            #convierte "frame" de BGR a HSV

#Entra a MySQL y toma los registros con el nombre de fruta
cursor1.execute("SELECT id, HSV, DiasRest FROM Calibraciones WHERE fruta='"+Fruta+"'")    #Petición a MySQL para tomar los valores de los registros de la tabla que cumplen los requisitos
DatosID=cursor1.fetchall()                                                          #Los registros tomados se almacenana en una variable de python

"""Tomar 1 registro, crear el filtro, aplicarlo, determinar area y guardar el ID del
    registro que tenga el area más grande
"""
AreaMax=0
#Toma una calibración para construir el filtro y aplicarlo, luego repite con la siguiente calibración
for i in range(0,len(DatosID)):
    datos_calibracionBD = json.loads(DatosID[i][1])                                       #Toma el valor de HSV de un registro y lo guarda como JSON en datos_calibración
    l_h = datos_calibracionBD["Hmin"]                  #pasa el contenido del msg.payload a variables individuales
    l_s = datos_calibracionBD["Smin"]  
    l_v = datos_calibracionBD["Vmin"]                                             #Valores de parametros HSV minimos                                                                                      
    u_h = datos_calibracionBD["Hmax"]
    u_s = datos_calibracionBD["Smax"]
    u_v = datos_calibracionBD["Vmax"]                                             #Valores de parametros HSV maximos
    #Construye filtro
    l_b = np.array([l_h, l_s, l_v])                                         #construye un array con los valores minimos de hsv
    u_b = np.array([u_h, u_s, u_v])                                         #construye un array con los valores maximos de hsv
    mask = cv2.inRange(hsv, l_b, u_b)                                       #construye la imagen mascara con los array minimos y maximos de hsv    
    res = cv2.bitwise_and(frame, frame, mask=mask)                          #Aplica una comparación AND elemento a elemento de las matrices de imagen frame y mask
    
    areaTotal=0
    cnts, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #Encuentra los contornos de las areas que cumplen con la mascara, devuelve dos cosas, los contornos y la jerarquia de contrnos
    for c in cnts:                                                          #cnt es un arrelo que contiene el contorno, para cada c en el arreglo
        areaTotal+=cv2.contourArea(c)                                             #determina el area acumulada de cada contorno
    if (AreaMax<areaTotal):
        AreaMax=areaTotal
        DiasRestareaMax=json.loads(DatosID[i][2])

print(DiasRestareaMax)


#cv2.imshow("live transmission", frame)                                  #Crea ventana para ver imagen original "frame"
#cv2.imshow("mask", mask)                                                #crea ventana para ver la imagen de filtro construido "mask"
#cv2.imshow("res", res)                                                  #crea ventana para ver imagen resultante despues del filtro "res" 
cv2.imwrite("/home/ramses/ImagenPythonMask2.png",mask)
cv2.imwrite("/home/ramses/ImagenPythonRes2.png",res)
cv2.imwrite("/home/ramses/ImagenPythonOriginal2.png",frame)

"""
    key=cv2.waitKey(5)
    if key==ord('q'):
        break
        
cv2.destroyAllWindows()
"""