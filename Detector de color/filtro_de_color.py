import cv2
import urllib.request
import numpy as np                                                          #Bibliotecas 
 
def nothing(x):                                                             
    pass
 
url='http://192.168.1.70/cam-lo.jpg'                                            #Asigna la URL a la cual se conecta para capturar la imagen 
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)                   #Construye la ventana de visualización de la imagen captada de la url    
 
l_h, l_s, l_v = 92, 57, 50                                                  #Valores de parametros HSV minimos                
u_h, u_s, u_v = 142, 153, 178                                               #Valores de parametros HSV maximos
 
while True:                                                                 #mientras sea verdadero se ejecuta el codigo dentro        
    img_resp=urllib.request.urlopen(url)                                    #Abre la imagen de la URL            
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)               #contruye una imagen con formato unit8 desde la anterior
    frame=cv2.imdecode(imgnp,-1)                                            #construye la imagen "frame"             
    #_, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                            #convierte "frame" de BGR a HSV
 
    l_b = np.array([l_h, l_s, l_v])                                         #construye un array con los valores minimos de hsv
    u_b = np.array([u_h, u_s, u_v])                                         #construye un array con los valores maximos de hsv
    
    mask = cv2.inRange(hsv, l_b, u_b)                                       #construye la imagen mascara con los array minimos y maximos de hsv    
 
    cnts, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #Encuentra los contornos de las areas que cumplen con la mascara, devuelve dos cosas, los contornos y la jerarquia de contrnos
 
    for c in cnts:                                                          #cnt es un arrelo que contiene el contorno, para cada c en el arreglo
        area=cv2.contourArea(c)                                             #determina el area de caa contoruno
        if area>2000:                                                       #si el area es ayor a 2000 
            cv2.drawContours(frame,[c],-1,(255,0,0),3)                      #dibuja el contorno encontrados en frame con color y tamaño de linea 
            M=cv2.moments(c)                                                #calcula el centro del contorno
            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])
 
            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame,"blue",(cx-20, cy-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
        
    res = cv2.bitwise_and(frame, frame, mask=mask)                          #Aplica una comparación AND elemento a elemento de las matrices de imagen frame y mask
 
    cv2.imshow("live transmission", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key=cv2.waitKey(5)
    if key==ord('q'):
        break
    
 
cv2.destroyAllWindows()