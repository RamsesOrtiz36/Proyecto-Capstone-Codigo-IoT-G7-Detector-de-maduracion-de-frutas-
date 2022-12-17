import numpy as np
import cv2

def nada(x):
    pass
cv2.namedWindow('Parametros')
cv2.createTrackbar('Tonalidad Minima','Parametros',0,179,nada)
cv2.createTrackbar('Tonalidad Maxima','Parametros',0,179,nada)

cv2.createTrackbar('Pureza Minima','Parametros',0,255,nada)
cv2.createTrackbar('Pureza Maxima','Parametros',0,255,nada)

cv2.createTrackbar('Luminosida Minima','Parametros',0,255,nada)
cv2.createTrackbar('Luminosida Maxima','Parametros',0,255,nada)

cv2.createTrackbar('Kernel X','Parametros',1,30,nada)
cv2.createTrackbar('Kernel Y','Parametros',1,30,nada)

#crear Video
cap=cv2.VideoCapture(0)

while (1): #capturar imagen de la camara
    ret, frame =cap.read()      #verifica que la imagen se capturo correctamente
    if ret :
        hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)         #Cnvertir imagen BGR a HSV

        #leer sliders

        Tmin=cv2.getTrackbarPos('Tonalidad Minima','Parametros')
        Tmax=cv2.getTrackbarPos('Tonalidad Maxima','Parametros')

        Pmin=cv2.getTrackbarPos('Pureza Minima','Parametros')
        Pmax=cv2.getTrackbarPos('Pureza Maxima','Parametros')

        Lmin=cv2.getTrackbarPos('Luminosida Minima','Parametros')
        Lmax=cv2.getTrackbarPos('Luminosida Maxima','Parametros')

        kernelx = cv2.getTrackbarPos('Kernel X','Parametros')
        kernely = cv2.getTrackbarPos('Kernel Y','Parametros')

            #establecer rangos maximos y minimos del filtro HSV
        color_oscuro= np.array((Tmin,Pmin,Lmin))
        color_brillante=np.array((Tmax,Pmax,Lmax))
            #detecta pixxeles dentro del rango del filtro HSV
        mascara = cv2.inRange(hsv,color_oscuro,color_brillante)
            #crear kernel para eliminar ruido
        kernel= np.ones((kernelx,kernely),np.uint8)
        mascara =cv2.morphologyEx(mascara,cv2.MORPH_CLOSE,kernel)
        mascara =cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel)
            #dibujar el rectangulo de donde esta el color
            #RETR_LIST Calcula los contornos guardadolos sin jerarquia
            #APPROX_SIMPLE es el metodo de aproxximación de contorno, elimina pixeles redundantes
        contornos, _ = cv2.findContours(mascara,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame,contornos,-1,(0,0,0),2)
            #mostrar la imagen de la camara y de la mascara
        cv2.imshow("Camara",frame)
        cv2.imshow("Mascara",mascara)
            #Al presionar la tecla ESC se cierra todo
        k=cv2.waitKay(5)
        if k == 27:
            cv2.destroyAllWindows()
            break
cap.release()












