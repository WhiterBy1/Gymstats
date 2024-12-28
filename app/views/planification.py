import json
from validation.const import PLANIFICATION_CONTENT_FILE, PLANIFICATIONS_FILE
from db.dbFuntions import incentar_db, obtener_columnas
from validation.validaciones import (
    validar_ejercicio,
    validar_usuario,
    validar_formato_fecha,
    validar_entero,
    validar_cadena_no_vacia,
    validar_rango,
    validar_si_no
)

# Función para solicitar entrada con validación y reintentos
def solicitar_entrada(prompt, validacion, mensaje_error):
    while True:
        try:
            valor = input(prompt)
            if validacion(valor, mensaje_error):
                return valor
        except Exception as e:
            print(f"Error inesperado: {e}")
        print("Por favor, intente nuevamente.\n")

# Función para agregar planificaciones
def AgregarPlanificacion():
    print("\n--- Agregar Nueva Planificación ---")

    # Validar fecha
    date = solicitar_entrada(
        "Ingrese la fecha de la planificación (YYYY-MM-DD): ",
        lambda x, _: validar_formato_fecha(x, "Error en la fecha"),
        "La fecha no es válida."
    )

    # Validar usuario
    user_id = solicitar_entrada(
        "Ingrese el ID del usuario: ",
        lambda x, _: validar_usuario(x),
        "El ID de usuario no existe."
    )

    # Validar nombre de rutina
    routine_name = solicitar_entrada(
        "Ingrese el nombre de la rutina: ",
        lambda x, _: validar_cadena_no_vacia(x, "Error en el nombre de rutina"),
        "El nombre de la rutina no puede estar vacío."
    )

    incentar_db(
        PLANIFICATIONS_FILE,
        ["date", "user_id", "status", "routine_name"],
        [date, user_id, False, routine_name]
    )
    print("¡Planificación agregada exitosamente!\n")

    # Preguntar si desea agregar contenido
    opcion = solicitar_entrada(
        "¿Desea agregar contenido a esta planificación? (s/n): ",
        lambda x, _: validar_si_no(x, "Error en la respuesta"),
        "Debe ingresar 's' para sí o 'n' para no."
    )

    if opcion.lower() == 's':
        AgregarContenido()

# Función para agregar contenido a una planificación
def AgregarContenido():
    planification_id = solicitar_entrada(
        "Ingrese el ID de la planificación: ",
        lambda x, _: validar_entero(x, "Error en el ID de planificación"),
        "El ID de la planificación debe ser un número entero."
    )

    print("\n--- Agregar Contenido a la Planificación ---")
    while True:
        exercise_id = solicitar_entrada(
            "Ingrese el ID del ejercicio (0 para salir): ",
            lambda x, _: x == "0" or validar_ejercicio(x),
            "El ID del ejercicio no existe."
        )

        if exercise_id == "0":
            break

        set_detail = construir_set_detail()
        incentar_db(
            PLANIFICATION_CONTENT_FILE,
            ["planification_id", "exercise_id", "set_detail"],
            [planification_id, exercise_id, set_detail]
        )
        print("¡Contenido agregado exitosamente!\n")

# Función para construir un set_detail (JSON) detallado
def construir_set_detail():
    series = int(solicitar_entrada(
        "Ingrese la cantidad de series: ",
        lambda x, _: validar_entero(x, "Error en la cantidad de series"),
        "El número de series debe ser un entero válido."
    ))

    contenido = []
    for i in range(1, series + 1):
        print(f"\n--- Serie {i} ---")

        peso_plan = float(solicitar_entrada(
            "Ingrese el peso planificado (kg): ",
            lambda x, _: validar_rango(x, 0, 1000, "Error en el peso planificado"),
            "El peso debe ser un valor numérico entre 0 y 1000."
        ))

        repeticiones = int(solicitar_entrada(
            "Ingrese el número de repeticiones: ",
            lambda x, _: validar_entero(x, "Error en las repeticiones"),
            "El número de repeticiones debe ser un entero válido."
        ))

        rpe = int(solicitar_entrada(
            "Ingrese el RPE (1-10): ",
            lambda x, _: validar_rango(x, 1, 10, "Error en el RPE"),
            "El RPE debe estar entre 1 y 10."
        ))

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
    input("Presiona enter para dejar de ver...\n")
