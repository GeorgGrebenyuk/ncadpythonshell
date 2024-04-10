#Получаем путь, откуда запускается скрипт
$current_directory =  split-path -parent $MyInvocation.MyCommand.Definition
$nano_220_dir = "C:\Users\" + $Env:username + "\AppData\Roaming\Nanosoft\nanoCAD x64 22.0\Config"
$nano_230_dir = "C:\Users\" + $Env:username + "\AppData\Roaming\Nanosoft\nanoCAD x64 23.0\Config"
$nano_231_dir = "C:\Users\" + $Env:username + "\AppData\Roaming\Nanosoft\nanoCAD x64 23.1\Config"
$nano_235_dir = "C:\Users\" + $Env:username + "\AppData\Roaming\Nanosoft\nanoCAD x64 23.5\Config"
#Наши проверяемые значения - файл адаптации и загружаемая dll
$NPS_cfg_name = "NcPythonShell.cfg"
$NPS_cfg_path = "#include " + $current_directory + "\" + $NPS_cfg_name
$NPS_dll_name = "CADPythonShell.dll"
$NPS_dll_path = $current_directory + "\" + $NPS_dll_name

Write-Host "Current directory = " $current_directory
Write-Host "NPS_cfg_path = " $NPS_cfg_path
Write-Host "NPS_dll_path = " $NPS_dll_path

#Редактируем CFG файл nanoCAD для добавления нашей библиотеки
#editing_mode = 0: меняем nano_***_cfg; =1: меняем файл автозагрузки
function Edit_Nano_CFG {
    param (
    [parameter(Mandatory=$true, Position=0)][string]$nano_config_dir,
    [parameter(Mandatory=$true, Position=1)][int]$editing_mode)

    $nano_config_path = ""
    $temp_NetModules_exists = 0
    $temp_NetModules_adding = 0
    if ($editing_mode -eq 0){ $nano_config_path = $nano_config_dir + "\nanoCAD.cfg"}
    elseif ($editing_mode -eq 1){ $nano_config_path = $nano_config_dir + "\nApp.ini"}
    Write-Host "Param path = " $nano_config_path

    $nano_config_stringbuilder = [System.Text.StringBuilder]::new()
    #Если файл существует, то считываем в память его содержимое за минусом нужной строки
    if ([System.IO.File]::Exists($nano_config_path))
    {
        Write-Host "exist"
        
        foreach ($config_line in [System.IO.File]::ReadLines($nano_config_path))
        {
            #Write-Host $config_line
            if (($editing_mode -eq 0) -and (!$config_line.Contains($NPS_cfg_name))) {[void]$nano_config_stringbuilder.AppendLine($config_line)}
            elseif (($editing_mode -eq 1) -and (!$config_line.Contains($NPS_dll_name))) 
            {
                
                if (($temp_NetModules_exists -eq 0) -and ($config_line.Contains('[\NetModules]')))
                {
                    $temp_NetModules_exists = 1
                    [void]$nano_config_stringbuilder.AppendLine($config_line)
                }
                elseif (($temp_NetModules_exists -eq 1) -and ($config_line.Contains('[')))
                {
                    #Добавляем нашу .NET dll
                    $temp_NetModules_adding = 1
                    [void]$nano_config_stringbuilder.AppendLine($NPS_dll_path)
                    [void]$nano_config_stringbuilder.AppendLine($config_line)
                }
                else{[void]$nano_config_stringbuilder.AppendLine($config_line)}
            }

        }
    }
    #Если файл не существует (в основном, для nApp.ini), то создаем его с новой информацией
    #Вне зависимости от того, была ли эта надстройка же загружена, добавляем её адаптацию (или файл dll) в загрузку
        if ($editing_mode -eq 0) {[void]$nano_config_stringbuilder.AppendLine($NPS_cfg_path)}
        elseif (($editing_mode -eq 1)) 
        {

            if (($temp_NetModules_exists -eq 0) -and ($temp_NetModules_adding -eq 0))
            {
                [void]$nano_config_stringbuilder.AppendLine('[\NetModules]')
                [void]$nano_config_stringbuilder.AppendLine($NPS_dll_path)
            }
            elseif (($temp_NetModules_exists -eq 1) -and ($temp_NetModules_adding -eq 0))
            {
                [void]$nano_config_stringbuilder.AppendLine($NPS_dll_path)
            }
        }
        
        #Записываем изменения в файл
        [System.IO.File]::WriteAllText($nano_config_path, $nano_config_stringbuilder.ToString())
}

#Edit_Nano_CFG $nano_220_dir 1
#Edit_Nano_CFG $nano_220_dir 0


Edit_Nano_CFG $nano_230_dir 1
Edit_Nano_CFG $nano_230_dir 0

Edit_Nano_CFG $nano_231_dir 1
Edit_Nano_CFG $nano_231_dir 0

Edit_Nano_CFG $nano_235_dir 1
Edit_Nano_CFG $nano_235_dir 0


#TODO доделать авто-проверку какая версия по версии hostmgd.dll копируемой
Write-Host "End!"
