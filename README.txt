README.


## Trazabilidad del Proceso

* **Ingesta de Datos:**
    * Se extraen datos de la API Open Brewery DB y se almacenan en una base de datos SQLite (`brewery.db`).
    * Se generan archivos CSV y Excel como muestras de los datos.
    * Se genera un archivo de auditoría para verificar la integridad de los datos.


* **Preprocesamiento de Datos:**
    * Se limpian y transforman los datos almacenados en SQLite.
    * Se eliminan duplicados, se manejan valores nulos y se corrigen tipos de datos.
    * Se genera un archivo CSV con los datos limpios.
    * Se genera un archivo de auditoría para documentar los cambios.


* **Enriquecimiento de Datos:**
    * Se integran datos de archivos XML, JSON y XLSX con los datos limpios.
    * Se genera un archivo CSV con los datos enriquecidos.
    * Se genera un reporte de enriquecimiento.

## Instrucciones de Ejecución

* **Clonación del Repositorio:**
    * `git clone https://github.com/jimymora25/tarea_2_BigData.git`
* **Instalacion Dependencias:**
    * `pip install requests pandas openpyxl jupyter lxml`
* **Ejecucion del Script de Enriquecimiento:**
    * `python Tarea_3/integracion_datos.py`

## Automatización con GitHub Actions

El flujo de trabajo automatizado mediante GitHub Actions realiza los siguientes pasos:

* **Checkout del código:**    Obtiene el código fuente del repositorio.
* **Configurar Python:**      Configura el entorno de Python 3.10.
* **Instalar dependencias:**  Instala las librerías necesarias.
* **Ejecutar `Script_Brewery.ipynb`:** Extrae y almacena datos de la API.
* **Ejecutar `Script_Brewery_errores.ipynb`:** Genera datos erróneos para pruebas.
* **Ejecutar `limpieza.py`:** Limpia los datos.
* **Instalar dependencias `lxml`:** Instala dependencias adicionales.
* **Ejecutar `integracion_datos.py`:** Enriquece los datos.



