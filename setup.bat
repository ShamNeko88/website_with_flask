@echo off
python -m venv venv
venv\Scripts\pip.exe install -r requirements.txt
del data
mkdir data
venv\Scripts\python.exe setup.py

