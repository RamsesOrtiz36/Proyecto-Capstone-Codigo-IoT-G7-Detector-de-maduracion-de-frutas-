import mysql.connector                                                              #Biblioteca para establecer comunicación a MySQL        

conexion1=mysql.connector.connect(host="localhost",                                 #Establece la conexión a MySQL
                                  user="Ramses",                                    #Nombre de usuario con permiso para acceder
                                  passwd="Tanis36",                                 #Contraseña para acceder a MySQL de forma remota
                                  database="Detector_de_maduracion_de_frutas")      #Nombre de la base de datos a la cual se quiere ingresar
cursor1=conexion1.cursor()                                                          #Crea el "cursor" que se usa para ingresar comandos de MySQL
cursor1.execute("SELECT id, fruta, HSV FROM Calibraciones WHERE fruta='Fruta3'")    #Petición a MySQL para tomar los valores de los registros de la tabla que cumplen los requisitos
DatosID=cursor1.fetchall()                                                          #Los registros tomados se almacenana en una variable de python
print(DatosID)                                                                      #Visualizamos los datos que tiene la variable 

conexion1.close()                                                                   #cerramos la conexión a la base de datos
