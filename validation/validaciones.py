# Función para validar si un usuario existe
from validation.const import EXERCISES_FILE, USERS_FILE
from db.dbFuntions import leer_csv


def validar_usuario(user_id):
    users = leer_csv(USERS_FILE)
    return any(int(user["id"]) == int(user_id) for user in users)


# Función para validar si un ejercicio existe
def validar_ejercicio(exercise_id):
    exercises = leer_csv(EXERCISES_FILE)
    return any(int(ex["id"]) == int(exercise_id) for ex in exercises)

def permitir_entre():
    pass