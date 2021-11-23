# Homicidios en Colombia
### Proyecto para Igenieria de Datos_Manejo de Base de Datos

_Para este proyecto se utilizaron fuentes reales, datos con licencia abierta del gobierno [www.datos.gov.co]. A partir de estos datos se realizaron varios modelos para la estrucuta de nuestra base de datos, se realizo el Modelo Entidad Relacion y su Modelo Relacional, despues usando Python se realizo la coneccion a PostgreSQL para el manejo de los datos desde la libreria DASH y asi presentar graficas que llevaron a distintos analisis presentados en el documento en PDF dentro de este repositorio._

## Ver y Usar el repositorio 🚀

_Ahora se explicara la forma de obtener una copia del proyecto y correrlo en su maquina local y usarlo para su proposito._

### Pre-requisitos

_Utilizamos 2 herramientas principalmente Python 🐍 y PostgreSQL 🐘 (esta puede cambiar a gusto suyo) por tanto explicaremos lo necesario para que esto funcione para usted con estas dos herramientas._

🐍 Instalacion de [Python](https://www.python.org/downloads/)

🐘 *Instalacion de [PostgreSQL](https://www.postgresql.org/download/)

❗ (En caso de querer clonar repositorio) Instalacion de [Git](https://git-scm.com/downloads)


_siga las instrucciones de las documentaciones oficiales_

### Instalacíon 💾

_Para clonar o duplicar un repositorio y obtener todos los archivos presentes existen varias maneras, explicaremos una de ellas y la mas basica._


1) ProyectoIGDB>Code>Download ZIP
2) Abrir la Carpeta en la que lo hallas descargado, en caso de no tener windows 11 es necesario tener una herramienta para descomprimir archivos (Una alternativa de codigo abierto es [7-zip](https://www.7-zip.org/download.html). Es posible que se demore este proceso por la cantidad de datos en las DB tiempo_aproximado: 7 minutos.
3) Abra la carpeta en su Editor de Codigo Favorito
4) Correr archivo de python (proyecto.py) / Activar entorno virtual

_Si corre **proyecto.py** y le genera algun tipo de error puede ser porque no se le activo el entorno virtual (En cada de tener error en el codigo baje hasta  "Usando los archivos"), ya que al correr el archivo le podria salir un menu en la terminal con las siguientes opciones:_

[N] No ejecutar  [Z] Ejecutar una vez  [U] Suspender  
[?] Ayuda(el valor predeterminado es "N"):

_Si le sale el menu ejecute el entorno virtual dando "Z" + Enter (tecla) en la terminal, En caso contrario de que le salga algun error del entorno virtual activelo manualmente (En una terminal dentro de la carpeta del proyecto):_

```
cd env
.\activate
```

_En el momento que halla completado la descarga y abierto la carpeta, es posible que le genere problemas con las librerias no-instaladas en este caso para la instalacion manual de las librerias siga los siguientes pasos:_

instalacion de libreria **psycopg2**
```
pip install psycopg2
```
instalacion de libreria **dash**
```
pip install dash
```
instalacion de libreria **pandas**
```
pip install pandas
```
## Usando los archivos 🖇️

_Al usar una Base de datos en un local host lo mas probable es que no compartamos datos identicos en la conexion de postgreSQL, por tanto es importante hacer lo siguiente._

_Despues de instalar su herramienta de SQL (En nuestro caso PostgreSQL) tendremos que crear una base de datos desde la herramienta PgAdmin o desde SQL shell en ambos casos deberia crearse y verse de la siguiente manera (de manera manual) :_

```
CREATE DATABASE your_name_data_base
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
```
_Despues de eso toca insertar los datos de la base de datos a nuestra propia base de datos, para ello es necesario abrir la carpeta de nombre SQL desde el editor de texto, en ella se encuentran dos archivos y otra carpeta de nombre database, estos archivos son .sql es decir que importandolos o copiandolos en la herramienta de postgreSQL bastaria para realizar la importacion de datos._

:bangbang: 
_Pero antes de ejecutar recuerde cambiar el directorio de la base de datos a su directorio, como lo puede ver en los comentarios de los archivos DDL y DML, luego ejecutelos en ese orden._
:bangbang: 

_Por ultimo tienen que entrar al archivo Connection.py seguir sus instrucciones que basicamente es ubicar los datos SUYOS de la base de datos user, password, database, host y port._

## Autores ✒️

* 🍔 **Johan Caro** - *Implementacion grafica en DASH, Entregas y Documentos, estructura de modelos relacionales, implementacion de datos, implementaciones finales* [Yucaloid](https://github.com/Yucaloid)
* 🌷 **Juanita Robles** - *Implementacion grafica en DASH, proceso de diseño y estructuras, modelos relacionales* [juanis07](https://github.com/juanis07)
* 🍀 **Andrés Yañez** - *Busqueda e implementacion de datos, Conexiones Python, PostgreSQL y Git, Code Tester, modelos relacionaes* [TheChieft](https://github.com/TheChieft)

## Expresiones de Gratitud 🎁

_El grupo conformado por Johan Caro, Juanita Robles y Andres Yañez agradecemos publicamenta a nuestra profesora de la materia Ingenieria de Datos 🤓, Tambien cada uno esta agrecido entre nosotros por el trabajo realizado y cumplir con todo lo plasmado al inicio del proyecto 😊._





