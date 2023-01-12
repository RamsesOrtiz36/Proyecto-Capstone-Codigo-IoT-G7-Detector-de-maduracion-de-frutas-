#include <esp32cam.h>//esp32cam.h

#define pressButton 12
#define led_FLASH 4
bool Boton_flash = false;

const char* WIFI_SSID = "INFINITUM1885_2.4";
const char* WIFI_PASS = "7pxYYmS6EP";
 


void  setup(){ 
 pinMode(pressButton,INPUT);                           //Declara el puerto para colocar el push button 
  pinMode(led_FLASH,OUTPUT);                            //Declara el puerto para usar el Flash de la ESP32CAM
  
}
void loop()
{
  while (digitalRead(pressButton)==HIGH ){
      delay (100);
      if (digitalRead(pressButton)==HIGH ){
        if(Boton_flash==false){
          Boton_flash==true;               
          } 
        else{
          Boton_flash==false;
          }
      }   
  } 
if (Boton_flash==false){
  digitalWrite(led_FLASH,LOW);
  }
else {
  digitalWrite(led_FLASH,HIGH);
  }  
}
