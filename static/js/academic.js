/**
 * Sentix - Academic Benchmarks & Explainable AI (XAI) Dashboard
 * Emerald Obsidian & Deep Black Theme
 * Rigorous statistical NLP evaluation, 3x3 confusion matrix heatmap,
 * token-level attribution bars, and formal academic documentation.
 */

let academicData = null;
let featureWeightsData = null;

document.addEventListener('DOMContentLoaded', () => {
    initAcademicSuite();
});

function initAcademicSuite() {
    loadAcademicMetrics();
    loadFeatureWeights();
    loadAcademicCitation();
    initXAIPlayground();
    initBenchmarkButtons();
}

/* ==========================================================================
   Load Formal Benchmark Metrics
   ========================================================================== */
async function loadAcademicMetrics() {
    const runBtn = document.getElementById('btn-run-academic-benchmark');
    if (runBtn) {
        runBtn.innerHTML = '<i data-lucide="loader-2" class="w-4 h-4 animate-spin"></i> Running Evaluation...';
        runBtn.disabled = true;
    }

    try {
        const res = await fetch('/api/academic-metrics');
        const data = await res.json();
        academicData = data;

        renderAcademicSummary(data.benchmark_summary);
        renderConfusionMatrix(data.confusion_matrix, data.class_metrics);
        renderClassMetricsTable(data.class_metrics);
        renderCrossValidation(data.benchmark_summary.cross_validation_5fold);

    } catch (e) {
        console.error('Error fetching academic metrics:', e);
    } finally {
        if (runBtn) {
            runBtn.innerHTML = '<i data-lucide="play" class="w-4 h-4"></i> Run Live Benchmark Suite';
            runBtn.disabled = false;
        }
        if (window.lucide) lucide.createIcons();
    }
}

function renderAcademicSummary(summary) {
    if (!summary) return;

    const accEl = document.getElementById('academic-accuracy');
    const f1El = document.getElementById('academic-f1');
    const precEl = document.getElementById('academic-precision');
    const recEl = document.getElementById('academic-recall');
    const kappaEl = document.getElementById('academic-kappa');
    const mccEl = document.getElementById('academic-mcc');
    const latencyEl = document.getElementById('academic-latency');
    const throughputEl = document.getElementById('academic-throughput');

    if (accEl) accEl.textContent = `${(summary.accuracy * 100).toFixed(1)}%`;
    if (f1El) f1El.textContent = summary.macro_f1.toFixed(3);
    if (precEl) precEl.textContent = summary.macro_precision.toFixed(3);
    if (recEl) recEl.textContent = summary.macro_recall.toFixed(3);
    if (kappaEl) kappaEl.textContent = summary.cohen_kappa.toFixed(3);
    if (mccEl) mccEl.textContent = summary.matthews_corrcoef.toFixed(3);
    if (latencyEl) latencyEl.textContent = `${summary.mean_latency_ms.toFixed(2)} ms`;
    if (throughputEl) throughputEl.textContent = `${Math.round(summary.throughput_samples_per_sec)}/sec`;

    // Visual gauge
    const accGauge = document.getElementById('academic-accuracy-gauge');
    if (accGauge) accGauge.style.width = `${summary.accuracy * 100}%`;
}

function renderConfusionMatrix(cmData, classMetrics) {
    const container = document.getElementById('academic-confusion-matrix');
    if (!container || !cmData) return;

    const labels = cmData.labels; // ["Positive", "Neutral", "Negative"]
    const matrix = cmData.matrix;

    let html = `
        <div class="overflow-x-auto">
            <table class="w-full text-center border-collapse">
                <thead>
                    <tr>
                        <th class="p-2 text-[10px] font-bold text-zinc-500 uppercase">Actual \\ Pred</th>
                        ${labels.map(l => `<th class="p-2 text-xs font-black text-emerald-400 uppercase tracking-wider">${l}</th>`).join('')}
                        <th class="p-2 text-[10px] font-bold text-zinc-400 uppercase">Recall</th>
                    </tr>
                </thead>
                <tbody>
    `;

    for (let r = 0; r < labels.length; r++) {
        const actualLabel = labels[r];
        const rowSum = matrix[r].reduce((a, b) => a + b, 0);
        const recall = classMetrics[actualLabel] ? `${(classMetrics[actualLabel].recall * 100).toFixed(0)}%` : '-';

        html += `<tr><td class="p-2 text-xs font-black text-emerald-300 text-left border-r border-emerald-500/20">${actualLabel}</td>`;

        for (let c = 0; c < labels.length; c++) {
            const count = matrix[r][c];
            const isDiagonal = r === c;
            const pct = rowSum > 0 ? Math.round((count / rowSum) * 100) : 0;

            // Background heat styling
            let bgClass = "bg-zinc-900/60 text-zinc-400";
            if (isDiagonal) {
                if (count >= 15) bgClass = "bg-emerald-500/25 text-emerald-300 font-extrabold border border-emerald-500/40";
                else bgClass = "bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30";
            } else if (count > 0) {
                bgClass = "bg-rose-500/20 text-rose-300 font-semibold border border-rose-500/30";
            }

            html += `
                <td class="p-3">
                    <div class="p-2.5 rounded-xl ${bgClass} flex flex-col items-center justify-center transition hover:scale-105">
                        <span class="text-base">${count}</span>
                        <span class="text-[10px] opacity-75">${pct}%</span>
                    </div>
                </td>
            `;
        }

        html += `<td class="p-2 text-xs font-bold text-zinc-300 border-l border-emerald-500/20">${recall}</td></tr>`;
    }

    html += `
                </tbody>
            </table>
        </div>
    `;

    container.innerHTML = html;
}

function renderClassMetricsTable(classMetrics) {
    const tbody = document.getElementById('academic-class-metrics-tbody');
    if (!tbody || !classMetrics) return;

    tbody.innerHTML = Object.entries(classMetrics).map(([lbl, m]) => `
        <tr class="border-b border-emerald-500/10 hover:bg-emerald-500/5 transition">
            <td class="py-2.5 px-3 text-xs font-bold text-emerald-400">${lbl}</td>
            <td class="py-2.5 px-3 text-xs text-zinc-300 font-mono">${(m.precision * 100).toFixed(1)}%</td>
            <td class="py-2.5 px-3 text-xs text-zinc-300 font-mono">${(m.recall * 100).toFixed(1)}%</td>
            <td class="py-2.5 px-3 text-xs text-emerald-300 font-mono font-bold">${m.f1_score.toFixed(3)}</td>
            <td class="py-2.5 px-3 text-xs text-zinc-400 font-mono">${m.support}</td>
        </tr>
    `).join('');
}

function renderCrossValidation(cv) {
    const container = document.getElementById('academic-cv-container');
    if (!container || !cv) return;

    container.innerHTML = `
        <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold text-zinc-300">5-Fold Stratified Cross-Validation:</span>
            <span class="text-xs font-mono font-extrabold text-emerald-400">Mean: ${(cv.mean * 100).toFixed(1)}% ± ${(cv.std * 100).toFixed(1)}%</span>
        </div>
        <div class="grid grid-cols-5 gap-2">
            ${cv.folds.map((score, i) => `
                <div class="p-2 rounded-xl bg-[#040605]/80 border border-emerald-500/20 text-center">
                    <span class="text-[10px] text-zinc-500 block uppercase">Fold ${i+1}</span>
                    <span class="text-xs font-mono font-bold text-emerald-300">${(score * 100).toFixed(1)}%</span>
                </div>
            `).join('')}
        </div>
    `;
}

/* ==========================================================================
   Explainable AI (XAI) Word Attribution Tester
   ========================================================================== */
function initXAIPlayground() {
    const explainBtn = document.getElementById('btn-run-xai-explain');
    const inputEl = document.getElementById('xai-input-sentence');

    explainBtn?.addEventListener('click', () => {
        const text = inputEl?.value.trim();
        if (text) runXAIExplanation(text);
    });

    // Preset chips
    const presets = document.querySelectorAll('.xai-preset-chip');
    presets.forEach(p => {
        p.addEventListener('click', () => {
            if (inputEl) {
                inputEl.value = p.getAttribute('data-text');
                runXAIExplanation(inputEl.value);
            }
        });
    });

    // Run initial demo on start
    if (inputEl && inputEl.value.trim()) {
        runXAIExplanation(inputEl.value.trim());
    }
}

async function runXAIExplanation(text) {
    const container = document.getElementById('xai-tokens-container');
    const scoreBadge = document.getElementById('xai-compound-score');
    const labelBadge = document.getElementById('xai-label-badge');
    if (!container) return;

    container.innerHTML = `
        <div class="py-8 flex items-center justify-center text-emerald-400 text-xs">
            <div class="animate-spin w-5 h-5 border-2 border-emerald-500 border-t-transparent rounded-full mr-2"></div>
            Decomposing lexical valence vectors...
        </div>
    `;

    try {
        const res = await fetch('/api/academic-explain', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await res.json();

        if (scoreBadge) scoreBadge.textContent = `${data.compound > 0 ? '+' : ''}${data.compound.toFixed(3)}`;
        if (labelBadge) {
            labelBadge.textContent = data.label;
            labelBadge.className = `px-2.5 py-0.5 rounded-full text-xs font-black ${
                data.compound > 0.05 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' :
                (data.compound < -0.05 ? 'bg-rose-500/20 text-rose-400 border border-rose-500/40' : 'bg-zinc-800 text-zinc-300')
            }`;
        }

        renderXAITokens(data.tokens);

    } catch (e) {
        console.error('Error running XAI explanation:', e);
        container.innerHTML = '<div class="py-4 text-xs text-rose-400">Failed to generate explanation.</div>';
    }
}

function renderXAITokens(tokens) {
    const container = document.getElementById('xai-tokens-container');
    if (!container) return;

    container.innerHTML = '';

    if (!tokens || tokens.length === 0) {
        container.innerHTML = '<div class="text-xs text-zinc-500">No tokens analyzed.</div>';
        return;
    }

    const grid = document.createElement('div');
    grid.className = "flex flex-wrap gap-2.5 items-center";

    tokens.forEach(tok => {
        const isPos = tok.direction === 'positive';
        const isNeg = tok.direction === 'negative';

        let badgeBg = "bg-[#040605]/80 border-zinc-800 text-zinc-400";
        let barBg = "bg-zinc-600";
        if (isPos) {
            badgeBg = "bg-emerald-500/10 border-emerald-500/40 text-emerald-300 font-bold";
            barBg = "bg-gradient-to-r from-emerald-500 to-green-400";
        } else if (isNeg) {
            badgeBg = "bg-rose-500/10 border-rose-500/40 text-rose-300 font-bold";
            barBg = "bg-gradient-to-r from-rose-500 to-red-400";
        }

        const chip = document.createElement('div');
        chip.className = `p-2 rounded-xl border ${badgeBg} flex flex-col min-w-[70px] shadow-sm transition hover:scale-105`;
        chip.innerHTML = `
            <div class="flex items-center justify-between text-[11px] mb-1">
                <span>${tok.word}</span>
                <span class="text-[9px] font-mono opacity-80">${tok.score > 0 ? '+' : ''}${tok.score.toFixed(1)}</span>
            </div>
            <div class="w-full h-1.5 rounded-full bg-zinc-800 overflow-hidden">
                <div class="h-full ${barBg}" style="width: ${tok.bar_percent}%"></div>
            </div>
            <span class="text-[8px] uppercase tracking-wider text-zinc-500 mt-1">${tok.role}</span>
        `;
        grid.appendChild(chip);
    });

    container.appendChild(grid);
}

/* ==========================================================================
   Feature Weights & Discriminative N-Grams
   ========================================================================== */
async function loadFeatureWeights() {
    try {
        const res = await fetch('/api/academic-features');
        const data = await res.json();
        featureWeightsData = data;

        const posList = document.getElementById('academic-top-positive-features');
        const negList = document.getElementById('academic-top-negative-features');

        if (posList && data.top_positive) {
            posList.innerHTML = data.top_positive.map(f => `
                <div class="flex items-center justify-between p-2 rounded-xl bg-emerald-500/5 border border-emerald-500/15">
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        <span class="text-xs font-bold text-emerald-300">"${f.feature}"</span>
                        <span class="text-[9px] text-zinc-500 uppercase">${f.type}</span>
                    </div>
                    <span class="font-mono text-xs font-bold text-emerald-400">+${f.weight.toFixed(2)}</span>
                </div>
            `).join('');
        }

        if (negList && data.top_negative) {
            negList.innerHTML = data.top_negative.map(f => `
                <div class="flex items-center justify-between p-2 rounded-xl bg-rose-500/5 border border-rose-500/15">
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                        <span class="text-xs font-bold text-rose-300">"${f.feature}"</span>
                        <span class="text-[9px] text-zinc-500 uppercase">${f.type}</span>
                    </div>
                    <span class="font-mono text-xs font-bold text-rose-400">${f.weight.toFixed(2)}</span>
                </div>
            `).join('');
        }

    } catch (e) {
        console.error('Error loading feature weights:', e);
    }
}

/* ==========================================================================
   Citation & Export Handlers
   ========================================================================== */
async function loadAcademicCitation() {
    try {
        const res = await fetch('/api/academic-citation');
        const data = await res.json();

        const bibtexEl = document.getElementById('academic-bibtex-block');
        if (bibtexEl) bibtexEl.textContent = data.bibtex;

    } catch (e) {
        console.error('Error loading citation:', e);
    }
}

function initBenchmarkButtons() {
    const runBtn = document.getElementById('btn-run-academic-benchmark');
    runBtn?.addEventListener('click', () => {
        loadAcademicMetrics();
    });

    const copyBibtexBtn = document.getElementById('btn-copy-bibtex');
    copyBibtexBtn?.addEventListener('click', () => {
        const code = document.getElementById('academic-bibtex-block')?.textContent;
        if (code) {
            navigator.clipboard.writeText(code).then(() => {
                copyBibtexBtn.innerHTML = '<i data-lucide="check" class="w-3.5 h-3.5 text-emerald-400"></i> Copied to Clipboard!';
                setTimeout(() => {
                    copyBibtexBtn.innerHTML = '<i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy BibTeX';
                    if (window.lucide) lucide.createIcons();
                }, 2000);
            });
        }
    });

    const exportJsonBtn = document.getElementById('btn-export-academic-json');
    exportJsonBtn?.addEventListener('click', () => {
        if (!academicData) return;
        const blob = new Blob([JSON.stringify(academicData, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `sentix_academic_evaluation_report_${Date.now()}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });
}
