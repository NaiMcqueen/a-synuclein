@echo off
setlocal enabledelayedexpansion

set "configDir=C:\Users\naiar\Naidocking\configs\"
set "ligandDir=C:\Users\naiar\Naidocking\ligands\"
set "baseOutputDir=C:\Users\naiar\Naidocking\outputs\"

if not exist "%baseOutputDir%" mkdir "%baseOutputDir%"

for %%c in (%configDir%*_config.txt) do (
    set "configFile=%%c"
    set "configName=%%~nc"
    echo Procesando configuracion: !configName!

    set "outputDir=!baseOutputDir!!configName!"
    if not exist "!outputDir!" mkdir "!outputDir!"

    for %%f in (%ligandDir%*.pdbqt) do (
        set "ligand=%%f"
        set "ligandName=%%~nf"
        echo Ejecutando docking: !ligandName! con config !configName!
        "C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe" --config "%%c" --ligand "%%f" --out "!outputDir!\!ligandName!_out.pdbqt"
        echo Docking completado para: !ligandName! con configuracion !configName!
    )
)

echo Todos los dockings han sido completados.
pause