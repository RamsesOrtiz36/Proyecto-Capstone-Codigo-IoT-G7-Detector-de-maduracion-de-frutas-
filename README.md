# Proyecto-Capstone-Codigo-IoT-G7-Maduración de frutas-
Repositorio del proyecto Capstone del diplomado de Codigo IoT generación 7 equipo "Maduración de frutas"

En base a los objetivos de desarrollo sostenible de la ONU nos enfocamos a ver los probelmas que tiene el país de México, resaltando la desnutrición, gran parte del territorio nacional presenta una mala alimentación.
La forma en que abordamos el problema es incrementar la accesibilidad de frutas y verduras, para ello ocupamos un dispositivo que detecte el grado de madures de estos productos de forma objetiva.
## Integrantes del equipo:
* Ramsés Ortiz Castro
* Erica Saavedra Riveros
* Ojeda Aguilar Jose Omar
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

## Justificación:
En la actualidad se genera mucho desperdicio a nivel mundial de alimentos per cápita en la venta al por menor y a nivel de los consumidores según en el punto 12.3 de Objetivo de Desarrollo Sostenible, el cual se pretende reducir las pérdidas de alimentos en las cadenas de producción y distribución.    
Hoy en día en puntos de compra-venta de alimentos como mercados, centros comerciales, centrales de abastos, donde existe merma de frutas y verduras los cuales su destino final es el vertedero municipal.
La presente investigación es viable, pues se realizará un prototipo el cual, por medio de diferentes sensores, se detectará la fruta en diferentes etapas de madurez, que indiquen el momento necesario para vender la mercancía a menor precio y cuando se tendrá que donar a instituciones sin fines de lucro para evitar la pérdida total del producto.
En el aspecto social beneficiará a las comunidades a tener acceso a la alimentación a precios justos y las instituciones sin fines de lucro, obtendrán un ingreso en especie. Y aunado a ello se minimizará la merma generada en los puntos de compra venta y por ende minimizarán los residuos diarios que se llevan a los rellenos sanitaros municipales.
Esta investigación tiene una utilidad metodológica, ya que con ello se tiene una vertiente para futuras investigaciones, actualizaciones, modificaciones o implementaciones en cualquier área geográfica.
En el aspecto disciplinario el estudio pretende contribuir a nivel nacional y mundial, ya que en cualquier metrópoli que se puede reducir la merma generada de frutas para que exista un mejor aprovechamiento del mismo.


## División del proyecto en partes
Se propone ver el proyecto en partes funcionales y determinar que funciones rrealiza cada una.
* Dispositivo.
* Base de datos.
* Procesamiento de datos.
### Funciones del dispositivo
En el dispositivo cumplira funciones de entrada y salida, donde los sensores son entradas y una pantalla será la salida
* Detectar temperatura y humedad del ambiente
* Detectar temperatura del producto
* Detectar concentración de CO2 del espacio cercano al producto
* Detectar el color del producto
* Detectar la firmeza del producto.

Para darle información al usuario se ocupa una pantalla y un medio para introducir información directamente del usuario
* Mostrar lista de nombres de productos para que el usuario lo seleccione.
* Agregar calibración por el usuario.
* Enviar datos a base de datos
* Mostrar información del producto al usuario
  * Grado de madures del producto
  * Tiempo de vida (calendario o grafica de Gantt)
  * Señal para donación
  * Información de valor agregado (recetas de cocina con el conjunto de productos)

### Función de la base de datos
* Guardar los valores de los sensores enviados por el dispositivo
* Entregar datos al sistema de procesamiento de datos

### Procesamiento de datos
* Tomar datos de referencia de la base de datos según el producto
* Tomar datos de sensores guardados en base de datos según el producto

* Comparar conjunto de datos de sensores contra conjunto de valores de referencia para el producto especifico.
* Determinar grado de madures del producto.
* Determinar tiempo de vida útil 
* Determinar fecha para donación de producto 
* Enviar resultados
xx