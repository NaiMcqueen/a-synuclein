@echo off
REM Cambia al directorio donde están los scripts y archivos
cd /d C:\Users\Naiar\Naidocking\Uniformero

REM Ejecuta pymol con el script y el archivo de entrada
"C:\ProgramData\pymol\Scripts\pymol.exe" -cq scripts\rms_script.py -- outputs\tuarchivo_out.pdbqt
