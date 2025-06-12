import os
import subprocess

print("Script uniformero.py iniciado")

# Ruta base: donde está este script
base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Ruta absoluta a la carpeta 'outputs'
output_folder = r"C:\Users\naiar\Naidocking\automatizacion\uniformero\outputs"
script_path = r"C:\Users\naiar\Naidocking\automatizacion\uniformero\script\script_rms_calculation.py"
pymol_exe = r"C:\ProgramData\pymol\Scripts\pymol.exe"

print("Buscando archivos en subcarpetas de: " + output_folder)

try:
    config_folders = [f for f in os.listdir(output_folder)
                      if os.path.isdir(os.path.join(output_folder, f)) and f.endswith("_config")]

    if not config_folders:
        print("No se encontraron carpetas *_config dentro de outputs.")
        exit(1)

except Exception as e:
    print("Error al leer las carpetas de salida: " + str(e))
    exit(1)

for folder in config_folders:
    folder_path = os.path.join(output_folder, folder)
    print(f"\nEntrando en carpeta: {folder_path}")

    files = os.listdir(folder_path)
    for file in files:
        if file.endswith("_out.pdbqt"):
            print("Analizando archivo:", file)
            full_path = os.path.join(folder_path, file)

            process = subprocess.Popen(
                [pymol_exe, "-cq", script_path, "--", full_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()

            if stdout:
                print(stdout.decode("utf-8"))

            if stderr:
                print("Error en", file, ":\n" + stderr.decode("utf-8"))
        else:
            print("Ignorado:", file)

print("\nFin del script")
