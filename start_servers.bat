@echo off
:: Run Flask backend
start cmd /k "cd backend && python server.py"

:: Wait for a few seconds to make sure Flask starts before running React
timeout /t 5

:: Run React frontend
start cmd /k "cd frontend && npm start"
