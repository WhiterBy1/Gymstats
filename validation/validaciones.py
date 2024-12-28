from validation.const import EXERCISES_FILE, USERS_FILE
from db.dbFuntions import leer_csv
import re

# Validar si un usuario existe
def validar_usuario(user_id):
    users = leer_csv(USERS_FILE)
    return any(int(user["id"]) == int(user_id) for user in users)


# Validar si un ejercicio existe
def validar_ejercicio(exercise_id):
    exercises = leer_csv(EXERCISES_FILE)
    return any(int(ex["id"]) == int(exercise_id) for ex in exercises)


# Validar si un valor está dentro de un rango numérico
def validar_rango(valor, minimo, maximo, mensaje_error):
    try:
        valor = float(valor)
    except ValueError:
        print(f"{mensaje_error}: El valor debe ser numérico.")
        return False
    if minimo <= valor <= maximo:
        return True
    print(f"{mensaje_error}: El valor debe estar entre {minimo} y {maximo}.")
    return False


# Validar entradas enteras
def validar_entero(valor:str, mensaje_error):
    if not valor.isdigit():
        print(f"{mensaje_error}: El valor debe ser un número entero.")
        return False
    return True


# Validar si una cadena no está vacía
def validar_cadena_no_vacia(cadena, mensaje_error):
    if not cadena.strip():
        print(f"{mensaje_error}: El valor no puede estar vacío.")
        return False
    return True


# Validar sí/no
def validar_si_no(respuesta:str, mensaje_error):
    if respuesta.lower() not in ["s", "n"]:
        print(f"{mensaje_error}: Debe ingresar 's' para sí o 'n' para no.")
        return False
    return True


# Validar el formato de fecha (YYYY-MM-DD)
def validar_formato_fecha(fecha, mensaje_error):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):
        print(f"{mensaje_error}: Debe ingresar una fecha en el formato YYYY-MM-DD.")
        return False
    return True

