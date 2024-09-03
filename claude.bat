@echo off
REM Navigate to the virtual environment directory
cd /d C:\Users\kevin\OneDrive\Documents\GitHub\Claude-Assistant\browser-launch

REM Activate the virtual environment
call Scripts\activate

REM Run the Python script
python claude_launcher.py

REM Deactivate the virtual environment
deactivate

pause
