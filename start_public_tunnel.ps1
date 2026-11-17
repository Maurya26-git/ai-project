Write-Host "=========================================================================" -ForegroundColor Cyan
Write-Host "   Sentix - Free Public Worldwide HTTPS Tunnel" -ForegroundColor Cyan
Write-Host "   Exposing http://127.0.0.1:5000 to the Global Internet" -ForegroundColor Cyan
Write-Host "=========================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting Cloudflare Tunnel..." -ForegroundColor Yellow
Write-Host "Copy the generated 'https://*.trycloudflare.com' link and paste it into"
Write-Host "the Sentix QR Code Modal to share access across ANY network (4G/5G/WiFi)!"
Write-Host ""
cloudflared tunnel --url http://127.0.0.1:5000
