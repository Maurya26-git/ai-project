@echo off
title Sentix Public Worldwide Tunnel (Cloudflare Tunnel)
echo =========================================================================
echo    Sentix - Free Public Worldwide HTTPS Tunnel
echo    Exposing http://127.0.0.1:5000 to the Global Internet
echo =========================================================================
echo.
echo Starting Cloudflare Tunnel...
echo Copy the generated "https://*.trycloudflare.com" link below and paste it 
echo into the Sentix QR Code Modal to share access with any smartphone on ANY network!
echo.
cloudflared tunnel --url http://127.0.0.1:5000
pause
