# Función para agregar una nueva planificación
import json
from const import PLANIFICATION_CONTENT_FILE, PLANIFICATIONS_FILE
from dbFuntions import escribir_csv, leer_csv
from planificationLogic import AgregarContenido, construir_set_detail
from validaciones import validar_ejercicio, validar_usuario

#Funcion para agregar planificaciones
def AgregarPlanificacion():
    print("\n--- Agregar Nueva Planificación ---")
    date = input("Ingrese la fecha de la planificación (YYYY-MM-DD): ")
    user_id = input("Ingrese el ID del usuario: ")

    # Validar si el usuario existe
    if not validar_usuario(user_id):
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

# Función para agregar contenido a una planificación
def AgregarContenido(planification_id):
    print("\n--- Agregar Contenido a la Planificación ---")
    planification_content = leer_csv(PLANIFICATION_CONTENT_FILE)

    while True:
        exercise_id = input("Ingrese el ID del ejercicio (0 para salir): ")
        if exercise_id == "0":
            break

        if not validar_ejercicio(exercise_id):
            print("El ID del ejercicio no existe. Inténtelo de nuevo.")
            continue

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
