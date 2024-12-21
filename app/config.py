import os
import sys
#configuracion
current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)  # Inserta el directorio actual al inicio de sys.path
print(f"PYTHONPATH configurado a: {current_dir}")

print("\n\nScript principal ejecutándose...\n\n")