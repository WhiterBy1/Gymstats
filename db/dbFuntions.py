import csv
import os
import pandas as pd
from validation.validaciones import (
    validar_cadena_no_vacia,
    validar_rango,
    validar_usuario,
    validar_ejercicio,
)

# Función para calcular un nuevo ID basado en los existentes
def calcular_id(table: list):
    return max([int(row["id"]) for row in table], default=0) + 1


# Función para escribir en un archivo CSV
def escribir_csv(filename, data):
    fieldnames = data[0].keys() if data else []
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if fieldnames:
            writer.writeheader()
            writer.writerows(data)


# Función para leer un archivo CSV
def leer_csv(filename) -> list:
    if not os.path.exists(filename):
        return []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)


#Funcion para incertar en la base de datos
def incentar_db(filename, columns:list[str], values:list, IdNeeded:bool=False):
    table = leer_csv(filename)
    new_id = calcular_id(table)
    row = {'id': new_id}
    for column, value in zip(columns, values):
        row[column] = value
    table.append(row)
    escribir_csv(filename, table)
    if IdNeeded:
        return new_id

#Vizualizacion de  columnas usando dataframes
def obtener_columnas(filename, columns: list[str]):
    df = pd.read_csv(filename, encoding="latin1")
    dfinfo = df[columns]
    print("\n\n", dfinfo, "\n\n")
