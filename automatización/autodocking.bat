@echo off
setlocal enabledelayedexpansion

set "configDir=C:\Users\naiar\Naidocking\automatización\configs"
set "ligandDir=C:\Users\naiar\Naidocking\automatización\ligands"
set "baseOutputDir=C:\Users\naiar\Naidocking\automatización\outputs\"

if not exist "%baseOutputDir%" mkdir "%baseOutputDir%"

for %%c in (%configDir%*_config.txt) do (
    set "configFile=%%c"
    set "configName=%%~nc"
    
    rem extraer antes del "_config" del nombre del archivo
    for /f "tokens=1 delims=_config" %%a in ("!fullName!") do (
        set "configName=%%a"
    )
    echo Nombre base de la configuracion: !baseName!

    set "outputDir=!baseOutputDir!!configName!"
    if not exist "!outputDir!" mkdir "!outputDir!"

    for %%f in (%ligandDir%*.pdbqt) do (
        set "ligand=%%f"
        set "ligandName=%%~nf"
        echo Ejecutando docking: !ligandName! con config !configName!
        "C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe" --config "%%c" --ligand "%%f" --out "!outputDir!!configName!_ligandName!_out.pdbqt"
        echo Docking completado para: !ligandName! con configuracion !configName!
    )
)

echo Todos los dockings han sido completados.
pause