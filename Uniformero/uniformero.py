import os
import subprocess

print("Script uniformero.py arrancó")

output_folder = "outputs"
script_path = "scripts/script_rms_calculation.py"
pymol_exe = r"C:\ProgramData\pymol\Scripts\pymol.exe"

print(f"Buscando archivos en: {output_folder}")

files = os.listdir(output_folder)
print(f"Archivos encontrados: {files}")

for file in files:
    if file.endswith("_out.pdbqt"):
        print(f"Analizando archivo: {file}")
        full_path = os.path.join(output_folder, file)
        result = subprocess.run([
            pymol_exe, "-cq", script_path, "--", full_path
        ], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Error en {file}: {result.stderr}")

print("Fin del script")