@echo off
setlocal enabledelayedexpansion
cls
if "%~1"=="1" (
    goto :execute1
)
if "%~2"=="1" (
    set "selection=1" && goto :execute1
)
if "%~2"=="2" (
    set "selection=2" && goto :execute1
)
:selection
echo vMix Helper instalation.
echo ------------------------
echo 1. Install vmix-helper.
echo 2. Force install/reinstall vmix-helper.
echo 3. Uninstall vmix-helper.
echo 4. Exit.

set /p "sele=Please select Number:"

if "!sele!"=="1" set "selection=1" && cls && goto execute1
if "!sele!"=="2" set "selection=2" && cls && goto execute1
if "!sele!"=="3" cls && goto uninstall
if "!sele!"=="4" exit 0

cls
echo.
echo "Invalid choice! Please enter a number between 1 and 4."
echo.
goto selection

:execute1
where pip >nul 2>nul
if !errorlevel! equ 0 (
    set "pip_cmd=pip"
    goto :execute2
)

:execute2
if defined pip_cmd (
    echo Installing vmix_helper...
	for %%f in ("dist\vmix_helper-*.whl") do (
		set "WHEEL_PATH=%%f"
	)
	if not defined WHEEL_PATH (
		echo Can't find dist\vmix_helper-*.whl file
		pause
		exit 1
	)
	taskkill /IM "pythonw.exe" /F >nul 2>nul
	if !selection! equ 1 (
		echo !pip_cmd! install !WHEEL_PATH!
		!pip_cmd! install !WHEEL_PATH!
	) else (
		echo !pip_cmd! install --force-reinstall !WHEEL_PATH!
		!pip_cmd! install --force-reinstall !WHEEL_PATH!
	)
	if !errorlevel! equ 0 (
		powershell -Command "$wsh = New-Object -ComObject WScript.Shell; $s = $wsh.CreateShortcut('%USERPROFILE%\Desktop\vmix-helper.lnk'); $s.TargetPath = 'vmix-helper.exe'; $s.Save()"
		start %USERPROFILE%\Desktop\vmix-helper.lnk
		cls
		echo vmix-helper is now running, you will find it in the system tray section.
		echo ------------------------------------------------------------------------
	)
	pause
	exit 1
) else (
    echo Python not found we will try to install it.
	powershell -NoProfile -ExecutionPolicy Bypass -Command ^"^
		try{^
			$process = Start-Process powershell -Verb RunAs -Wait -PassThru -ArgumentList '-NoExit -NoProfile -Command \^"^
				try {^
					Get-Command winget -ErrorAction Stop;^
					winget settings --enable BypassCertificatePinningForMicrosoftStore;^
					Add-AppxPackage -Path ''https://cdn.winget.microsoft.com/cache/source.msix'';^
					winget install python3 --location ''C:\python3'' --scope machine --accept-source-agreements --accept-package-agreements --override ''/passive InstallAllUsers=1 DefaultAllUsersTargetDir=C:\\python3 CompileAll=1 PrependPath=1'';^
					if ^($LASTEXITCODE -eq 0^) {^
						winget install -e --id ''Microsoft.VCRedist.2015+.x64'' --scope machine --accept-source-agreements --accept-package-agreements;^
						exit 0;^
					}^
					pause;^
					exit 1;^
				} catch {^
					$retryCount = 0;^
					Write-Host ''Winget not found. trying to install it...'' -ForegroundColor Yellow;^
					while ^($retryCount -lt 2^) {^
						try {^
							Install-PackageProvider -Name NuGet -Force;^
							Install-Module -Name Microsoft.WinGet.Client -Force -Repository PSGallery;^
							try {^
								Repair-WinGetPackageManager -Force -AllUsers;^
							} catch {}^
							Get-Command winget -ErrorAction Stop;^
							winget settings --enable BypassCertificatePinningForMicrosoftStore;^
							Add-AppxPackage -Path ''https://cdn.winget.microsoft.com/cache/source.msix'';^
							Write-Host ''Winget installed successfully. trying to install python now...'' -ForegroundColor Yellow;^
							winget install python3 --location ''C:\python3'' --scope machine --accept-source-agreements --accept-package-agreements --override ''/passive InstallAllUsers=1 DefaultAllUsersTargetDir=C:\\python3 CompileAll=1 PrependPath=1'';^
							if ^($LASTEXITCODE -eq 0^) {^
								winget install -e --id ''Microsoft.VCRedist.2015+.x64'' --scope machine --accept-source-agreements --accept-package-agreements;^
								exit 0;^
							}^
							pause;^
							exit 1;^
						} catch {^
							$retryCount++;^
							Write-Host ''An error occurred: '' $_.Exception.Message -ForegroundColor Red;^
							Write-Host ''Trying Again.'' -ForegroundColor Green;^
						}^
					}^
					pause;^
					exit 1;^
				}\^"' -ErrorAction Stop;^
			if ^($process.ExitCode -ne 0^) {^
				Write-Host ''An error occurred: '' $_.Exception.Message -ForegroundColor Red;^
				pause;^
				exit 1;^
			}^
			exit 0;^
		}catch{^
			Write-Host ''An error occurred: '' $_.Exception.Message -ForegroundColor Red;^
			pause;^
			exit 1;^
		}"
	if !errorlevel! equ 0 (
		for /f "tokens=*" %%i in ('powershell -command "[Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')"') do set "PATH=%%i"
		timeout /t 1 /nobreak >nul
		start "" "%0" 1 !sele!
		exit 0
	)
	pause
	exit 1
)

:uninstall
del "%USERPROFILE%\Desktop\vmix-helper.lnk"
del "%USERPROFILE%\vmix-helper.conf"
del "%USERPROFILE%\vmix-helper.set"
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\vmix-helper.lnk"
taskkill /IM "pythonw.exe" /F
pip uninstall vmix_helper -y
cls
echo vmix-helper removed successfully
pause
exit 0
endlocal