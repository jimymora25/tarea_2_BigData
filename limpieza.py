import pandas as pd
import os

# Ruta de los archivos
input_file = "breweries_data_erroneous.csv"  # Archivo con errores
output_file = "breweries_data_cleaned.csv"   # Archivo limpio
audit_file = "audit_log.txt"                 # Archivo de auditoría

# Cargar datos
try:
    df = pd.read_csv(input_file)

    # Inicializar archivo de auditoría
    audit_log = []
    audit_log.append(f"Archivo original cargado: {input_file}")
    audit_log.append(f"Número de registros iniciales: {len(df)}")

    # Eliminar duplicados
    records_before = len(df)
    df = df.drop_duplicates()
    records_after = len(df)
    audit_log.append(f"Duplicados eliminados: {records_before - records_after}")

    # Manejar valores nulos
    nulls_before = df.isnull().sum().sum()
    df = df.fillna({
        "city": "Unknown",
        "brewery_type": "Unknown",
        "state": "Unknown",
        "longitude": 0.0,
        "latitude": 0.0
    })
    nulls_after = df.isnull().sum().sum()
    audit_log.append(f"Valores nulos antes: {nulls_before}, después: {nulls_after}")

    # Corregir tipos de datos
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce").fillna(0.0)
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce").fillna(0.0)
    audit_log.append("Errores en tipos de datos corregidos para 'longitude' y 'latitude'.")

    # Normalizar estados (ejemplo: "CA" y "California")
    df["state"] = df["state"].replace({"CA": "California", "INVALID": "Unknown"})
    audit_log.append("Estados normalizados en la columna 'state'.")

    # Guardar los datos limpios en un nuevo archivo
    df.to_csv(output_file, index=False)
    audit_log.append(f"Archivo limpio guardado: {output_file}")

    # Crear archivo de auditoría
    with open(audit_file, "w") as f:
        f.write("\n".join(audit_log))
    print(f"Proceso completado. Archivos generados:\n- {output_file}\n- {audit_file}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {input_file}. Genera los datos primero.")
except Exception as e:
    print(f"Error durante el preprocesamiento: {e}")
