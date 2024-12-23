import os
# Carpeta para almacenar los archivos CSV
# Define la carpeta de la base de datos relativa al archivo actual
DB_FOLDER = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "db")), "dB_temp")

# Rutas de los archivos CSV
USERS_FILE = os.path.join(DB_FOLDER, "users.csv")
PLANIFICATIONS_FILE = os.path.join(DB_FOLDER, "planifications.csv")
PLANIFICATION_CONTENT_FILE = os.path.join(DB_FOLDER, "planification_content.csv")
EXERCISES_FILE = os.path.join(DB_FOLDER, "exercises.csv")