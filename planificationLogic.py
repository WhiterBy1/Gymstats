import csv
import os
import json

# Carpeta para almacenar los archivos CSV
DB_FOLDER = "dB_temp"

# Rutas de los archivos CSV
USERS_FILE = os.path.join(DB_FOLDER, "users.csv")
PLANIFICATIONS_FILE = os.path.join(DB_FOLDER, "planifications.csv")
PLANIFICATION_CONTENT_FILE = os.path.join(DB_FOLDER, "planification_content.csv")
EXERCISES_FILE = os.path.join(DB_FOLDER, "exercises.csv")

# Función para inicializar archivos CSV con datos iniciales
def inicializar_archivos():
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    users = [
        {"id": 1, "user": "user1", "password": "password1"},
        {"id": 2, "user": "user2", "password": "password2"},
        {"id": 3, "user": "user3", "password": "password3"}
    ]

    planifications = []
    planification_content = []
    exercises = [
        {"id": 1, "name": "Push-up", "category": "Strength"},
        {"id": 2, "name": "Running", "category": "Cardio"},
        {"id": 3, "name": "Squat", "category": "Strength"}
    ]

    escribir_csv(USERS_FILE, users)
    escribir_csv(PLANIFICATIONS_FILE, planifications)
    escribir_csv(PLANIFICATION_CONTENT_FILE, planification_content)
    escribir_csv(EXERCISES_FILE, exercises)

# Función para escribir en un archivo CSV
def escribir_csv(filename, data):
    fieldnames = data[0].keys() if data else []
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if fieldnames:
            writer.writeheader()
            writer.writerows(data)

# Función para leer un archivo CSV
def leer_csv(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Función para construir un set_detail (JSON) detallado
def construir_set_detail():
    series = int(input("Ingrese la cantidad de series: "))
    contenido = []

    for i in range(1, series + 1):
        print(f"\n--- Serie {i} ---")
        peso_plan = float(input("Ingrese el peso planificado (kg): "))
        repeticiones = int(input("Ingrese el número de repeticiones: "))
        rpe = int(input("Ingrese el RPE (1-10): "))

        contenido.append({
            "numero": i,
            "peso_plan": peso_plan,
            "repeticiones": repeticiones,
            "rpe": rpe
        })

    return json.dumps({"series": series, "contenido": contenido})

# Función para obtener o crear un ejercicio
def obtener_o_crear_ejercicio():
    exercises = leer_csv(EXERCISES_FILE)
    exercise_name = input("Ingrese el nombre del ejercicio: ").strip()

    # Buscar el ejercicio por nombre
    for exercise in exercises:
        if exercise["name"].lower() == exercise_name.lower():
            print(f"Ejercicio encontrado: {exercise['name']} (ID: {exercise['id']})")
            return exercise["id"]

    # Si no se encuentra, crear uno nuevo
    new_id = max([int(ex["id"]) for ex in exercises], default=0) + 1
    category = input("Ingrese la categoría del ejercicio (por ejemplo, Pecho, Cuadriceps): ").strip()

    new_exercise = {"id": new_id, "name": exercise_name, "category": category}
    exercises.append(new_exercise)
    escribir_csv(EXERCISES_FILE, exercises)

    print(f"Nuevo ejercicio agregado: {exercise_name} (ID: {new_id})")
    return new_id

# Función para agregar contenido a una planificación
def AgregarContenido(planification_id):
    print("\n--- Agregar Contenido a la Planificación ---")
    planification_content = leer_csv(PLANIFICATION_CONTENT_FILE)

    while True:
        exercise_id = obtener_o_crear_ejercicio()
        set_detail = construir_set_detail()

        new_id = max([int(row["id"]) for row in planification_content], default=0) + 1
        planification_content.append({
            "id": new_id,
            "planification_id": planification_id,
            "exercice_id": exercise_id,
            "set_detail": set_detail
        })

        escribir_csv(PLANIFICATION_CONTENT_FILE, planification_content)
        print("¡Contenido agregado exitosamente!\n")

        continuar = input("¿Desea agregar otro ejercicio? (s/n): ").lower()
        if continuar != 's':
            break

# Función para agregar una nueva planificación
def AgregarPlanificacion():
    print("\n--- Agregar Nueva Planificación ---")
    date = input("Ingrese la fecha de la planificación (YYYY-MM-DD): ")
    user_id = input("Ingrese el ID del usuario: ")

    # Validar si el usuario existe
    users = leer_csv(USERS_FILE)
    if not any(user["id"] == user_id for user in users):
        print("El ID de usuario no existe. Inténtelo de nuevo.\n")
        return

    routine_name = input("Ingrese el nombre de la rutina: ")
    planifications = leer_csv(PLANIFICATIONS_FILE)

    # Calcular el nuevo ID
    new_id = max([int(row["id"]) for row in planifications], default=0) + 1

    planifications.append({
        "id": new_id,
        "date": date,
        "user_id": user_id,
        "status": False,
        "routine_name": routine_name
    })

    escribir_csv(PLANIFICATIONS_FILE, planifications)
    print("¡Planificación agregada exitosamente!\n")

    # Preguntar si desea agregar contenido a la planificación
    opcion = input("¿Desea agregar contenido a esta planificación? (s/n): ").lower()
    if opcion == 's':
        AgregarContenido(str(new_id))

# Función principal
def main():
    if not os.path.exists(PLANIFICATIONS_FILE):
        inicializar_archivos()

    while True:
        print("Seleccione una opción:")
        print("1. Agregar Planificación")
        print("2. Agregar Contenido a una Planificación")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            AgregarPlanificacion()
        elif opcion == "2":
            planification_id = input("Ingrese el ID de la planificación: ")
            AgregarContenido(planification_id)
        elif opcion == "3":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()
