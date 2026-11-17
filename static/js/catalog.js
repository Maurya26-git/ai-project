/**
 * Sentix - Interactive Catalog Engine (Electronics, Movies, Games & World Destinations)
 * Emerald Obsidian & Deep Black Theme
 * Handles section browsing, subcategory filtering, universal AI entity synthesis,
 * authentic poster fallbacks, and instant transfer to Live Analyzer & History.
 */

let activeCatalogType = 'electronics'; // 'electronics', 'movie', 'game', or 'travel'
let activeSubcategory = 'all';
let currentLoadedItem = null;
let reviewPreviewDebounce = null;

document.addEventListener('DOMContentLoaded', () => {
    initCatalog();
});

function initCatalog() {
    initCatalogTabs();
    initSubcategoryFilters();
    initCatalogSearch();
    loadCatalogItems();
    initReviewModal();
    initUniversalSearchBanner();
}

/* ==========================================================================
   Reliable Emerald Obsidian SVG Poster Fallback Generator
   Guarantees 100% zero broken image icons under any network condition!
   ========================================================================== */
window.handlePosterError = function(img, title, type, category) {
    if (!img) return;
    img.onerror = null; // Prevent recursion

    let icon = "⚡";
    let typeName = "TECH HARDWARE";
    if (type === 'movie') {
        icon = "🎬";
        typeName = "CINEMA POSTER";
    } else if (type === 'game') {
        icon = "🎮";
        typeName = "VIDEO GAME";
    } else if (type === 'travel') {
        icon = "✈️";
        typeName = "WORLD DESTINATION";
    }

    const cleanTitle = (title || 'Sentix Item').replace(/[<>&'"]/g, '');
    const displayTitle = cleanTitle.length > 24 ? cleanTitle.substring(0, 22) + '...' : cleanTitle;

    const svg = `
        <svg xmlns="http://www.w3.org/2000/svg" width="600" height="900" viewBox="0 0 600 900">
            <defs>
                <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#040605" />
                    <stop offset="50%" stop-color="#090e0c" />
                    <stop offset="100%" stop-color="#050706" />
                </linearGradient>
                <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#059669" />
                    <stop offset="50%" stop-color="#34d399" />
                    <stop offset="100%" stop-color="#047857" />
                </linearGradient>
            </defs>
            <rect width="600" height="900" fill="url(#bgGrad)"/>
            <rect x="24" y="24" width="552" height="852" rx="28" fill="none" stroke="url(#emeraldGrad)" stroke-width="2" stroke-opacity="0.35"/>
            <circle cx="300" cy="380" r="90" fill="#10b981" fill-opacity="0.08" stroke="url(#emeraldGrad)" stroke-width="1.8"/>
            <text x="300" y="410" font-family="system-ui, sans-serif" font-size="75" text-anchor="middle">${icon}</text>
            <text x="300" y="530" font-family="system-ui, sans-serif" font-size="30" font-weight="900" fill="#ecfdf5" text-anchor="middle">${displayTitle}</text>
            <text x="300" y="575" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#10b981" letter-spacing="4" text-anchor="middle">${typeName}</text>
            <text x="300" y="820" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#71717a" letter-spacing="2" text-anchor="middle">SENTIX AI INTELLIGENCE</text>
        </svg>
    `;

    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg.trim());
};

/* ==========================================================================
   Catalog Main Tab Navigation (Electronics vs Movies vs Games vs Travel)
   ========================================================================== */
function initCatalogTabs() {
    const electronicsBtn = document.getElementById('catalog-tab-electronics');
    const moviesBtn = document.getElementById('catalog-tab-movies');
    const gamesBtn = document.getElementById('catalog-tab-games');
    const travelBtn = document.getElementById('catalog-tab-travel');

    electronicsBtn?.addEventListener('click', () => {
        activeCatalogType = 'electronics';
        activeSubcategory = 'all';
        updateCatalogTypeUI();
        loadCatalogItems();
    });

    moviesBtn?.addEventListener('click', () => {
        activeCatalogType = 'movie';
        activeSubcategory = 'all';
        updateCatalogTypeUI();
        loadCatalogItems();
    });

    gamesBtn?.addEventListener('click', () => {
        activeCatalogType = 'game';
        activeSubcategory = 'all';
        updateCatalogTypeUI();
        loadCatalogItems();
    });

    travelBtn?.addEventListener('click', () => {
        activeCatalogType = 'travel';
        activeSubcategory = 'all';
        updateCatalogTypeUI();
        loadCatalogItems();
    });
}

function updateCatalogTypeUI() {
    const electronicsBtn = document.getElementById('catalog-tab-electronics');
    const moviesBtn = document.getElementById('catalog-tab-movies');
    const gamesBtn = document.getElementById('catalog-tab-games');
    const travelBtn = document.getElementById('catalog-tab-travel');
    const filterPillsContainer = document.getElementById('catalog-filter-pills');

    const allButtons = [electronicsBtn, moviesBtn, gamesBtn, travelBtn];
    allButtons.forEach(btn => {
        btn?.classList.remove('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        btn?.classList.add('bg-transparent', 'text-slate-600', 'dark:text-zinc-400');
    });

    if (activeCatalogType === 'electronics') {
        electronicsBtn?.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        electronicsBtn?.classList.remove('bg-transparent', 'text-slate-600', 'dark:text-zinc-400');

        if (filterPillsContainer) {
            filterPillsContainer.innerHTML = `
                <button data-subcat="all" class="subcat-pill active px-3.5 py-1.5 rounded-full text-xs font-black bg-emerald-500 text-slate-950 shadow-sm transition">All Electronics</button>
                <button data-subcat="mobiles" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">📱 Mobiles</button>
                <button data-subcat="gadgets" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🎧 Gadgets & Audio</button>
            `;
            initSubcategoryFilters();
        }
    } else if (activeCatalogType === 'movie') {
        moviesBtn?.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        moviesBtn?.classList.remove('bg-transparent', 'text-slate-600', 'dark:text-zinc-400');

        if (filterPillsContainer) {
            filterPillsContainer.innerHTML = `
                <button data-subcat="all" class="subcat-pill active px-3.5 py-1.5 rounded-full text-xs font-black bg-emerald-500 text-slate-950 shadow-sm transition">All Genres</button>
                <button data-subcat="sci-fi" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🚀 Sci-Fi</button>
                <button data-subcat="action" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">💥 Action</button>
                <button data-subcat="thriller" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🧠 Thriller</button>
                <button data-subcat="animation" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🎨 Animation</button>
            `;
            initSubcategoryFilters();
        }
    } else if (activeCatalogType === 'game') {
        gamesBtn?.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        gamesBtn?.classList.remove('bg-transparent', 'text-slate-600', 'dark:text-zinc-400');

        if (filterPillsContainer) {
            filterPillsContainer.innerHTML = `
                <button data-subcat="all" class="subcat-pill active px-3.5 py-1.5 rounded-full text-xs font-black bg-emerald-500 text-slate-950 shadow-sm transition">All Video Games</button>
                <button data-subcat="action-rpg" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">⚔️ Action RPG</button>
                <button data-subcat="open-world" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🌍 Open World</button>
                <button data-subcat="sci-fi" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🚀 Sci-Fi RPG</button>
            `;
            initSubcategoryFilters();
        }
    } else if (activeCatalogType === 'travel') {
        travelBtn?.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-green-600', 'text-slate-950', 'shadow-md', 'font-black');
        travelBtn?.classList.remove('bg-transparent', 'text-slate-600', 'dark:text-zinc-400');

        if (filterPillsContainer) {
            filterPillsContainer.innerHTML = `
                <button data-subcat="all" class="subcat-pill active px-3.5 py-1.5 rounded-full text-xs font-black bg-emerald-500 text-slate-950 shadow-sm transition">All Destinations</button>
                <button data-subcat="japan" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🌸 Japan</button>
                <button data-subcat="france" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🗼 France</button>
                <button data-subcat="italy" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🏛️ Rome</button>
                <button data-subcat="switzerland" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🏔️ Swiss Alps</button>
                <button data-subcat="india" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🕌 Taj Mahal</button>
                <button data-subcat="greece" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🌊 Santorini</button>
                <button data-subcat="egypt" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🏜️ Pyramids</button>
                <button data-subcat="iceland" class="subcat-pill px-3.5 py-1.5 rounded-full text-xs font-semibold bg-slate-100 dark:bg-zinc-800 text-slate-700 dark:text-zinc-300 hover:bg-emerald-500/20 transition">🌌 Iceland</button>
            `;
            initSubcategoryFilters();
        }
    }
}

function initSubcategoryFilters() {
    const pills = document.querySelectorAll('.subcat-pill');
    pills.forEach((p) => {
        p.addEventListener('click', () => {
            pills.forEach((btn) => {
                btn.classList.remove('active', 'bg-emerald-500', 'text-slate-950', 'font-black');
                btn.classList.add('bg-slate-100', 'dark:bg-zinc-800', 'text-slate-700', 'dark:text-zinc-300');
            });
            p.classList.add('active', 'bg-emerald-500', 'text-slate-950', 'font-black');
            p.classList.remove('bg-slate-100', 'dark:bg-zinc-800', 'text-slate-700', 'dark:text-zinc-300');

            activeSubcategory = p.getAttribute('data-subcat');
            loadCatalogItems();
        });
    });
}

function initCatalogSearch() {
    const searchInput = document.getElementById('catalog-search-input');
    searchInput?.addEventListener('input', () => {
        const val = searchInput.value.trim();
        const banner = document.getElementById('universal-search-banner');
        const querySpan = document.getElementById('universal-search-query-name');

        if (val.length >= 2) {
            banner?.classList.remove('hidden');
            if (querySpan) querySpan.textContent = `"${val}"`;
        } else {
            banner?.classList.add('hidden');
        }

        loadCatalogItems();
    });

    searchInput?.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const val = searchInput.value.trim();
            if (val) triggerUniversalSynthesize(val);
        }
    });
}

function initUniversalSearchBanner() {
    const btn = document.getElementById('btn-trigger-universal-synthesize');
    btn?.addEventListener('click', () => {
        const searchInput = document.getElementById('catalog-search-input');
        const val = searchInput?.value.trim();
        if (val) triggerUniversalSynthesize(val);
    });
}

/* ==========================================================================
   Universal AI Entity Synthesis: Any Item in the World!
   ========================================================================== */
window.triggerUniversalSynthesize = async function(query) {
    if (!query || !query.trim()) return;

    const container = document.getElementById('catalog-grid-container');
    const banner = document.getElementById('universal-search-banner');
    if (!container) return;

    container.innerHTML = `
        <div class="col-span-full py-20 flex flex-col items-center justify-center text-center">
            <div class="w-16 h-16 rounded-3xl bg-emerald-500/20 border-2 border-emerald-500/50 flex items-center justify-center text-emerald-400 mb-4 animate-pulse glow-emerald">
                <i data-lucide="cpu" class="w-8 h-8"></i>
            </div>
            <h3 class="text-base font-black text-zinc-100">Sentix Universal Synthesis Active</h3>
            <p class="text-xs text-zinc-400 mt-1 max-w-sm">Generating authentic specifications, high-res portrait posters, and pre-analyzing customer reviews for <strong class="text-emerald-400">"${query}"</strong>...</p>
        </div>
    `;
    if (window.lucide) lucide.createIcons();

    try {
        const res = await fetch(`/api/universal-search?q=${encodeURIComponent(query)}&force=true`);
        const data = await res.json();

        if (data.success && data.item) {
            const item = data.item;

            // Switch active catalog tab to match synthesized item type
            if (item.type && item.type !== activeCatalogType) {
                activeCatalogType = item.type;
                activeSubcategory = 'all';
                updateCatalogTypeUI();
            }

            banner?.classList.add('hidden');
            const searchInput = document.getElementById('catalog-search-input');
            if (searchInput) searchInput.value = '';

            // Reload and prepend
            await loadCatalogItems();

            if (window.triggerConfetti) window.triggerConfetti();

            // Flash toast notification
            showToast(`✨ Universal Dossier Generated: ${item.title}`);
        } else {
            container.innerHTML = `<div class="col-span-full py-12 text-center text-rose-400 text-xs">Synthesis failed: ${data.error || 'Unknown error'}</div>`;
        }
    } catch (e) {
        console.error('Error synthesizing entity:', e);
        container.innerHTML = '<div class="col-span-full py-12 text-center text-rose-400 text-xs">Network error during universal synthesis.</div>';
    }
};

function showToast(msg) {
    const toast = document.createElement('div');
    toast.className = "fixed bottom-6 right-6 z-50 p-4 rounded-2xl bg-[#090e0c]/95 border border-emerald-500/50 text-emerald-300 font-bold text-xs shadow-2xl backdrop-blur-xl flex items-center gap-2 animate-bounce";
    toast.innerHTML = `<i data-lucide="sparkles" class="w-4 h-4 text-emerald-400"></i> ${msg}`;
    document.body.appendChild(toast);
    if (window.lucide) lucide.createIcons();
    setTimeout(() => toast.remove(), 4000);
}

/* ==========================================================================
   Load & Render Items Grid
   ========================================================================== */
async function loadCatalogItems() {
    const container = document.getElementById('catalog-grid-container');
    const searchVal = document.getElementById('catalog-search-input')?.value.trim() || '';
    if (!container) return;

    let url = `/api/catalog?type=${activeCatalogType}`;
    if (activeSubcategory && activeSubcategory !== 'all') {
        url += `&category=${activeSubcategory}`;
    }
    if (searchVal) {
        url += `&search=${encodeURIComponent(searchVal)}`;
    }

    const typeNames = {
        'electronics': 'Electronics',
        'movie': 'Movies',
        'game': 'Video Games',
        'travel': 'World Destinations'
    };

    container.innerHTML = `
        <div class="col-span-full py-16 flex flex-col items-center justify-center text-emerald-400">
            <div class="animate-spin w-8 h-8 border-3 border-emerald-500 border-t-transparent rounded-full mb-3"></div>
            <p class="text-xs font-medium text-zinc-400">Loading ${typeNames[activeCatalogType] || 'Catalog'} collection...</p>
        </div>
    `;

    try {
        const res = await fetch(url);
        const data = await res.json();

        if (data.success && data.items) {
            renderCatalogGrid(data.items, searchVal);
        } else {
            container.innerHTML = '<div class="col-span-full py-12 text-center text-slate-400 text-sm">Failed to load items.</div>';
        }
    } catch (e) {
        console.error('Error fetching catalog:', e);
        container.innerHTML = '<div class="col-span-full py-12 text-center text-slate-400 text-sm">Network error loading catalog.</div>';
    }
}

function renderCatalogGrid(items, searchVal) {
    const container = document.getElementById('catalog-grid-container');
    if (!container) return;
    container.innerHTML = '';

    if (items.length === 0) {
        if (searchVal) {
            container.innerHTML = `
                <div class="col-span-full py-16 text-center text-slate-400">
                    <div class="w-14 h-14 mx-auto rounded-3xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 mb-3 glow-emerald">
                        <i data-lucide="sparkles" class="w-7 h-7"></i>
                    </div>
                    <p class="text-base font-extrabold text-zinc-100">Item not in local library</p>
                    <p class="text-xs text-zinc-400 mt-1 max-w-md mx-auto">Sentix Universal Search can generate an authentic dossier for <strong>"${searchVal}"</strong> on the fly with live NLP sentiment analysis!</p>
                    <button onclick="triggerUniversalSynthesize('${searchVal.replace(/'/g, "\\'")}')" class="mt-4 px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 via-emerald-400 to-green-600 text-slate-950 font-black text-xs shadow-lg shadow-emerald-500/25 hover:from-emerald-600 hover:to-green-700 transition inline-flex items-center gap-2">
                        <i data-lucide="cpu" class="w-4 h-4"></i> Synthesize Live Dossier for "${searchVal}"
                    </button>
                </div>
            `;
        } else {
            container.innerHTML = `
                <div class="col-span-full py-16 text-center text-slate-400">
                    <i data-lucide="package-x" class="w-10 h-10 mx-auto text-emerald-500/40 mb-2"></i>
                    <p class="text-sm font-semibold text-zinc-300">No matching items found</p>
                    <p class="text-xs text-zinc-500 mt-1">Try clearing search filters.</p>
                </div>
            `;
        }
        if (window.lucide) lucide.createIcons();
        return;
    }

    items.forEach((item) => {
        const sentiment = item.sentiment;
        const isPos = sentiment.label.includes('Positive');
        const badgeColor = isPos ? 'bg-emerald-500/15 text-emerald-400 border-emerald-500/40' : 'bg-rose-500/15 text-rose-400 border-rose-500/40';

        const isPosterStyle = item.type === 'movie' || item.type === 'game' || item.type === 'travel';
        const imageHeightClass = isPosterStyle ? 'h-60 sm:h-64' : 'h-44';

        const safeTitle = (item.title || '').replace(/'/g, "\\'");

        const card = document.createElement('div');
        card.className = "tilt-card emerald-card-hover group relative rounded-3xl border border-emerald-500/20 dark:border-emerald-500/25 bg-white/90 dark:bg-[#0b100d]/90 p-4 shadow-md hover:shadow-2xl transition-all duration-300 flex flex-col justify-between overflow-hidden cursor-pointer";

        card.innerHTML = `
            <!-- Top Poster / Hardware Image -->
            <div class="relative w-full ${imageHeightClass} rounded-2xl overflow-hidden mb-3 bg-[#040605] flex items-center justify-center">
                <img src="${item.image}" alt="${item.title}" loading="lazy" class="w-full h-full object-cover group-hover:scale-106 transition-transform duration-500" onerror="window.handlePosterError(this, '${safeTitle}', '${item.type}', '${item.category}')">
                <div class="absolute inset-0 bg-gradient-to-t from-[#040605]/90 via-[#040605]/20 to-transparent"></div>
                <span class="absolute top-2.5 left-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-black bg-[#040605]/90 text-emerald-400 border border-emerald-500/40 backdrop-blur-md">
                    ${item.badge}
                </span>
                ${item.price ? `<span class="absolute bottom-2.5 right-2.5 px-2.5 py-1 rounded-lg text-xs font-black bg-gradient-to-r from-emerald-500 to-green-600 text-slate-950 shadow-md">${item.price}</span>` : ''}
                ${item.duration ? `<span class="absolute bottom-2.5 right-2.5 px-2.5 py-1 rounded-lg text-xs font-bold bg-[#040605]/90 text-emerald-300 border border-emerald-500/40 backdrop-blur-md">${item.duration}</span>` : ''}
                ${item.best_season ? `<span class="absolute bottom-2.5 right-2.5 px-2.5 py-1 rounded-lg text-xs font-bold bg-[#040605]/90 text-emerald-300 border border-emerald-500/40 backdrop-blur-md">🗓️ ${item.best_season}</span>` : ''}
            </div>

            <!-- Content -->
            <div class="flex-1 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between text-[11px] text-emerald-500/80 mb-1 font-semibold">
                        <span>${item.category_label}</span>
                        ${item.director ? `<span>Dir: ${item.director}</span>` : ''}
                        ${item.developer ? `<span>Dev: ${item.developer}</span>` : ''}
                        ${item.country ? `<span>📍 ${item.country}</span>` : ''}
                    </div>
                    <h3 class="font-extrabold text-sm text-slate-900 dark:text-zinc-100 group-hover:text-emerald-400 transition truncate" title="${item.title}">${item.title}</h3>
                    <p class="text-xs text-slate-600 dark:text-zinc-400 line-clamp-2 mt-1 leading-relaxed">${item.tagline}</p>
                </div>

                <!-- Sentiment Summary Meter -->
                <div class="mt-4 pt-3 border-t border-emerald-500/15 dark:border-emerald-500/20">
                    <div class="flex items-center justify-between mb-1.5">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 dark:text-zinc-400">Consensus:</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded-full border ${badgeColor}">
                            ${sentiment.pos_percent}% Positive (${(sentiment.score > 0 ? '+' : '') + sentiment.score.toFixed(2)})
                        </span>
                    </div>
                    
                    <div class="w-full h-1.5 rounded-full bg-zinc-200 dark:bg-zinc-800 overflow-hidden flex">
                        <div class="h-full bg-emerald-500" style="width: ${sentiment.pos_percent}%"></div>
                        <div class="h-full bg-zinc-600" style="width: ${sentiment.neu_percent}%"></div>
                        <div class="h-full bg-rose-500" style="width: ${sentiment.neg_percent}%"></div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="grid grid-cols-2 gap-2 mt-3.5">
                        <button class="btn-select-live-analyzer w-full py-2 px-2 rounded-xl bg-gradient-to-r from-emerald-500 via-emerald-400 to-green-600 hover:from-emerald-600 hover:to-green-700 text-slate-950 font-black text-xs shadow-md shadow-emerald-500/20 transition flex items-center justify-center gap-1.5">
                            <i data-lucide="zap" class="w-3.5 h-3.5"></i> Analyze Live
                        </button>
                        <button class="btn-inspect-modal w-full py-2 px-2 rounded-xl border border-emerald-500/30 hover:bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-bold text-xs transition flex items-center justify-center gap-1">
                            <i data-lucide="sliders" class="w-3.5 h-3.5"></i> Reviews
                        </button>
                    </div>
                </div>
            </div>
        `;

        // Action 1: Select item -> takes to Live Analyzer & saves to History
        const liveBtn = card.querySelector('.btn-select-live-analyzer');
        liveBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            sendItemToLiveAnalyzerAndHistory(item);
        });

        // Clicking card also directly selects the item for Live Analysis
        card.addEventListener('click', () => {
            sendItemToLiveAnalyzerAndHistory(item);
        });

        // Action 2: Inspect in Modal
        const inspectBtn = card.querySelector('.btn-inspect-modal');
        inspectBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            openReviewModal(item.id);
        });

        container.appendChild(card);
    });

    if (window.apply3DTiltListeners) window.apply3DTiltListeners();
    if (window.lucide) lucide.createIcons();
}

/* ==========================================================================
   Seamless Transfer: Item Selected -> Live Analyzer -> History
   ========================================================================== */
window.sendItemToLiveAnalyzerAndHistory = async function(item) {
    const input = document.getElementById('sentiment-text-input');
    if (!input) return;

    let fullItem = item;
    try {
        const res = await fetch(`/api/catalog/${item.id}`);
        const data = await res.json();
        if (data.success && data.item) {
            fullItem = data.item;
        }
    } catch (e) {
        console.error('Error fetching full item for live analyzer:', e);
    }

    const reviewSnippets = (fullItem.reviews || []).map(r => `"${r.text}"`).join(' ');
    const fullText = `[${fullItem.title} - ${fullItem.category_label}] ${fullItem.tagline}. Key aspects evaluated: ${fullItem.aspects_preset ? fullItem.aspects_preset.join(', ') : 'Performance, Quality, Value'}. Verified customer feedback: ${reviewSnippets}`;

    input.value = fullText;
    if (window.updateCharWordCounts) window.updateCharWordCounts();

    const liveTabBtn = document.querySelector('[data-tab="tab-live"]');
    liveTabBtn?.click();

    if (window.triggerAnalysis) {
        window.triggerAnalysis(fullItem.title);
    }

    if (window.triggerConfetti) {
        window.triggerConfetti();
    }
};

/* ==========================================================================
   Review & Inspect Modal
   ========================================================================== */
function initReviewModal() {
    const modal = document.getElementById('item-review-modal');
    const closeBtn = document.getElementById('btn-close-review-modal');
    const reviewTextarea = document.getElementById('modal-review-input');
    const submitBtn = document.getElementById('btn-submit-review');
    const sendToLiveBtn = document.getElementById('modal-btn-send-to-live');
    const starBtns = document.querySelectorAll('.star-rating-btn');

    closeBtn?.addEventListener('click', () => {
        modal?.classList.add('hidden');
    });

    modal?.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.add('hidden');
    });

    sendToLiveBtn?.addEventListener('click', () => {
        if (currentLoadedItem) {
            modal?.classList.add('hidden');
            sendItemToLiveAnalyzerAndHistory(currentLoadedItem);
        }
    });

    reviewTextarea?.addEventListener('input', () => {
        clearTimeout(reviewPreviewDebounce);
        reviewPreviewDebounce = setTimeout(() => {
            updateLiveReviewSentimentPreview();
        }, 300);
    });

    let selectedRating = 5;
    starBtns.forEach((btn) => {
        btn.addEventListener('click', () => {
            selectedRating = parseInt(btn.getAttribute('data-star'));
            updateStarDisplay(selectedRating);
        });
    });

    // Preset chips
    const presets = document.querySelectorAll('.modal-review-preset');
    presets.forEach(p => {
        p.addEventListener('click', () => {
            if (reviewTextarea) {
                reviewTextarea.value = p.getAttribute('data-text');
                updateLiveReviewSentimentPreview();
            }
        });
    });

    submitBtn?.addEventListener('click', async () => {
        if (!currentLoadedItem) return;
        const text = reviewTextarea?.value.trim();
        const author = document.getElementById('modal-review-author')?.value.trim() || 'Verified Reviewer';

        if (!text) {
            alert('Please write review text before submitting.');
            return;
        }

        submitBtn.innerHTML = '<i data-lucide="loader-2" class="w-3.5 h-3.5 animate-spin"></i> Submitting...';
        submitBtn.disabled = true;

        try {
            const res = await fetch(`/api/catalog/${currentLoadedItem.id}/review`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    text: text,
                    author: author,
                    rating: selectedRating
                })
            });
            const data = await res.json();

            if (data.success) {
                reviewTextarea.value = '';
                document.getElementById('modal-review-live-badge').textContent = 'Type to preview sentiment';
                openReviewModal(currentLoadedItem.id);
                loadCatalogItems();

                if (window.triggerConfetti) window.triggerConfetti();
            } else {
                alert(data.error || 'Failed to submit review.');
            }
        } catch (e) {
            console.error('Error submitting review:', e);
            alert('Network error submitting review.');
        } finally {
            submitBtn.innerHTML = '<i data-lucide="send" class="w-3.5 h-3.5"></i> Submit Review';
            submitBtn.disabled = false;
            if (window.lucide) lucide.createIcons();
        }
    });
}

function updateStarDisplay(rating) {
    const starBtns = document.querySelectorAll('.star-rating-btn');
    starBtns.forEach((btn, idx) => {
        if (idx < rating) {
            btn.classList.add('text-emerald-400');
            btn.classList.remove('text-zinc-600');
        } else {
            btn.classList.remove('text-emerald-400');
            btn.classList.add('text-zinc-600');
        }
    });
}

async function updateLiveReviewSentimentPreview() {
    const text = document.getElementById('modal-review-input')?.value.trim();
    const badge = document.getElementById('modal-review-live-badge');
    if (!badge) return;

    if (!text) {
        badge.textContent = 'Type to preview sentiment';
        badge.className = 'px-2 py-0.5 rounded text-[10px] font-semibold bg-zinc-800 text-zinc-400';
        return;
    }

    try {
        const res = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await res.json();

        if (data.success && data.data) {
            const score = data.data.overall.compound_score;
            const label = data.data.overall.label;
            const emotion = data.data.emotions.dominant;

            badge.textContent = `${label} (${score > 0 ? '+' : ''}${score.toFixed(2)}) · ${emotion}`;
            badge.className = `px-2 py-0.5 rounded text-[10px] font-bold ${
                score > 0.05 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' :
                (score < -0.05 ? 'bg-rose-500/20 text-rose-400 border border-rose-500/40' : 'bg-zinc-800 text-zinc-300')
            }`;
        }
    } catch (e) {
        console.error('Error previewing review sentiment:', e);
    }
}

async function openReviewModal(itemId) {
    const modal = document.getElementById('item-review-modal');
    if (!modal) return;

    try {
        const res = await fetch(`/api/catalog/${itemId}`);
        const data = await res.json();

        if (data.success && data.item) {
            const item = data.item;
            currentLoadedItem = item;

            const modalImg = document.getElementById('modal-item-image');
            if (modalImg) {
                modalImg.src = item.image;
                modalImg.onerror = () => window.handlePosterError(modalImg, item.title, item.type, item.category);
            }

            document.getElementById('modal-item-title').textContent = item.title;
            document.getElementById('modal-item-category').textContent = item.category_label;
            document.getElementById('modal-item-tagline').textContent = item.tagline;

            const sentiment = item.sentiment;
            const scoreEl = document.getElementById('modal-sentiment-score');
            if (scoreEl) {
                scoreEl.textContent = `${sentiment.score > 0 ? '+' : ''}${sentiment.score.toFixed(2)}`;
                scoreEl.className = `text-2xl font-black ${sentiment.score > 0 ? 'text-emerald-400' : (sentiment.score < 0 ? 'text-rose-400' : 'text-zinc-400')}`;
            }

            document.getElementById('modal-pos-pct').textContent = `${sentiment.pos_percent}% Positive`;
            document.getElementById('modal-neg-pct').textContent = `${sentiment.neg_percent}% Negative`;
            document.getElementById('modal-emotion-badge').textContent = `Dominant Emotion: ${sentiment.dominant_emotion}`;

            // Render aspects
            const aspectsContainer = document.getElementById('modal-aspects-list');
            if (aspectsContainer) {
                aspectsContainer.innerHTML = (sentiment.aspects || []).map(asp => {
                    const isAspPos = asp.score > 0;
                    return `
                        <div class="flex items-center justify-between text-xs py-1 border-b border-emerald-500/10">
                            <span class="text-zinc-300">${asp.aspect}</span>
                            <span class="font-bold font-mono ${isAspPos ? 'text-emerald-400' : 'text-rose-400'}">
                                ${isAspPos ? '+' : ''}${asp.score.toFixed(2)} (${asp.sentiment})
                            </span>
                        </div>
                    `;
                }).join('') || '<p class="text-xs text-zinc-500">No aspect consensus yet.</p>';
            }

            // Render community reviews feed
            const reviewsFeed = document.getElementById('modal-reviews-feed');
            const revCount = document.getElementById('modal-reviews-count');
            if (revCount) revCount.textContent = `${(item.reviews || []).length} Verified Reviews`;

            if (reviewsFeed) {
                reviewsFeed.innerHTML = (item.reviews || []).map(r => {
                    const s = r.sentiment_analysis;
                    const isPos = s ? s.compound_score > 0 : true;
                    return `
                        <div class="p-3 rounded-2xl bg-[#040605]/80 border border-emerald-500/15">
                            <div class="flex items-center justify-between mb-1">
                                <span class="text-xs font-bold text-zinc-200">${r.author}</span>
                                <span class="text-[10px] text-zinc-400">${r.date}</span>
                            </div>
                            <div class="flex items-center gap-1 mb-1.5 text-xs text-emerald-400">
                                ${'★'.repeat(r.rating || 5)}${'☆'.repeat(5 - (r.rating || 5))}
                                ${s ? `<span class="ml-2 text-[10px] font-bold px-2 py-0.2 rounded-full ${isPos ? 'bg-emerald-500/15 text-emerald-300' : 'bg-rose-500/15 text-rose-300'}">${s.label} (${s.dominant_emotion})</span>` : ''}
                            </div>
                            <p class="text-xs text-zinc-300 leading-relaxed">${r.text}</p>
                        </div>
                    `;
                }).join('');
            }

            modal.classList.remove('hidden');
            if (window.lucide) lucide.createIcons();
        }
    } catch (e) {
        console.error('Error opening review modal:', e);
    }
}
