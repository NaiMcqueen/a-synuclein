import os

base_dir = 'outputs'  # Ajusta si necesario

print('Iniciando script...')

for config_dir in os.listdir(base_dir):
    if not config_dir.endswith('_config'):
        continue

    rms_results_path = os.path.join(base_dir, config_dir, 'rms_results')
    if not os.path.isdir(rms_results_path):
        print('No se encontro la carpeta rms_results en: {}'.format(config_dir))
        continue

    print('Procesando carpeta: {}'.format(rms_results_path))
    extracted_texts = []

    for filename in os.listdir(rms_results_path):
        if filename.endswith('rms_results.txt'):
            file_path = os.path.join(rms_results_path, filename)
            print('  Leyendo archivo: {}'.format(filename))
            
            with open(file_path, 'r') as file:
                lines = file.readlines()

            for line in lines:
                try:
                    rms_value = float(line.split(':')[-1].strip())
                    if rms_value < 2:
                        if "and" in line and ":" in line: #Verificar que sea "and" y no "vs"
                            extracted_text = line.split("and")[1].split(":")[0].strip()
                            extracted_texts.append(extracted_text)
                except (ValueError, IndexError):
                    print('    Linea ignorada (malformada): {}'.format(line.strip()))
                    continue

    if extracted_texts:
        unique_texts = list(set(extracted_texts))
        delete_command = "delete " + " and ".join(unique_texts)

        delete_file_path = os.path.join(rms_results_path, 'delete.txt')
        with open(delete_file_path, 'w') as output_file:
            output_file.write(delete_command + '\n')

        print('Archivo delete.txt creado en: {}'.format(delete_file_path))
    else:
        print('No se encontraron RMS menores a 2 en: {}'.format(rms_results_path))
