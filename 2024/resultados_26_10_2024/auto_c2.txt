@echo off
setlocal enabledelayedexpansion
set configFile=C:\Users\naiar\Naidocking\8FPT_C2_config.txt
set ligandDir=C:\Users\naiar\Naidocking\ligands\
set outputDir=C:\Users\naiar\Naidocking\c2_output\

if not exist "%outputDir%" mkdir "%outputDir%"

for %%f in ("%ligandDir%*.pdbqt") do (
    set "ligand=%%f"
    set "ligandName=%%~nf"
    "C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe" --config "%configFile%" --ligand "%%f" --out "%outputDir%%%~nf_out.pdbqt"
    echo Docking completado para: !ligandName!
)

echo Todos los dockings han sido completados.
pause