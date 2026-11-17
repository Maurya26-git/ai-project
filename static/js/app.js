/**
 * Sentix - Main Application Logic & Single Text Analysis
 * Luxury Gold & Obsidian Dark Edition
 */

let emotionChart = null;
let liveAnalysisTimeout = null;
let currentPresets = [];

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initTabNavigation();
    initPresets();
    initLiveAnalyzer();
    initGeminiModal();
    initHistory();
});

/* ==========================================================================
   Theme Management (Luxury Obsidian Dark / Warm Champagne Light)
   ========================================================================== */
function initTheme() {
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const savedTheme = localStorage.getItem('sentix_theme') || 
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'dark'); // Default to dark for luxury feel

    if (savedTheme === 'dark') {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
    updateThemeIcon(savedTheme === 'dark');

    themeToggleBtn?.addEventListener('click', () => {
        const isDark = document.documentElement.classList.toggle('dark');
        localStorage.setItem('sentix_theme', isDark ? 'dark' : 'light');
        updateThemeIcon(isDark);
        if (emotionChart) emotionChart.update();
    });
}

function updateThemeIcon(isDark) {
    const iconContainer = document.getElementById('theme-toggle-icon');
    if (!iconContainer) return;
    iconContainer.innerHTML = isDark 
        ? '<i data-lucide="sun" class="w-4 h-4 text-emerald-400"></i>' 
        : '<i data-lucide="moon" class="w-4 h-4 text-emerald-600"></i>';
    if (window.lucide) lucide.createIcons();
}

/* ==========================================================================
   Tab Navigation
   ========================================================================== */
function initTabNavigation() {
    const tabButtons = document.querySelectorAll('.nav-tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-tab');

            tabButtons.forEach(b => {
                b.classList.remove('active', 'border-emerald-500', 'text-emerald-500', 'dark:text-emerald-400', 'dark:border-emerald-400');
                b.classList.add('border-transparent', 'text-slate-500', 'dark:text-zinc-400');
            });

            btn.classList.add('active', 'border-emerald-500', 'text-emerald-500', 'dark:text-emerald-400', 'dark:border-emerald-400');
            btn.classList.remove('border-transparent', 'text-slate-500', 'dark:text-zinc-400');

            tabPanes.forEach(pane => {
                if (pane.id === targetId) {
                    pane.classList.remove('hidden');
                } else {
                    pane.classList.add('hidden');
                }
            });

            if (window.lucide) lucide.createIcons();
            if (targetId === 'tab-batch' && window.batchSentimentChart) {
                window.batchSentimentChart.resize();
            }
        });
    });
}

/* ==========================================================================
   Presets & Sample Texts
   ========================================================================== */
async function initPresets() {
    const container = document.getElementById('preset-pills-container');
    if (!container) return;

    try {
        const res = await fetch('/api/samples');
        const data = await res.json();
        if (data.success && data.single_presets) {
            currentPresets = data.single_presets;
            renderPresetPills(currentPresets);
        }
    } catch (err) {
        console.error('Failed to load sample presets:', err);
    }
}

function renderPresetPills(presets) {
    const container = document.getElementById('preset-pills-container');
    if (!container) return;
    container.innerHTML = '';

    presets.forEach(p => {
        const btn = document.createElement('button');
        btn.className = "text-xs px-3 py-1.5 rounded-full border border-emerald-500/25 dark:border-emerald-500/30 bg-white/70 dark:bg-zinc-900/80 hover:bg-emerald-500/15 text-slate-800 dark:text-zinc-200 transition flex items-center gap-1.5 shadow-sm";
        btn.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400"></span> ${p.title}`;
        btn.addEventListener('click', () => {
            const input = document.getElementById('sentiment-text-input');
            if (input) {
                input.value = p.text;
                updateCharWordCounts();
                triggerAnalysis(p.title);
            }
        });
        container.appendChild(btn);
    });
}

/* ==========================================================================
   Live Analyzer
   ========================================================================== */
function initLiveAnalyzer() {
    const textInput = document.getElementById('sentiment-text-input');
    const analyzeBtn = document.getElementById('btn-analyze-now');
    const clearBtn = document.getElementById('btn-clear-text');
    const autoAnalyzeCheckbox = document.getElementById('chk-auto-analyze');

    textInput?.addEventListener('input', () => {
        updateCharWordCounts();
        if (autoAnalyzeCheckbox?.checked) {
            clearTimeout(liveAnalysisTimeout);
            liveAnalysisTimeout = setTimeout(() => {
                triggerAnalysis();
            }, 400);
        }
    });

    analyzeBtn?.addEventListener('click', () => {
        triggerAnalysis();
    });

    clearBtn?.addEventListener('click', () => {
        if (textInput) {
            textInput.value = '';
            updateCharWordCounts();
            resetResultsUI();
        }
    });

    if (textInput && textInput.value.trim().length > 0) {
        updateCharWordCounts();
        triggerAnalysis();
    }
}

window.updateCharWordCounts = function() {
    const text = document.getElementById('sentiment-text-input')?.value || '';
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    const chars = text.length;

    const countElem = document.getElementById('word-char-counter');
    if (countElem) {
        countElem.innerText = `${words} words · ${chars} characters`;
    }
};

window.triggerAnalysis = async function(sourceName = null) {
    const textInput = document.getElementById('sentiment-text-input');
    const text = textInput?.value.trim();
    if (!text) {
        resetResultsUI();
        return;
    }

    const analyzeBtn = document.getElementById('btn-analyze-now');
    const loadingSpinner = document.getElementById('live-spinner');

    if (analyzeBtn) analyzeBtn.disabled = true;
    if (loadingSpinner) loadingSpinner.classList.remove('hidden');

    const geminiKey = localStorage.getItem('sentix_gemini_key') || '';

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                text: text,
                gemini_api_key: geminiKey
            })
        });

        const json = await response.json();
        if (json.success && json.data) {
            renderAnalysisResults(json.data);
            saveToHistory(json.data, sourceName);
        } else {
            console.error('Analysis error:', json.error);
        }
    } catch (err) {
        console.error('Network error during analysis:', err);
    } finally {
        if (analyzeBtn) analyzeBtn.disabled = false;
        if (loadingSpinner) loadingSpinner.classList.add('hidden');
    }
};

/* ==========================================================================
   Render Analysis Results
   ========================================================================== */
function renderAnalysisResults(data) {
    const resultsContainer = document.getElementById('analysis-results-container');
    const placeholder = document.getElementById('analysis-placeholder');

    if (placeholder) placeholder.classList.add('hidden');
    if (resultsContainer) resultsContainer.classList.remove('hidden');

    const overall = data.overall;
    const compound = overall.compound_score;

    // 1. Overall Label and theme badge
    const badgeElem = document.getElementById('result-sentiment-badge');
    if (badgeElem) {
        badgeElem.innerText = overall.label;
        badgeElem.style.backgroundColor = overall.theme_color + '22';
        badgeElem.style.color = overall.theme_color;
        badgeElem.style.borderColor = overall.theme_color + '77';
    }

    // 2. Compound Score & Confidence
    const compoundElem = document.getElementById('result-compound-score');
    if (compoundElem) {
        compoundElem.innerText = (compound > 0 ? '+' : '') + compound.toFixed(2);
        compoundElem.style.color = overall.theme_color;
    }

    const confElem = document.getElementById('result-confidence-percent');
    if (confElem) {
        confElem.innerText = `${overall.confidence_percent}%`;
    }

    // 3. Gauge Needle rotation
    const needle = document.getElementById('gauge-needle');
    if (needle) {
        const deg = Math.max(-90, Math.min(90, compound * 90));
        needle.style.transform = `rotate(${deg}deg)`;
        needle.style.backgroundColor = overall.theme_color;
    }

    // 4. Sub-scores
    const posBar = document.getElementById('bar-pos-score');
    const neuBar = document.getElementById('bar-neu-score');
    const negBar = document.getElementById('bar-neg-score');
    const posText = document.getElementById('text-pos-score');
    const neuText = document.getElementById('text-neu-score');
    const negText = document.getElementById('text-neg-score');

    if (posBar) posBar.style.width = `${Math.round(overall.positive_score * 100)}%`;
    if (neuBar) neuBar.style.width = `${Math.round(overall.neutral_score * 100)}%`;
    if (negBar) negBar.style.width = `${Math.round(overall.negative_score * 100)}%`;

    if (posText) posText.innerText = `${Math.round(overall.positive_score * 100)}%`;
    if (neuText) neuText.innerText = `${Math.round(overall.neutral_score * 100)}%`;
    if (negText) negText.innerText = `${Math.round(overall.negative_score * 100)}%`;

    const subjElem = document.getElementById('text-subjectivity-score');
    const subjBar = document.getElementById('bar-subjectivity-score');
    if (subjElem) subjElem.innerText = `${Math.round(overall.subjectivity * 100)}% (${overall.subjectivity > 0.5 ? 'Subjective' : 'Objective'})`;
    if (subjBar) subjBar.style.width = `${Math.round(overall.subjectivity * 100)}%`;

    // 5. ML Model Validation Badge
    const mlBadge = document.getElementById('ml-prediction-badge');
    if (mlBadge && data.ml_model) {
        mlBadge.innerText = `ML Model: ${data.ml_model.label} (${Math.round(data.ml_model.confidence * 100)}%)`;
    }

    // 6. Token Highlighter
    renderTokenHighlighting(data.tokens);

    // 7. Aspect-Based Sentiment Analysis (ABSA)
    renderAspects(data.aspects);

    // 8. Emotion Radar Chart
    renderEmotionChart(data.emotions);

    // 9. Tone & Sarcasm Tags
    renderToneTags(data.tone_descriptors, data.sarcasm_detected);

    // 10. Gemini LLM Insights
    renderGeminiInsights(data.gemini_insights);

    if (window.lucide) lucide.createIcons();
}

function renderTokenHighlighting(tokens) {
    const container = document.getElementById('token-highlight-container');
    if (!container) return;
    container.innerHTML = '';

    if (!tokens || tokens.length === 0) {
        container.innerHTML = '<span class="text-slate-400 text-sm">No tokens available.</span>';
        return;
    }

    tokens.forEach(tok => {
        const span = document.createElement('span');
        span.className = `token-chip token-${tok.type}`;
        span.innerText = tok.text;
        span.title = tok.tooltip || tok.type;
        container.appendChild(span);
        container.appendChild(document.createTextNode(' '));
    });
}

function renderAspects(aspects) {
    const container = document.getElementById('aspects-container');
    const countBadge = document.getElementById('aspects-count-badge');
    if (!container) return;
    container.innerHTML = '';

    if (countBadge) {
        countBadge.innerText = `${aspects ? aspects.length : 0} detected`;
    }

    if (!aspects || aspects.length === 0) {
        container.innerHTML = `
            <div class="col-span-full py-4 text-center text-slate-400 text-sm italic">
                General sentiment applies across the entire text. No single isolated aspect detected.
            </div>
        `;
        return;
    }

    aspects.forEach(asp => {
        const isPos = asp.sentiment === 'Positive';
        const isNeg = asp.sentiment === 'Negative';
        const colorClass = isPos 
            ? 'border-emerald-500/30 bg-emerald-500/10 text-emerald-400' 
            : (isNeg 
                ? 'border-rose-500/30 bg-rose-500/10 text-rose-400' 
                : 'border-zinc-700 bg-zinc-800 text-zinc-300');

        const card = document.createElement('div');
        card.className = `p-3 rounded-2xl border ${colorClass} transition flex flex-col justify-between`;
        card.innerHTML = `
            <div class="flex items-center justify-between gap-2 mb-1">
                <span class="font-bold text-xs">${asp.aspect}</span>
                <span class="text-[10px] px-2 py-0.5 rounded-full font-bold ${isPos ? 'bg-emerald-400/20 text-emerald-300 border border-emerald-400/30' : (isNeg ? 'bg-rose-400/20 text-rose-300 border border-rose-400/30' : 'bg-zinc-700 text-zinc-300')}">
                    ${asp.sentiment} (${(asp.score > 0 ? '+' : '') + asp.score.toFixed(2)})
                </span>
            </div>
            <p class="text-xs text-slate-400 dark:text-zinc-400 truncate" title="${asp.clause}">"${asp.clause}"</p>
        `;
        container.appendChild(card);
    });
}

function renderEmotionChart(emotionsData) {
    const canvas = document.getElementById('emotionRadarChart');
    if (!canvas) return;

    const dominantElem = document.getElementById('dominant-emotion-text');
    if (dominantElem) {
        dominantElem.innerText = emotionsData.dominant;
        dominantElem.style.color = emotionsData.dominant_color;
    }

    const labels = emotionsData.breakdown.map(e => e.emotion);
    const scores = emotionsData.breakdown.map(e => e.percentage);

    const isDark = document.documentElement.classList.contains('dark');
    const gridColor = isDark ? 'rgba(245, 158, 11, 0.12)' : 'rgba(217, 119, 6, 0.16)';
    const textColor = isDark ? '#fbbf24' : '#b45309';

    if (emotionChart) {
        emotionChart.destroy();
    }

    const ctx = canvas.getContext('2d');
    emotionChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Emotion %',
                data: scores,
                backgroundColor: 'rgba(245, 158, 11, 0.22)',
                borderColor: '#f59e0b',
                pointBackgroundColor: '#fbbf24',
                pointBorderColor: '#ffffff',
                borderWidth: 2,
                pointRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    angleLines: { color: gridColor },
                    grid: { color: gridColor },
                    pointLabels: {
                        color: textColor,
                        font: { size: 11, weight: '600' }
                    },
                    ticks: {
                        display: false,
                        maxTicksLimit: 5
                    },
                    suggestedMin: 0,
                    suggestedMax: 80
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}

function renderToneTags(tones, sarcasmDetected) {
    const container = document.getElementById('tone-tags-container');
    if (!container) return;
    container.innerHTML = '';

    if (sarcasmDetected) {
        const sarcasmPill = document.createElement('span');
        sarcasmPill.className = "px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 flex items-center gap-1";
        sarcasmPill.innerHTML = '<i data-lucide="alert-triangle" class="w-3.5 h-3.5"></i> Sarcasm Detected';
        container.appendChild(sarcasmPill);
    }

    tones.forEach(t => {
        const pill = document.createElement('span');
        pill.className = "px-2.5 py-1 rounded-full text-xs font-semibold bg-zinc-100 dark:bg-zinc-800 text-slate-800 dark:text-zinc-200 border border-emerald-500/20";
        pill.innerText = t;
        container.appendChild(pill);
    });
}

function renderGeminiInsights(geminiData) {
    const container = document.getElementById('gemini-insights-container');
    if (!container) return;

    if (!geminiData || !geminiData.enabled) {
        container.innerHTML = `
            <div class="p-4 rounded-2xl border border-emerald-500/30 bg-emerald-500/10 text-slate-700 dark:text-zinc-300 text-xs flex items-center justify-between">
                <div class="flex items-center gap-2">
                    <i data-lucide="sparkles" class="w-4 h-4 text-emerald-400"></i>
                    <span>Connect your <strong>Gemini API Key</strong> for executive insights & deep LLM reasoning.</span>
                </div>
                <button onclick="openGeminiModal()" class="px-3 py-1 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold text-xs transition">
                    Configure
                </button>
            </div>
        `;
        return;
    }

    let insightsHtml = `
        <div class="p-5 rounded-2xl border border-emerald-500/40 bg-gradient-to-br from-emerald-500/10 via-zinc-900/90 to-zinc-950 text-zinc-200">
            <div class="flex items-center justify-between mb-3">
                <div class="flex items-center gap-2">
                    <i data-lucide="sparkles" class="w-5 h-5 text-emerald-400"></i>
                    <h4 class="font-extrabold text-sm text-emerald-400">Gemini LLM Executive Summary</h4>
                </div>
                <span class="text-xs px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30">
                    ${geminiData.confidence_percentage}% Confidence
                </span>
            </div>
            <p class="text-xs leading-relaxed mb-3 text-zinc-300">${geminiData.executive_summary || ''}</p>
    `;

    if (geminiData.actionable_insights && geminiData.actionable_insights.length > 0) {
        insightsHtml += `
            <div class="mt-3 pt-3 border-t border-emerald-500/20">
                <h5 class="text-xs font-bold text-emerald-300 mb-1.5 flex items-center gap-1.5">
                    <i data-lucide="check-circle" class="w-3.5 h-3.5 text-emerald-400"></i> Actionable Takeaways:
                </h5>
                <ul class="list-disc list-inside space-y-1 text-xs text-zinc-400">
                    ${geminiData.actionable_insights.map(i => `<li>${i}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    insightsHtml += `</div>`;
    container.innerHTML = insightsHtml;
}

function resetResultsUI() {
    const resultsContainer = document.getElementById('analysis-results-container');
    const placeholder = document.getElementById('analysis-placeholder');

    if (resultsContainer) resultsContainer.classList.add('hidden');
    if (placeholder) placeholder.classList.remove('hidden');
}

/* ==========================================================================
   Gemini API Key Modal
   ========================================================================== */
function initGeminiModal() {
    const modal = document.getElementById('gemini-key-modal');
    const input = document.getElementById('gemini-api-key-input');
    const saveBtn = document.getElementById('btn-save-gemini-key');
    const closeBtn = document.getElementById('btn-close-gemini-modal');
    const removeBtn = document.getElementById('btn-remove-gemini-key');

    const savedKey = localStorage.getItem('sentix_gemini_key') || '';
    if (input) input.value = savedKey;

    saveBtn?.addEventListener('click', () => {
        const val = input?.value.trim() || '';
        if (val) {
            localStorage.setItem('sentix_gemini_key', val);
            alert('Gemini API key saved successfully!');
            modal?.classList.add('hidden');
            triggerAnalysis();
        }
    });

    removeBtn?.addEventListener('click', () => {
        localStorage.removeItem('sentix_gemini_key');
        if (input) input.value = '';
        alert('Gemini API key removed.');
        modal?.classList.add('hidden');
        triggerAnalysis();
    });

    closeBtn?.addEventListener('click', () => {
        modal?.classList.add('hidden');
    });
}

window.openGeminiModal = function() {
    const modal = document.getElementById('gemini-key-modal');
    modal?.classList.remove('hidden');
};

/* ==========================================================================
   History Tracking (with Gold Badges & Item Tagging)
   ========================================================================== */
function initHistory() {
    renderHistoryList();
    const clearHistoryBtn = document.getElementById('btn-clear-history');
    clearHistoryBtn?.addEventListener('click', () => {
        if (confirm('Are you sure you want to clear your analysis history?')) {
            localStorage.removeItem('sentix_history');
            renderHistoryList();
        }
    });
}

function saveToHistory(resultData, itemName = null) {
    try {
        let history = JSON.parse(localStorage.getItem('sentix_history') || '[]');
        const entry = {
            id: Date.now(),
            itemName: itemName || null,
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
            text: resultData.text.slice(0, 110) + (resultData.text.length > 110 ? '...' : ''),
            fullText: resultData.text,
            label: resultData.overall.label,
            compound: resultData.overall.compound_score,
            color: resultData.overall.theme_color,
            emotion: resultData.emotions.dominant
        };

        history.unshift(entry);
        if (history.length > 40) history = history.slice(0, 40);
        localStorage.setItem('sentix_history', JSON.stringify(history));

        renderHistoryList();
    } catch (e) {
        console.error('Error saving history:', e);
    }
}

window.saveCustomReviewToHistory = function(resultData, itemName = null) {
    saveToHistory(resultData, itemName);
};

function renderHistoryList() {
    const container = document.getElementById('history-items-container');
    const emptyState = document.getElementById('history-empty-state');
    if (!container) return;

    const history = JSON.parse(localStorage.getItem('sentix_history') || '[]');

    if (history.length === 0) {
        if (emptyState) emptyState.classList.remove('hidden');
        container.innerHTML = '';
        return;
    }

    if (emptyState) emptyState.classList.add('hidden');
    container.innerHTML = '';

    history.forEach(item => {
        const row = document.createElement('div');
        row.className = "p-3.5 rounded-2xl border border-emerald-500/20 dark:border-emerald-500/25 bg-white/80 dark:bg-zinc-900/80 hover:border-emerald-500/50 transition cursor-pointer flex items-center justify-between gap-4 shadow-sm";
        row.innerHTML = `
            <div class="flex-1 min-w-0">
                <div class="flex items-center gap-2 mb-1">
                    ${item.itemName ? `<span class="text-[10px] px-2 py-0.5 rounded-full font-black bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 flex items-center gap-1"><i data-lucide="check-circle" class="w-3 h-3 text-emerald-400"></i> ${item.itemName}</span>` : ''}
                    <span class="text-[10px] text-zinc-400">${item.timestamp}</span>
                </div>
                <p class="text-xs text-slate-800 dark:text-zinc-200 truncate font-semibold">"${item.text}"</p>
                <div class="flex items-center gap-2 mt-1.5">
                    <span class="text-[10px] px-2 py-0.5 rounded-full font-bold" style="background-color: ${item.color}22; color: ${item.color}; border: 1px solid ${item.color}55">
                        ${item.label} (${(item.compound > 0 ? '+' : '') + item.compound.toFixed(2)})
                    </span>
                    <span class="text-[10px] text-zinc-400 font-medium">Dominant Emotion: <strong class="text-emerald-400">${item.emotion}</strong></span>
                </div>
            </div>
            <button class="text-xs px-3 py-1.5 rounded-xl bg-emerald-500/15 hover:bg-emerald-500 text-emerald-400 hover:text-slate-950 font-bold border border-emerald-500/30 transition flex items-center gap-1.5 flex-shrink-0">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i> Reload
            </button>
        `;
        row.addEventListener('click', () => {
            const input = document.getElementById('sentiment-text-input');
            if (input) {
                input.value = item.fullText;
                updateCharWordCounts();
                document.querySelector('[data-tab="tab-live"]')?.click();
                triggerAnalysis(item.itemName);
            }
        });
        container.appendChild(row);
    });

    if (window.lucide) lucide.createIcons();
}
