#include <DHT.h>  // Incluimos librería
 
#define DHTPIN 2  // Definimos el pin digital donde se conecta el sensor
// Dependiendo del tipo de sensor
#define DHTTYPE DHT11
 
DHT dht(DHTPIN, DHTTYPE); // Inicializamos el sensor DHT11
 
void setup() {
  
  Serial.begin(9600); // Comunicación con monitor serie
 
  dht.begin();  // Comenzamos comunicación del sensor DHT11
 
}
 
void loop() {
  delay(3000); // Esperamos 3 segundos entre medidas
 
  // Leer la humedad relativa
  float h = dht.readHumidity();
  // Leer la temperatura en grados centígrados
  float t = dht.readTemperature();
 
  // Comprobamos si ha habido algún error en la lectura
  if (isnan(h) || isnan(t) ) {
    Serial.println("Error obteniendo los datos del sensor DHT11");
    return;
  }
  //Mostramos valores en pantalla
  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.println(" °C ");

 
}
//Fin
