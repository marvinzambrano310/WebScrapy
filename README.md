# WebScrapy
La actividad se realizo usando el metodo de Beautiful Soup de tres diferentes paginas web:
- www.oxl.com.ec
- https://www.entrepreneur.com/topic/tecnologia
- https://www.elsevier.com/es-es/connect

La recopilacion de datos se dio en MongoDB Atlas usando la siguiente cadena de conexion:
- mongodb+srv://Marzam23:marzam23@dataanalysis.m9jnd.mongodb.net/test

Los datos obtenidos fueron similares pero de disferentes partes del codigo como el almacenamiento de:
- titulos
- enlaces
- imágenes
- y tamaño

Cada página envio distinta cantidad de datos:
 OLX: 7 registros
 Entrepreneur: 5 registros
 Elsevier: 10 registros
Un total de 22 registros por la ejecucion de los 3 codigos.

Los datos recopilados se muestran en el archivo Data.json
