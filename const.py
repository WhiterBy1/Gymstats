import os
# Carpeta para almacenar los archivos CSV
DB_FOLDER = "dB_temp"

# Rutas de los archivos CSV
USERS_FILE = os.path.join(DB_FOLDER, "users.csv")
PLANIFICATIONS_FILE = os.path.join(DB_FOLDER, "planifications.csv")
PLANIFICATION_CONTENT_FILE = os.path.join(DB_FOLDER, "planification_content.csv")
EXERCISES_FILE = os.path.join(DB_FOLDER, "exercises.csv")