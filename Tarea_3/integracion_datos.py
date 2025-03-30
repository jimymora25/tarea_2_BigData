import pandas as pd
import os
from lxml import etree
from datetime import datetime

# Leer el archivo fuente_adicional.xml
def leer_fuente_adicional_xml():
    ruta_xml = r"C:\Users\USUARIO\Downloads\tarea_2_BigData\Tarea_3\fuente_adicional.xml"
    if not os.path.exists(ruta_xml):
        print(f"❌ Error: El archivo no se encuentra en la ruta:\n{ruta_xml}")
        return None
    try:
        tree = etree.parse(ruta_xml)
        root = tree.getroot()
        rows = [{child.tag: child.text for child in cerveceria} for cerveceria in root.findall("cerveceria")]
        df_xml = pd.DataFrame(rows)
        print("✅ Información de la fuente XML:")
        print(df_xml.head())
        return df_xml
    except etree.XMLSyntaxError as e:
        print(f"❌ Error de sintaxis en el archivo XML: {e}")
        return None

# Leer el archivo fuente_adicional.json
def leer_fuente_adicional_json():
    ruta_json = r"C:\Users\USUARIO\Downloads\tarea_2_BigData\Tarea_3\fuente_adicional.json"
    if not os.path.exists(ruta_json):
        print(f"❌ Error: El archivo no se encuentra en la ruta:\n{ruta_json}")
        return None
    try:
        df_json = pd.read_json(ruta_json, lines=True, encoding='utf-8')
        print("✅ Información de la fuente JSON:")
        print(df_json.head())
        return df_json
    except ValueError as e:
        print(f"❌ Error al leer el archivo JSON: {e}")
        return None

# Leer el archivo fuente_adicional.xlsx
def leer_fuente_adicional_xlsx():
    ruta_xlsx = r"C:\Users\USUARIO\Downloads\tarea_2_BigData\Tarea_3\fuente_adicional.xlsx"
    if not os.path.exists(ruta_xlsx):
        print(f"❌ Error: El archivo no se encuentra en la ruta:\n{ruta_xlsx}")
        return None
    try:
        df_xlsx = pd.read_excel(ruta_xlsx)
        print("✅ Información de la fuente XLSX:")
        print(df_xlsx.head())
        return df_xlsx
    except ValueError as e:
        print(f"❌ Error al leer el archivo XLSX: {e}")
        return None

# Integrar datasets base y fuentes adicionales
def integrar_datasets(dataset_base, fuentes_adicionales):
    df_enriquecido = dataset_base.copy()
    for fuente, df_adicional in fuentes_adicionales.items():
        if df_adicional is None:
            print(f"⚠️ La fuente '{fuente}' no pudo ser cargada.")
            continue
        columna_merge = 'id'
        try:
            df_enriquecido['id'] = df_enriquecido['id'].astype(str)
            df_adicional['id'] = df_adicional['id'].astype(str)
            print(f"Nulos en df_{fuente}['id']: {df_adicional['id'].isnull().sum()}")
            print(f"Duplicados en df_{fuente}['id']: {df_adicional['id'].duplicated().sum()}")
            df_enriquecido = pd.merge(df_enriquecido, df_adicional, how="left", on=columna_merge, suffixes=("", f"_{fuente}"))
            print(f" Datos de la fuente '{fuente}' integrados correctamente.")
        except Exception as e:
            print(f"❌ Error durante la integración de '{fuente}': {e}")
    return df_enriquecido

# Generar el reporte de enriquecimiento
def generar_reporte_enriquecimiento(dataset_base, dataset_enriquecido, fuentes_usadas):
    ruta_reporte = r"C:\Users\USUARIO\Downloads\tarea_2_BigData\Tarea_3\enrichment_report.txt"
    with open(ruta_reporte, "w") as reporte:
        reporte.write("Reporte de Enriquecimiento de Datos\n")
        reporte.write(f"Fecha y Hora de la Integración: {datetime.now()}\n")
        reporte.write("=" * 50 + "\n")
        reporte.write(f"Cantidad de registros en el dataset base: {len(dataset_base)}\n")
        reporte.write(f"Cantidad de columnas en el dataset base: {len(dataset_base.columns)}\n")
        reporte.write(f"Cantidad de registros en el dataset enriquecido: {len(dataset_enriquecido)}\n")
        reporte.write(f"Cantidad de columnas en el dataset enriquecido: {len(dataset_enriquecido.columns)}\n")
        reporte.write("=" * 50 + "\n")
        reporte.write("Fuentes de Datos Utilizadas:\n")
        for fuente in fuentes_usadas:
            reporte.write(f"- {fuente}\n")
        reporte.write("=" * 50 + "\n")
        nuevas_columnas = set(dataset_enriquecido.columns) - set(dataset_base.columns)
        reporte.write("Resumen de la Integración:\n")
        reporte.write(f"Se han integrado {len(nuevas_columnas)} nuevas columnas.\n")
        reporte.write("=" * 50 + "\n")
    print(f" Reporte de enriquecimiento generado: {ruta_reporte}")

if __name__ == "__main__":
    ruta_base = r"C:\Users\USUARIO\Downloads\tarea_2_BigData\Tarea_3\breweries_data_cleaned.csv"
    if not os.path.exists(ruta_base):
        print(f"❌ No se encontró el archivo base en:\n{ruta_base}")
        exit()
    dataset_base = pd.read_csv(ruta_base)
    print(" Dataset base cargado con éxito.")
    fuente_xml = leer_fuente_adicional_xml()
    fuente_json = leer_fuente_adicional_json()
    fuente_xlsx = leer_fuente_adicional_xlsx()
    print("\n Datos de la fuente XML:")
    print(fuente_xml)
    print("\n Datos de la fuente JSON:")
    print(fuente_json)
    print("\n Datos de la fuente XLSX:")
    print(fuente_xlsx)
    fuentes_adicionales = {"XML": fuente_xml, "JSON": fuente_json, "XLSX": fuente_xlsx}
    df_enriquecido = integrar_datasets(dataset_base, fuentes_adicionales)
    print("\n Información consolidada en el DataFrame enriquecido:")
    print(df_enriquecido.head())
    ruta_salida = r"C:\Users\USUARIO\Downloads\tarea_2_BigData\Tarea_3\dataset_enriquecido.csv"
    df_enriquecido.to_csv(ruta_salida, index=False)
    print(f" Archivo enriquecido generado correctamente:\n{ruta_salida}")
    fuentes_usadas = list(fuentes_adicionales.keys())
    generar_reporte_enriquecimiento(dataset_base, df_enriquecido, fuentes_usadas)