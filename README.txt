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
