import os
from dbFuntions import escribir_csv
from const import DB_FOLDER, EXERCISES_FILE, PLANIFICATION_CONTENT_FILE, PLANIFICATIONS_FILE, USERS_FILE 
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
