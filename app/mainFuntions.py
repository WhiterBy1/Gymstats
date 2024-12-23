# Función para agregar una nueva planificación
import json
from validation.const import PLANIFICATION_CONTENT_FILE, PLANIFICATIONS_FILE
from db.dbFuntions import leer_csv, incentar_db, obtener_columnas
from validation.validaciones import validar_ejercicio, validar_usuario, permitir_entre


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
    Planification_id = incentar_db(PLANIFICATIONS_FILE, ["date","user_id", "status", "routine_name"], [date, user_id, False, routine_name],IdNeeded=True)
    
    print("¡Planificación agregada exitosamente!\n")

    # Preguntar si desea agregar contenido a la planificación
    opcion = input("¿Desea agregar contenido a esta planificación? (s/n): ").lower()
    if opcion == 's':
        AgregarContenido(str(Planification_id))

# Función para agregar contenido a una planificación
def AgregarContenido(planification_id):
    print("\n--- Agregar Contenido a la Planificación ---")

    while True:
        exercise_id = input("Ingrese el ID del ejercicio (0 para salir): ")
        if exercise_id == "0":
            break

        if not validar_ejercicio(exercise_id):
            print("El ID del ejercicio no existe. Inténtelo de nuevo.")
            continue

        set_detail = construir_set_detail()
        incentar_db(PLANIFICATION_CONTENT_FILE, ["planification_id","exercice_id", "set_detail"], [planification_id, exercise_id, set_detail])
        
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

# Función para visualizar las planificaciones del usuario actual
def VisualizarPlanificaciones():
    obtener_columnas(PLANIFICATIONS_FILE, ["routine_name", "status", "date"])