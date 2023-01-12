"""
Programa creado por Ramses Ortiz Castro 
Fecha: 07 de Enero del 2023
Se realizo este programa como prueba acceder a la base de datos de MyQSL desde python
a la tabla de "Calibraciones" tomar los registros que tengan el nombre de fruta= Fruta1
pasarlos a una variable de python y de esos registros tomar del parametro HSV los valores 
de HSV minimos y maximos de calibraciones, estos estan en formato string y se psasn a formato JSON,
en python se maneja como diccionario el arreglo {key:value, key:value,..}
accedimos a cada "value" usando su "key".
El 11 de enero agregue la biblioteca de argparse para poder usar argumentos desde node red dentro de
el programa de python, tambien comprobe que el resultado de print() en python sale como output del node 
exe en node-red.
"""
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import mysql.connector                                                              #Biblioteca para establecer comunicación a MySQL        
import numpy as np                                                                  #Biblioteca para manejar arreglos
import json                                                                         #Biblioteca para manejar JSON
import cv2
import urllib.request
import argparse

#MySQL 
conexion1=mysql.connector.connect(host="localhost",                                 #Establece la conexión a MySQL
                                  user="Ramses",                                    #Nombre de usuario con permiso para acceder
                                  passwd="Tanis36",                                 #Contraseña para acceder a MySQL de forma remota
                                  database="Detector_de_maduracion_de_frutas")      #Nombre de la base de datos a la cual se quiere ingresar
cursor1=conexion1.cursor()                                                          #Crea el "cursor" que se usa para ingresar comandos de MySQL
def nothing(x):                                                             
    pass

global AreaMax
#AreaMax=0

#Argumentos desde Node-Red
# Parser
parser = argparse.ArgumentParser()
parser.add_argument("NombreFruta", help="Nombre de la fruta seleccionada desde Node red")
#parser.add_argument("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

Fruta = args.NombreFruta

print ("El nombre de fruta recibida es: " + Fruta)


#MQTT
"""msg = subscribe.simple("codigoIoT/NodeRed/Python/Medicion", hostname='localhost')         #Establece la subscripciona  tema de MQTT
print("%s %s" % (msg.topic, msg.payload))  """                                             #Imprime el tema y elcontenido del msg.payload
Mediciones= "Msg Payload"      #Variable datos_calibración contiene un json de la base de datos MySQL 
NombreFrutaPy = Fruta
print(NombreFrutaPy)
if Mediciones!="":
    cursor1.execute("SELECT id, HSV,DiasRest FROM Calibraciones WHERE fruta='"+NombreFrutaPy+"'")    #Petición a MySQL para tomar los valores de los registros de la tabla que cumplen los requisitos
    DatosIDLista=cursor1.fetchall()                       #Todos los registros de calibracion para esa fruta se almacenana en una variable tipo lista de python, diferente a arreglo
    print(DatosIDLista)                                   #Imprime contenido de la variable tipo lista  
    print(len(DatosIDLista))                              #Imprime la cantidad de elementos que tiene la lista desde 1               
    #print(type(DatosIDLista[1][1]))                       #Imprime el tipo de variable del elemento seleccionado, en este caso "str"             
    for i in range(0,len(DatosIDLista)):
        DatosIDJSON= json.loads(DatosIDLista[i][1])           #Toma el elemento de la lista y lo convierte a "diccionario" que funcionca como JSON  
        #print(type(DatosIDJSON))                              #Ve que tipo de variable es, en este caso "Dict= diccionario= {Key:value,key:valu,...}"              
        #print(DatosIDJSON)                                    #Imprime el contenido de la variable tipo Dict  
        Hmax=DatosIDJSON['Hmax']                              #Accede al diccionario y toma el valor de Hmax y lo guarda e variable de python Hmax
        Hmin=DatosIDJSON['Hmin']
        Smin=DatosIDJSON['Smin']
        Vmin=DatosIDJSON['Vmin']
        Smax=DatosIDJSON['Smax']
        Vmax=DatosIDJSON['Vmax']
        print(Hmax,Smax,Vmax, DatosIDLista[i][2], sep=" ")     #imprime valor de Hmax y el valor de "DiasRest"


    """
    for i in range(0,len(DatosIDLista)):
        print(DatosIDLista[i][1])
    
    DatosIDJSON= json.dumps(DatosIDtupla[1][1])
    print(type(DatosIDJSON))
    print(DatosIDJSON)
    """