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



def incentar_db(filename, columns: list[str], values: list, IdNeeded: bool = False):
    # Leer datos existentes
    table = leer_csv(filename)
    new_id = calcular_id(table)

    # Validaciones antes de insertar
    for column, value in zip(columns, values):
        validar_cadena_no_vacia(value, column)  # Validar que no esté vacío
        if column == "rpe":  # Validar rango para el RPE
            validar_rango(int(value), 1, 10, "RPE")
        elif column == "user_id":  # Validar que el usuario exista
            if not validar_usuario(int(value)):
                raise ValueError(f"El usuario con ID {value} no existe.")
        elif column == "exercise_id":  # Validar que el ejercicio exista
            if not validar_ejercicio(int(value)):
                raise ValueError(f"El ejercicio con ID {value} no existe.")

    # Crear nueva fila e insertar
    row = {'id': new_id}
    for column, value in zip(columns, values):
        row[column] = value
    table.append(row)
    escribir_csv(filename, table)

    if IdNeeded:
        return new_id


def obtener_columnas(filename, columns: list[str]):
    df = pd.read_csv(filename, encoding="latin1")
    dfinfo = df[columns]
    print("\n\n", dfinfo, "\n\n")
