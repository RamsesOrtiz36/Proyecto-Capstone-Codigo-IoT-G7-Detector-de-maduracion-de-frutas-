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

 temporales:

    - id
    - nombre de la fruta
    - fecha
    - temperatura
    - gases que emite
    - estado de maduración
    - días en estado para un buen consumo
