import os
from pymol import cmd

# Ruta base del proyecto
base_dir = r"C:\Users\naiar\Naidocking\automatizacion"  # <--- CAMBIAR ESTA RUTA
outputs_dir = os.path.join(base_dir, "uniformero", "outputs")

# Recorremos cada carpeta *_config
for folder in os.listdir(outputs_dir):
    if folder.endswith("_config"):
        estructura = folder.replace("_config", "")
        estructura_path = os.path.join(base_dir, estructura + "_prot.pdbqt")
        config_path = os.path.join(outputs_dir, folder)
        rms_path = os.path.join(config_path, "rms_results", "delete.txt")

        print("Procesando estructura:", estructura)

        # Cargar estructura proteica
        if os.path.exists(estructura_path):
            cmd.load(estructura_path, estructura + "_prot")
        else:
            print("Archivo de proteina no encontrado:", estructura_path)
            continue

        # Cargar ligandos y hacer split
        for fname in os.listdir(config_path):
            if fname.endswith("_out.pdbqt"):
                ligand_path = os.path.join(config_path, fname)
                cmd.load(ligand_path)

        for obj in cmd.get_names("all"):
            if obj.endswith("_out"):
                cmd.split_states(obj)

        # Ejecutar comandos de delete.txt
        if os.path.exists(rms_path):
            with open(rms_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("delete"):
                        try:
                            cmd.do(line)
                        except:
                            print("Error ejecutando:", line)
        else:
            print("delete.txt no encontrado en:", rms_path)

        # Crear carpeta 'interacciones' dentro del config
        interacciones_dir = os.path.join(config_path, "interacciones")
        if not os.path.exists(interacciones_dir):
            os.makedirs(interacciones_dir)

        output_file = os.path.join(interacciones_dir, estructura + "_residuos.txt")

        # Guardar interacciones
        with open(output_file, "w") as out:
            ligandos = cmd.get_names("objects", enabled_only=1)
            ligandos = [lig for lig in ligandos if "_lig_" in lig and lig.endswith("_out")]
            for ligando in ligandos:
                cmd.select("lig", ligando)
                cmd.select("interacciones", "lig around 4 and polymer")
                model = cmd.get_model("interacciones")

                out.write("Ligando: %s\n" % ligando)
                out.write("Aminoácidos que interactúan:\n")
                residuos_vistos = set()

                for atom in model.atom:
                    res_id = atom.chain + "/" + atom.resn + atom.resi
                    if res_id not in residuos_vistos:
                        out.write(res_id + "\n")
                        residuos_vistos.add(res_id)

                out.write("\n")
                cmd.delete("lig")
                cmd.delete("interacciones")

        print("Residuos guardados en:", output_file)

        # Limpiar para la siguiente estructura
        cmd.reinitialize()




