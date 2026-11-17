@echo off
echo ====================================================
echo Recompiling Project Synopsis PDF from HTML...
echo ====================================================
python "%~dp0generate_pdf.py"
echo.
pause
