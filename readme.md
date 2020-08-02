# Proyecto Soap Computación Paralela y Distribuida
Proyecto SOAP para la asignatura computación paralela y distribuida en la UTEM, semestre 1 2020; docente: Sebastián Salazar.
 El proyecto consiste en utilizar el protocolo SOAP para pasar información entre cliente y servidor, esto consiste en que el cliente selecciona el nombre de un archivo .csv con los campos necesarios, el programa cliente procesa este archivo y lo envía al servidor por medio del protocolo SOAP, el servidor parsea los datos enviados y construye un archivo excel el cual será enviado como información al cliente, luego el cliente recibe este archivo.

El entorno de este problema consiste en que el servidor deberá clasificar a los postulantes en las distintas carreras de la UTEM, estos postulantes buscan quedar en su mejor opción y en la mejor carrera. Luego el programa crea un excel el cual tiene las carreras ordenadas por prioridad y los postulantes de mayor a menor puntaje en cada una de estas.
#### Autores
· Daniel Aguilera T.

· Nicolás Andrews S.

## Dependencias y compilación
Se requiere una versión de python mayor a 3.7.3, preferible la última. Y las librerías `zeep` para el cliente y `spyne` y `xlsxwriter`para el servidor.

**Cliente:**
```
pip install zeep
```
**Servidor** 
```
pip install spyne
pip install xlsxwriter
```
#### Correr el programa:
El cliente debe usar el archivo `cliente.py` desde la terminal.
`$ python3 cliente.py`

El servidor debe correr el archivo `server.py` desde la terminal. 
`$ python3 server.py`

Nota: por diseño, el servidor creará un archivo .xlsx, el cual una vez terminada la operación no se elminará en ningún momento. En el caso de el programa intentar escribir el .xlsx con el mismo nombre que algún otro, este será sobreescrito.

###  Información adicional:
El programa del servidor contiene la definición del servidor y su punto de entrada por la función de RPC, sin embargo el funcionamiento del servidor corresponde a leer los datos de entrada (las carreras universitarias), esta información siempre está en la memoria del programa.
Sobre el archivo .xml: La entrada del servidor es un archivo xml con 2 campos (nombre y data) el primero se ocupa para crear el archivo `nombre.xlsx` y la data es un campo de información en base64 que el programa decodifica para operar. La salida del servidor es solo el ultimo campo que responde con la información del archivo excel en base64.
