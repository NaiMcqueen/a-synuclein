@echo off
set configFile=D:\Naidocking\8FPT_C1_config.txt
set ligandDir=D:\Naidocking\ligands\
set outputDir=D:\Naidocking\c1_output\

if not exist "%outputDir%" mkdir "%outputDir%"

for %%f in ("%ligandDir%*.pdbqt") do (
    set "ligand=%%f"
    set "ligandName=%%~nf"
    "D:\Instalaciones\The Scripps Research Institute\Vina\vina.exe" --config "%configFile%" --ligand "%%f" --out "%outputDir%%%~nf_out.pdbqt"
    echo Docking completado para: %%~nf
)

echo Todos los dockings han sido completados.
pause