# Proyecto-Capstone-Codigo-IoT-G7-Maduración de frutas-
Repositorio del proyecto Capstone del diplomado de Codigo IoT generación 7 equipo "Maduración de frutas"

En base a los objetivos de desarrollo sostenible de la ONU nos enfocamos a ver los probelmas que tiene el país de México, resaltando la desnutrición, gran parte del territorio nacional presenta una mala alimentación.
La forma en que abordamos el problema es incrementar la accesibilidad de frutas y verduras, para ello ocupamos un dispositivo que detecte el grado de madures de estos productos de forma objetiva.
## Dispositivo
El dispositivo debera detectar varios indicadores de madures de la mayoria de los productos, asociando un conjunto de valores de referencia a cada tipo de profucto.
Los indicadores de madures que se encuentran son:
* Concentración de Gas **Etileno**
* **Temperatura** ambiente y del producto
* Concentración de gas **CO2**
* Porcentaje de **Humedad del aire** en el ambiente
* Firmeza del cuerpo del producto o **Textura** 
* **Color** de la superficie del producto.

### Sensores
Cada indicador puede tener mínimo un sensor que obtenga de forma cuantitativa un valor
* Para **Etileno** los sensores son caros por el proceso que se ocupa para detectar el gas, por lo que es posible no tener sensor para este indicador
* Para temperatura ambiente se puede usar "Aqui va nombre de un sensor" y para temperatura de producto e puede usar un arreglo de sensores de contacto y de IR.
* Para Gas **CO2** existe una gran familia de sensores de gas conocida como MQ, usada para muchos proyectos de sensado de gases
* Para la humedad del aire usaremos "DHT11" que se encuentra dentro del Kit del diplomado
* Para la detección de la **textura** se buscarán opciones 
* Para el color se podria usar la camara y mediante analisis de imagen detectar color y porcentaje de color en la superficie delimitada.  
