#si genera problemas con las importaciones ejecutar: set PYTHONPATH=%CD%
import os
from validation.const import PLANIFICATIONS_FILE
from db.db import inicializar_archivos
from app.mainFuntions import AgregarContenido, AgregarPlanificacion, VisualizarPlanificaciones


# Función principal
def main():
    if not os.path.exists(PLANIFICATIONS_FILE):
        inicializar_archivos()
    
    while True:
        print("Seleccione una opción:")
        print("1. Agregar Planificación")
        print("2. Agregar Contenido a una Planificación")
        print("3. Visualizar Planificaciones")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            AgregarPlanificacion()
        elif opcion == "2":
            planification_id = input("Ingrese el ID de la planificación: ")
            AgregarContenido(planification_id)
        elif opcion == "3":
            VisualizarPlanificaciones()
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")


# Ejecutar el programa
if __name__ == "__main__":
    main()
