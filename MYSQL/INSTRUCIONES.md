# Instrucciones para configurar la base de datos

## Instrucciones para intalar MySQL
  1. actualizar los paquetes del sistema antes de instalar MySQL
  - `sudo apt update` 
  2. instalacion de MySQL
- `sudo apt install mysql-server` 

## pasos para relaizar Base de Datos en MySQL
1. Entrar a mysql
    - `sudo mysql`
2. Crear una nueva base de datos
    - `CREATE DATABASE Detector-de-maduracion-de-frutas;`
3. Seleccionar base de datos
    - `use Detector-de-maduracion-de-frutas;`
4. Crear una tabla llamada registro que contenga todos los campos necesarios.
CREATE TABLE registro (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP, fruta CHAR (248) NOT NULL, temp FLOAT(4,2) NOT NULL, hum INT(1) UNSIGNED NOT NULL, GLP y Butano FLOAT(4,2) UNSIGNED NOT NULL, Alcohol FLOAT(4,2) UNSIGNED NOT NULL, Metano FLOAT(4,2) UNSIGNED NOT NULL, Monóxido de Carbono FLOAT(4,2) UNSIGNED NOT NULL, Dióxido de Carbono FLOAT(4,2) UNSIGNED NOT NULL;

 temporales:

    - id
    - nombre de la fruta
    - fecha
    - temperatura
    - humedad
    - gases que emite (lista de gases para cada gas una columna, pueden ser los que se tiene en el codigo de arduino que hizo Erica) (nuemrico)
    - (¿Se puede guardar imagen como tipo de dato? en caso de ser que sí, entonces guardariamos la foto de la fruta de ese momento jpeg o png)
    - estado de maduración (numerico del 1 al 4 o texto)
    - días en estado para un buen consumo (variable tipo fecha)
