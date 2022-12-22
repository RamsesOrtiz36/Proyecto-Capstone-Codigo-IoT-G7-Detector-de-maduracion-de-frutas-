import mysql.connector                                                              #Biblioteca para establecer comunicación a MySQL        
import numpy as np                                                                  #Biblioteca para manejar arreglos
import json                                                                         #Biblioteca para manejar JSON

conexion1=mysql.connector.connect(host="localhost",                                 #Establece la conexión a MySQL
                                  user="Ramses",                                    #Nombre de usuario con permiso para acceder
                                  passwd="Tanis36",                                 #Contraseña para acceder a MySQL de forma remota
                                  database="Detector_de_maduracion_de_frutas")      #Nombre de la base de datos a la cual se quiere ingresar
cursor1=conexion1.cursor()                                                          #Crea el "cursor" que se usa para ingresar comandos de MySQL
cursor1.execute("SELECT id, fruta, HSV FROM Calibraciones WHERE fruta='Fruta3'")    #Petición a MySQL para tomar los valores de los registros de la tabla que cumplen los requisitos
DatosID=cursor1.fetchall()                                                          #Los registros tomados se almacenana en una variable de python
print(DatosID[3][2])                                                                #Visualizamos los datos que tiene la variable 
datos_calibracion = json.loads(DatosID[3][2])                                       #Toma el valor de HSV de un registro y lo guarda como JSON en datos_calibración
print(datos_calibracion["Hmin"])                                                    #Visualiza el contenido de datos_calibración
print(datos_calibracion["Vmin"]) 
print(datos_calibracion["Smin"]) 
print(datos_calibracion["Hmax"])
print(datos_calibracion["Vmax"])
print(datos_calibracion["Smax"])
l_h = datos_calibracion["Hmin"]                  #pasa el contenido del msg.payload a variables individuales
l_s = datos_calibracion["Smin"]  
l_v = datos_calibracion["Vmin"]                                             #Valores de parametros HSV minimos                                                                                      
u_h = datos_calibracion["Hmax"]
u_s = datos_calibracion["Smax"]
u_v = datos_calibracion["Vmax"]                                             #Valores de parametros HSV maximos
  











conexion1.close()                                                                   #cerramos la conexión a la base de datos

