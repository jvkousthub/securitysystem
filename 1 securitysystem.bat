@echo off

set "target=google.com"

ping %target% -n 1 >nul
if errorlevel 1 (
    echo Internet connection not available.
    echo Please connect to the internet and try again.
    pause
    exit
)

echo Installing module requirements...

python -c "import cv2"
if errorlevel 1 (
    echo Module 'opencv-python' is not installed. Installing...
    pip install opencv-contrib-python >nul
    pip install opencv-python >nul
) else (
    pip install opencv-contrib-python >nul
    echo Module 'opencv-python' is already installed.
	
)
echo Module (1/6) installed.
ping localhost -n 3 >nul
cls

python -c "import numpy"
if errorlevel 1 (
    echo Module 'numpy' is not installed. Installing...
    pip install numpy >nul
) else (
    echo Module 'numpy' is already installed.
)
echo Module (2/6) installed.
ping localhost -n 3 >nul
cls

python -c "import openpyxl"
if errorlevel 1 (
    echo Module 'openpyxl' is not installed. Installing...
    pip install openpyxl >nul
) else (
    echo Module 'openpyxl' is already installed.
)
echo Module (3/6) installed.
ping localhost -n 3 >nul
cls

python -c "import tkinter"
if errorlevel 1 (
    echo Module 'tkinter' is not installed. Installing...
    pip install tk >nul
) else (
    echo Module 'tkinter' is already installed.
)
echo Module (4/6) installed.
ping localhost -n 3 >nul
cls

python -c "import requests"
if errorlevel 1 (
    echo Module 'requests' is not installed. Installing...
    pip install requests >nul
) else (
    echo Module 'requests' is already installed.
)
echo Module (5/6) installed.
ping localhost -n 3 >nul
cls

python -c "import datetime"
if errorlevel 1 (
    echo Module 'datetime' is not installed. Installing...
    pip install datetime >nul
) else (
    echo Module 'datetime' is already installed.
)
echo Module (6/6) installed.
ping localhost -n 3 >nul
cls


python Window.py

exit
