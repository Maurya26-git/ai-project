@echo off
title Push Sentiment Analyzer to GitHub
color 0A
cd /d "C:\Users\remal\.gemini\antigravity\scratch\sentiment-analyzer"

echo ======================================================================
echo           PUSHING SENTIMENT ANALYZER TO GITHUB
echo   Repository: https://github.com/Maurya26-git/ai-project.git
echo ======================================================================
echo.

:: Ensure origin is set
git remote remove origin 2>nul
git remote add origin https://github.com/Maurya26-git/ai-project.git

echo Checking status...
git status
echo.

echo Pushing main branch to origin...
echo (If a GitHub login window appears, please click 'Sign in with your browser')
echo.
git push -u origin main --force

echo.
if %ERRORLEVEL% EQU 0 (
    echo ======================================================================
    echo [SUCCESS] All files pushed successfully to GitHub!
    echo View repository at: https://github.com/Maurya26-git/ai-project
    echo ======================================================================
) else (
    echo ======================================================================
    echo [NOTICE] Push needs GitHub authentication.
    echo If you have a Personal Access Token (PAT), you can paste it when prompted.
    echo ======================================================================
)

echo.
echo Press any key to exit...
pause >nul
