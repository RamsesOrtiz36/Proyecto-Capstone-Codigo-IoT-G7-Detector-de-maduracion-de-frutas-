//
//Matriz de sensores de gases
//Elaborado por: Equipo IoT
//SENSOR---------MEDICIÓN
//MQ-2----------(GLP y Butano)
//MQ-3----------(Alcohol)
//MQ-4----------(Metano)
//MQ-7----------(Monóxido de carbono)
//MQ-135--------(Dióxido de carbono)



const int mq2 = A5;
const int mq3 = A4;
const int mq4 = A3;
const int mq7 = A2;
const int mq135 = A1;


void setup() {
 Serial.begin(9600);                 
}


void loop() {  
   Serial.begin(9600);                 
digitalWrite(8, HIGH);    
 
delay(1000); 
float prom_mq2 = 0;
float prom_mq3 = 0;
float prom_mq4 = 0;
float prom_mq7 = 0;
float prom_mq135 = 0;

//*****MQ2****//
for ( int i = 0 ; i < 100 ; i++ ){
prom_mq2 += analogRead(mq2);
//delay(10);
}
prom_mq2 = prom_mq2 / 100;
//Serial.print("{");
//Serial.print("\\\"mq2\\\":""\\\"""");
//Serial.print(prom_mq2);
//Serial.print("\\\""",");
 Serial.print("{\"mq2\":");
 Serial.print(prom_mq2);
 Serial.print(",");
//*****MQ3****//
for ( int i = 0 ; i < 100 ; i++ ){
prom_mq3 += analogRead(mq3);
//delay(10);
}
prom_mq3 = prom_mq3 / 100;
//Serial.print("\\\"mq3\\\":""\\\"""");
//Serial.print(prom_mq3);
//Serial.print("\\\""",");
 Serial.print("\"mq3\":");
 Serial.print(prom_mq3);
 Serial.print(",");
//*****MQ4****//

for ( int i = 0 ; i < 100 ; i++ ){
prom_mq4 += analogRead(mq4);
//delay(10);
}
prom_mq4 = prom_mq4 / 100;
//Serial.print("\\\"mq4\\\":""\\\"""");
//Serial.print(prom_mq4);
//Serial.print("\\\""",");
 Serial.print("\"mq4\":");
 Serial.print(prom_mq4);
 Serial.print(",");
//*****MQ7****//
for ( int i = 0 ; i < 100 ; i++ ){
prom_mq7 += analogRead(mq7);
//delay(10)
;}
prom_mq7 = prom_mq7 / 100;
//Serial.print("\\\"mq7\\\":""\\\"""");
//Serial.print(prom_mq7);
//Serial.print("\\\""",");
 Serial.print("\"mq7\":");
 Serial.print(prom_mq7);
 Serial.print(",");
//*****MQ135****//
for ( int i = 0 ; i < 100 ; i++ ){
prom_mq135 += analogRead(mq135);
//delay(10);
}
prom_mq135 = prom_mq135 / 100;
//Serial.print("\\\"mq135\\\":""\\\"""");
//Serial.print(prom_mq135);
//Serial.println("\\");
 Serial.print("\"mq135\":");
 Serial.print(prom_mq135);
Serial.println("}");

Serial.end();
digitalWrite(8, LOW);   
delay(10000);

}
