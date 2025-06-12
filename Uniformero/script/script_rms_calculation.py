from pymol import cmd
import sys
import os

ligand_file = sys.argv[1]  # recibe como argumento el archivo PDBQT
ligand_name = os.path.splitext(os.path.basename(ligand_file))[0].replace('_out', '')  # quita .pdbqt y _out

# Carga con nombre controlado para que split_states funcione bien
cmd.load(ligand_file, ligand_name)

# Divide conformaciones en objetos separados
cmd.split_states(ligand_name)

# Selecciona todos los objetos que empiezan con ligand_name
ligands = [obj for obj in cmd.get_names("objects") if obj.startswith(ligand_name)]

# Calcular RMS entre todos los pares
output_lines = []
for i in range(len(ligands)):
    for j in range(i+1, len(ligands)):
        rms = cmd.rms_cur(ligands[i], ligands[j])
        output_lines.append(f"{ligands[i]} vs {ligands[j]}: {rms:.4f}")

# Obtener carpeta donde está el archivo ligand_file
ligand_dir = os.path.dirname(os.path.abspath(ligand_file))

# Crear subcarpeta 'rms_results' dentro de esa carpeta
output_dir = os.path.join(ligand_dir, "rms_results")
os.makedirs(output_dir, exist_ok=True)

# Guardar archivo de resultados ahí
output_file = os.path.join(output_dir, f"{ligand_name}_rms_results.txt")
with open(output_file, "w") as f:
    f.write("\n".join(output_lines))

print(f"Resultados guardados en {output_file}")
