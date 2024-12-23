import os
from validation.const import PLANIFICATIONS_FILE
from db.db import inicializar_archivos
from app.views.planification import AgregarContenido, AgregarPlanificacion, VisualizarPlanificaciones

#funcion para crear menus
def crear_menu(opciones:list[str], funciones:list ):
    
    while True:
        print("---------------------")
        print("Seleccione una opción:")
        for x, e in enumerate(opciones):
            print(f"{x+1}. {e}")
        print(f"{len(opciones)+1}. Salir\n---------------------")
        opcion = input("Opción: ")
        
        if opcion.isdigit() and 0 < int(opcion) < len(opciones)+1:
            funciones[int(opcion)-1]()
        elif opcion == str(len(opciones)+1):
            print("Adiós!")
            break
        else:
            print("\nOpción inválida, intente nuevamente.\n")

def gestion_planificaciones_menu():
    
    crear_menu(["Agregar Planificación",
                "Agregar Contenido a una Planificación",
                "Visualizar Planificaciones",
                ],
                [
                    AgregarPlanificacion,
                    AgregarContenido,
                    VisualizarPlanificaciones,
                ])



def mainmenu():
    if not os.path.exists(PLANIFICATIONS_FILE):
        inicializar_archivos()
    crear_menu(["Gestion de planificaciones",
                "Gestion de entrenamientos",
                "Data Analytics"
                ],
                [
                    gestion_planificaciones_menu,
                    #gestion_entrenamientos_menu,
                    #data_analytics_menu
                ])