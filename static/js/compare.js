/**
 * Sentix - Side-by-Side Comparison Module
 */

const COMPARE_PRESETS = [
    {
        name: "Product V1 vs Product V2",
        labelA: "Product V1",
        textA: "The initial release was clunky, battery drained fast, and the interface crashed frequently during file export.",
        labelB: "Product V2",
        textB: "The new updated version is exceptionally smooth, battery life doubled, and the team fixed all export bugs flawlessly! 🚀"
    },
    {
        name: "Brand A vs Competitor B",
        labelA: "Brand A",
        textA: "Great customer service and fast shipping, but the pricing is rather high compared to market averages.",
        labelB: "Competitor B",
        textB: "Incredible value for money, generous discount codes, and the product durability is second to none!"
    }
];

document.addEventListener('DOMContentLoaded', () => {
    initCompareModule();
});

function initCompareModule() {
    const compareBtn = document.getElementById('btn-run-compare');
    const presetsContainer = document.getElementById('compare-presets-container');

    if (presetsContainer) {
        COMPARE_PRESETS.forEach(p => {
            const btn = document.createElement('button');
            btn.className = "text-xs px-3 py-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white/60 dark:bg-slate-800/60 hover:bg-indigo-50 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 transition flex items-center gap-1.5 shadow-sm";
            btn.innerHTML = `<span class="w-2 h-2 rounded-full bg-violet-500"></span> ${p.name}`;
            btn.addEventListener('click', () => {
                document.getElementById('compare-label-a').value = p.labelA;
                document.getElementById('compare-text-a').value = p.textA;
                document.getElementById('compare-label-b').value = p.labelB;
                document.getElementById('compare-text-b').value = p.textB;
                runComparison();
            });
            presetsContainer.appendChild(btn);
        });
    }

    compareBtn?.addEventListener('click', runComparison);
}

async function runComparison() {
    const textA = document.getElementById('compare-text-a')?.value.trim();
    const textB = document.getElementById('compare-text-b')?.value.trim();
    const labelA = document.getElementById('compare-label-a')?.value.trim() || 'Item A';
    const labelB = document.getElementById('compare-label-b')?.value.trim() || 'Item B';

    if (!textA || !textB) {
        alert('Please provide text for both sides to compare.');
        return;
    }

    const btn = document.getElementById('btn-run-compare');
    if (btn) btn.disabled = true;

    try {
        const res = await fetch('/api/compare', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                text_a: textA,
                text_b: textB,
                label_a: labelA,
                label_b: labelB
            })
        });

        const json = await res.json();
        if (json.success) {
            renderCompareResults(json.comparison);
        } else {
            alert('Comparison failed: ' + json.error);
        }
    } catch (e) {
        console.error('Comparison error:', e);
    } finally {
        if (btn) btn.disabled = false;
    }
}

function renderCompareResults(comp) {
    const resultsContainer = document.getElementById('compare-results-container');
    if (!resultsContainer) return;
    resultsContainer.classList.remove('hidden');

    const resA = comp.analysis_a;
    const resB = comp.analysis_b;

    // Delta banner
    const deltaElem = document.getElementById('compare-delta-banner');
    if (deltaElem) {
        const delta = comp.delta_compound;
        const higher = comp.higher_sentiment;
        const isBetter = delta > 0;
        deltaElem.className = `p-4 rounded-2xl border text-center ${
            delta === 0 ? 'bg-zinc-800 border-zinc-700' :
            (delta > 0 ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-400' :
                         'bg-rose-500/15 border-rose-500/40 text-rose-400')
        }`;
        deltaElem.innerHTML = `
            <h4 class="font-bold text-base">
                ${delta === 0 ? 'Both texts exhibit identical sentiment valence.' : `<strong>${higher}</strong> has a higher sentiment score by <strong>${Math.abs(delta).toFixed(2)}</strong> points.`}
            </h4>
            <p class="text-xs mt-1 text-slate-500 dark:text-slate-400">
                ${comp.label_a}: ${(resA.overall.compound_score > 0 ? '+' : '') + resA.overall.compound_score.toFixed(2)} vs ${comp.label_b}: ${(resB.overall.compound_score > 0 ? '+' : '') + resB.overall.compound_score.toFixed(2)}
            </p>
        `;
    }

    // Render Column A
    renderSideCard('side-a', comp.label_a, resA);
    // Render Column B
    renderSideCard('side-b', comp.label_b, resB);

    if (window.lucide) lucide.createIcons();
}

function renderSideCard(prefix, label, analysis) {
    const titleElem = document.getElementById(`${prefix}-title`);
    const badgeElem = document.getElementById(`${prefix}-badge`);
    const scoreElem = document.getElementById(`${prefix}-score`);
    const emotionElem = document.getElementById(`${prefix}-emotion`);
    const aspectsContainer = document.getElementById(`${prefix}-aspects`);

    if (titleElem) titleElem.innerText = label;
    if (badgeElem) {
        badgeElem.innerText = analysis.overall.label;
        badgeElem.style.backgroundColor = analysis.overall.theme_color + '22';
        badgeElem.style.color = analysis.overall.theme_color;
    }
    if (scoreElem) {
        scoreElem.innerText = (analysis.overall.compound_score > 0 ? '+' : '') + analysis.overall.compound_score.toFixed(2);
        scoreElem.style.color = analysis.overall.theme_color;
    }
    if (emotionElem) {
        emotionElem.innerText = analysis.emotions.dominant;
    }

    if (aspectsContainer) {
        aspectsContainer.innerHTML = '';
        if (analysis.aspects && analysis.aspects.length > 0) {
            analysis.aspects.forEach(asp => {
                const isPos = asp.sentiment === 'Positive';
                const tag = document.createElement('span');
                tag.className = `text-[11px] px-2 py-0.5 rounded-full font-medium ${isPos ? 'bg-emerald-100 dark:bg-emerald-900/40 text-emerald-700 dark:text-emerald-300' : 'bg-rose-100 dark:bg-rose-900/40 text-rose-700 dark:text-rose-300'}`;
                tag.innerText = `${asp.aspect}: ${asp.sentiment}`;
                aspectsContainer.appendChild(tag);
            });
        } else {
            aspectsContainer.innerHTML = '<span class="text-xs text-slate-400">No specific aspects</span>';
        }
    }
}
