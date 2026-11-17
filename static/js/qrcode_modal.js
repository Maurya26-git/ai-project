/**
 * Sentix - QR Code & Remote Network Access Module
 * Emerald Obsidian & Deep Black Theme
 * Generates dynamic, real-time QR codes for Local Wi-Fi and Worldwide Public Internet access.
 */

let networkInfo = null;
let currentTargetUrl = '';
let activeQrMode = 'local'; // 'local' or 'public'
let publicUrlDebounce = null;

document.addEventListener('DOMContentLoaded', () => {
    initQrModal();
});

async function initQrModal() {
    const modal = document.getElementById('qr-access-modal');
    const openBtn = document.getElementById('btn-open-qr-modal');
    const closeBtn = document.getElementById('btn-close-qr-modal');
    const tabLocal = document.getElementById('qr-tab-local');
    const tabPublic = document.getElementById('qr-tab-public');
    const publicUrlInput = document.getElementById('qr-public-url-input');
    const applyPublicBtn = document.getElementById('btn-apply-public-url');
    const sampleTunnelBtn = document.getElementById('btn-sample-tunnel-url');
    const copyBtn = document.getElementById('btn-copy-access-url');
    const openUrlBtn = document.getElementById('btn-open-target-url');

    // 1. Fetch local network info from backend
    try {
        const res = await fetch('/api/network-info');
        const json = await res.json();
        if (json.success) {
            networkInfo = json;
            if (activeQrMode === 'local') {
                currentTargetUrl = json.local_url;
                updateLocalQr(currentTargetUrl);
            }
        }
    } catch (e) {
        console.error('Error fetching network info:', e);
        if (activeQrMode === 'local') {
            currentTargetUrl = window.location.origin;
            updateLocalQr(currentTargetUrl);
        }
    }

    // Initialize saved public URL or default
    const savedPublic = localStorage.getItem('sentix_public_url') || 'https://sentix-demo.trycloudflare.com';
    if (publicUrlInput) {
        publicUrlInput.value = savedPublic;
    }
    updatePublicQr(savedPublic);

    // Open Modal
    openBtn?.addEventListener('click', () => {
        modal?.classList.remove('hidden');
        if (activeQrMode === 'local') {
            updateLocalQr(networkInfo ? networkInfo.local_url : window.location.origin);
        } else {
            updatePublicQr(publicUrlInput ? publicUrlInput.value.trim() : savedPublic);
        }
    });

    closeBtn?.addEventListener('click', () => {
        modal?.classList.add('hidden');
    });

    modal?.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.add('hidden');
    });

    // Switch to Local WiFi tab
    tabLocal?.addEventListener('click', () => {
        activeQrMode = 'local';
        tabLocal.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        tabLocal.classList.remove('bg-transparent', 'text-zinc-400');
        tabPublic?.classList.remove('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        tabPublic?.classList.add('bg-transparent', 'text-zinc-400');

        document.getElementById('qr-local-panel')?.classList.remove('hidden');
        document.getElementById('qr-public-panel')?.classList.add('hidden');

        currentTargetUrl = networkInfo ? networkInfo.local_url : window.location.origin;
        updateLocalQr(currentTargetUrl);
    });

    // Switch to Worldwide Public Network tab
    tabPublic?.addEventListener('click', () => {
        activeQrMode = 'public';
        tabPublic.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        tabPublic.classList.remove('bg-transparent', 'text-zinc-400');
        tabLocal?.classList.remove('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        tabLocal?.classList.add('bg-transparent', 'text-zinc-400');

        document.getElementById('qr-local-panel')?.classList.add('hidden');
        document.getElementById('qr-public-panel')?.classList.remove('hidden');

        let pubUrl = publicUrlInput?.value.trim() || savedPublic;
        if (!pubUrl) pubUrl = 'https://sentix-demo.trycloudflare.com';
        currentTargetUrl = pubUrl;
        updatePublicQr(currentTargetUrl);
    });

    // Real-time update as user pastes or types their Cloudflare Tunnel URL
    publicUrlInput?.addEventListener('input', () => {
        clearTimeout(publicUrlDebounce);
        publicUrlDebounce = setTimeout(() => {
            const val = publicUrlInput.value.trim();
            if (val) {
                currentTargetUrl = val;
                localStorage.setItem('sentix_public_url', val);
                updatePublicQr(val);
                flashQrStatus('Updated Public QR Code!');
            }
        }, 250);
    });

    // Explicit "Update QR" button click
    applyPublicBtn?.addEventListener('click', () => {
        const val = publicUrlInput?.value.trim();
        if (val) {
            currentTargetUrl = val;
            localStorage.setItem('sentix_public_url', val);
            updatePublicQr(val);
            flashQrStatus('Updated Public QR Code!');
        } else {
            alert('Please enter a valid URL (e.g. https://your-tunnel.trycloudflare.com)');
        }
    });

    // "Try Sample Tunnel" button
    sampleTunnelBtn?.addEventListener('click', () => {
        const sampleUrl = 'https://sentix-tunnel-' + Math.floor(1000 + Math.random() * 9000) + '.trycloudflare.com';
        if (publicUrlInput) {
            publicUrlInput.value = sampleUrl;
        }
        currentTargetUrl = sampleUrl;
        localStorage.setItem('sentix_public_url', sampleUrl);
        updatePublicQr(sampleUrl);
        flashQrStatus('Loaded Sample Cloudflare Tunnel URL!');
    });

    // Copy URL
    copyBtn?.addEventListener('click', () => {
        const urlToCopy = currentTargetUrl || (activeQrMode === 'local' ? (networkInfo?.local_url || window.location.origin) : publicUrlInput?.value.trim());
        if (!urlToCopy) return;

        navigator.clipboard.writeText(urlToCopy).then(() => {
            const original = copyBtn.innerHTML;
            copyBtn.innerHTML = '<i data-lucide="check" class="w-3.5 h-3.5 text-emerald-400"></i> Copied!';
            if (window.lucide) lucide.createIcons();
            setTimeout(() => {
                copyBtn.innerHTML = original;
                if (window.lucide) lucide.createIcons();
            }, 2000);
        });
    });

    // Open URL
    openUrlBtn?.addEventListener('click', () => {
        if (currentTargetUrl) {
            window.open(currentTargetUrl, '_blank');
        }
    });
}

function updateLocalQr(url) {
    const qrImg = document.getElementById('qr-code-img');
    const urlDisplay = document.getElementById('qr-current-url-display');

    if (urlDisplay) {
        urlDisplay.innerText = url;
    }

    if (qrImg && url) {
        qrImg.src = `/api/qrcode?url=${encodeURIComponent(url)}&t=${Date.now()}`;
    }
}

function updatePublicQr(url) {
    const publicQrImg = document.getElementById('qr-public-code-img');
    const urlDisplay = document.getElementById('qr-current-url-display');
    const currentPublicSpan = document.getElementById('qr-public-current-url-span');

    if (urlDisplay) {
        urlDisplay.innerText = url;
    }

    if (currentPublicSpan) {
        currentPublicSpan.innerText = url;
    }

    if (publicQrImg && url) {
        publicQrImg.classList.add('opacity-40', 'scale-95');
        publicQrImg.src = `/api/qrcode?url=${encodeURIComponent(url)}&t=${Date.now()}`;
        publicQrImg.onload = () => {
            publicQrImg.classList.remove('opacity-40', 'scale-95');
        };
    }
}

function flashQrStatus(msg) {
    const badge = document.getElementById('qr-public-status-badge');
    if (badge) {
        badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping mr-1"></span> ${msg}`;
        badge.className = 'text-[11px] font-bold text-emerald-300 flex items-center justify-center transition-all';
        setTimeout(() => {
            badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400 mr-1"></span> Live Public QR Ready to Scan`;
            badge.className = 'text-[11px] font-bold text-emerald-400 flex items-center justify-center transition-all';
        }, 2500);
    }
}

window.openQrAccessModal = function() {
    const modal = document.getElementById('qr-access-modal');
    modal?.classList.remove('hidden');
};
