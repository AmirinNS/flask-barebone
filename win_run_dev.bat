@echo off

:: Make it possible to read immediate value of variable using !variable! syntax.
setlocal enabledelayedexpansion

:: Read file "settings.json" into variable data, removing line breaks.
set data=
for /f "delims=" %%x in (settings.json) do set "data=!data!%%x"

:: Remove whitespaces
set data=%data: =%
:: Remove quotes
set data=%data:"=%
:: Remove braces
set "data=%data:~1,-1%"
:: Change colon by to equal-sign
set "data=%data::==%"

for /f "tokens=1* delims=," %%a in ("%data%") do (
	set %%a
	set %%b
)

echo flask run --host=%host% --port=%port%
echo ====================================
echo Running Flask Development
echo ====================================
flask run --host=%host% --port=%port%

endlocal