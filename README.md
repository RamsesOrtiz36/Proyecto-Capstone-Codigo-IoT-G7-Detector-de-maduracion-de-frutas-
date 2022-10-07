# Proyecto-Capstone-Codigo-IoT-G7-Maduración de frutas-
Repositorio del proyecto Capstone del diplomado de Codigo IoT generación 7 equipo "Maduración de frutas". 

## Integrantes:
* Erica Saavedra
*
* **Ramsés Ortiz** 

## Introducción.
En base a los objetivos de desarrollo sostenible de la ONU nos enfocamos a ver los probelmas que tiene el país de México, resaltando la desnutrición, gran parte del territorio nacional presenta una mala alimentación.

La forma en que abordamos el problema es incrementar la accesibilidad de frutas y verduras, para ello proponemos un dispositivo que detecte el grado de madures de estos productos de forma objetiva, ayudando a la gestion de los productos al comerciante, dandole información del periodo de vida util, grado de maduración, fechas para donación.

En base al objetivo de [**Hambre Cero de la PNUD**](https://www.undp.org/es/sustainable-development-goals#hambre-cero) "Para 2030, duplicar la productividad agrícola y los ingresos de los pequeños productores de alimentos, en particular de las mujeres, los pueblos indígenas, los agricultores familiares, los pastores y los pescadores, incluso mediante un acceso seguro e igualitario a la tierra, otros recursos e insumos productivos, conocimientos y servicios financieros. mercados y oportunidades de valor añadido y empleo no agrícola."

Y de forma directa el aportar en cumplir el [objetivo 12 de la PNUD PRODUCCIÓN Y CONSUMO RESPONSABLES](https://www.undp.org/es/sustainable-development-goals#produccion-consumo-responsables) "De aquí a 2030, reducir a la mitad el desperdicio de alimentos per capita mundial en la venta al por menor y a nivel de los consumidores y reducir las pérdidas de alimentos en las cadenas de producción y suministro, incluidas las pérdidas posteriores a la cosecha."

## Dispositivo
Debera detectar varios indicadores de madures de la mayoria de los productos, asociando un conjunto de valores de referencia a cada tipo de profucto.
Los indicadores de madures son:
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
