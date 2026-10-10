@echo off
set SCRIPT_DIR=%~dp0
set PYTHON=python

if "%~1"=="" (
    echo ==========================================
    echo  Crawl One Story tu sachiepvien.net
    echo ==========================================
    echo.
    echo Cach dung: %~nx0 ^<story_url^> [slug] [--local]
    echo.
    pause
    exit /b 1
)

echo.
echo === Dang xu ly: %~1 ===
echo.

"%PYTHON%" "%SCRIPT_DIR%crawler\crawl_one.py" %*

if %ERRORLEVEL%==0 (
    echo.
    echo === THANH CONG! ===
) else (
    echo.
    echo === THAT BAI ===
)

echo.
pause
exit /b %ERRORLEVEL%