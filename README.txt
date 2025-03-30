README.
FUNCIONAMIENTO DEL CODIGO.

1. El archivo Script_Brewery.ipynb que es parte de la actividad 1 hace la ingesta desde la API en la
actividad entregada en la tarea 1 y genera los archivos brewery.db, breweries_data.xlsx, breweries_data.csv 
y el archivo auditoria.txt que documenta los registros de la ingesta como ejemplo tenemos: 
Cantidad de registros en el DataFrame original: 50
Cantidad de registros en la base de datos SQLite: 50
No hay diferencias en los datos.

2. El archivo Script_Brewery_errores.ipynb es con el que se trabaja en el preprocesamiento de datos 
para lo cual se le genera a la base de datos contaminacion de sus datos y poder hacer la limpieza con 
el codigo del archivo limpieza.py.

3. Una vez ejecutados estos codigos encontramos en formato .csv los archivos errones y en el mismo formato
los archivos que han sido limpiados durante el proceso de limpieza.

4. El archivo audit_log.txt muestra la auditoria de los procedimientos de los puntos anteriores.
.......

Tarea_3 Marzo 30 de 2025.

actividad enriquecimiento de datos de varias fuentes. 
1. Con el dataset obtenido en la tarea 2 con datos limpios llamado breweries_data_cleaned.csv se inicia su
enriquecimiento con datos provenientes de otras fuentes con otros formatos.
2. Se crea un archivo llamado integracion_datos.py el cual contiene el paso a paso para extraer la información de las diversas fuentes en nuestro ejemplo XML, xlsx y .json.
3. Se genera el código para mostrar los reportes que documenten los cambios. En nuestro caso el dataset base fue enriquecido con 15 nuevas columnas manteniéndose la cantidad de filas ya que las fuentes que nosotros utilizamos como ejemplo solo contenían un menor numero de filas. 
4. la consolidación de estas fuentes se hace en un archivo de salida llamado dataset_enriquecido.csv.
5. Se agrega al proyecto en githug donde se actualiza el workflow y se documenta su funcionalidad con el check correcto de ejecución.
Con este código  aprendimos integración de datos de diversas fuentes.....