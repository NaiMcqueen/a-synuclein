@echo off
setlocal enabledelayedexpansion

set configDir=C:\Users\naiar\Naidocking\automatizacion\configs\
set ligandDir=C:\Users\naiar\Naidocking\automatizacion\ligands\
set baseOutputDir=C:\Users\naiar\Naidocking\Uniformero\outputs\

if not exist "%baseOutputDir%" mkdir "%baseOutputDir%"

for %%c in ("%configDir%*_config.txt") do (
    set "configFile=%%c"
    set "configName=%%~nc"

     rem Extraer parte antes de "_config"
    for /f "tokens=1 delims=_" %%a in ("%%~nc") do (
        set "prefix=%%a"
    )

    rem Restaurar parte adicional si el nombre tiene más guiones bajos antes de _config
    set "fullPrefix=!configName:_config=!"

    echo Procesando configuracion: !configName!

    set "outputDir=%baseOutputDir%!configName!\"
    if not exist "!outputDir!" mkdir "!outputDir!"


    for %%f in ("%ligandDir%*.pdbqt") do (
        set "ligand=%%f"
        set "ligandName=%%~nf"
        "C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe" --config "%%c" --ligand "%%f" --out "!outputDir!!fullPrefix!_!ligandName!_out.pdbqt"
        echo Docking completado para: !ligandName! con configuracion !configName!
    )
)

echo Todos los dockings han sido completados.
pause