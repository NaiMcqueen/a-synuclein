import os
import subprocess

print("Script uniformero.py iniciado")

output_folder = "outputs"
script_path = "script/script_rms_calculation.py"
pymol_exe = r"C:\ProgramData\pymol\Scripts\pymol.exe"

print("Buscando archivos en: " + output_folder)

try:
    files = os.listdir(output_folder)
    print("Archivos encontrados: " + str(files))
except Exception as e:
    print("Error al leer la carpeta de salida: " + str(e))
    exit(1)

for file in files:
    if file.endswith("_out.pdbqt"):
        print("Analizando archivo: " + file)
        full_path = os.path.join(output_folder, file)

        process = subprocess.Popen(
            [pymol_exe, "-cq", script_path, "--", full_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        if stdout:
            print(stdout.decode("utf-8"))

        if stderr:
            print("Error en " + file + ":\n" + stderr.decode("utf-8"))

print("Fin del script")
