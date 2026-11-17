/**
 * Sentix - Batch & Dataset Analysis Engine
 */

let batchSentimentChart = null;
let batchEmotionChart = null;
let batchAllResults = [];
let batchCurrentPage = 1;
const ROWS_PER_PAGE = 8;

document.addEventListener('DOMContentLoaded', () => {
    initBatchHandlers();
});

function initBatchHandlers() {
    const fileInput = document.getElementById('batch-file-input');
    const dropZone = document.getElementById('batch-drop-zone');
    const demoBtn = document.getElementById('btn-load-demo-batch');
    const searchInput = document.getElementById('batch-table-search');
    const filterSelect = document.getElementById('batch-filter-sentiment');
    const exportCsvBtn = document.getElementById('btn-export-csv');
    const exportJsonBtn = document.getElementById('btn-export-json');

    dropZone?.addEventListener('click', () => fileInput?.click());

    dropZone?.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('border-indigo-500', 'bg-indigo-50/50', 'dark:bg-indigo-950/20');
    });

    dropZone?.addEventListener('dragleave', () => {
        dropZone.classList.remove('border-indigo-500', 'bg-indigo-50/50', 'dark:bg-indigo-950/20');
    });

    dropZone?.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('border-indigo-500', 'bg-indigo-50/50', 'dark:bg-indigo-950/20');
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            handleFileUpload(e.dataTransfer.files[0]);
        }
    });

    fileInput?.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
            handleFileUpload(e.target.files[0]);
        }
    });

    demoBtn?.addEventListener('click', async () => {
        loadDemoBatchData();
    });

    searchInput?.addEventListener('input', () => {
        batchCurrentPage = 1;
        renderBatchTable();
    });

    filterSelect?.addEventListener('change', () => {
        batchCurrentPage = 1;
        renderBatchTable();
    });

    exportCsvBtn?.addEventListener('click', exportBatchToCSV);
    exportJsonBtn?.addEventListener('click', exportBatchToJSON);
}

async function handleFileUpload(file) {
    const formData = new FormData();
    formData.append('file', file);

    const progressBox = document.getElementById('batch-progress-box');
    const progressBar = document.getElementById('batch-progress-bar');
    const statusText = document.getElementById('batch-status-text');

    if (progressBox) progressBox.classList.remove('hidden');
    if (progressBar) progressBar.style.width = '35%';
    if (statusText) statusText.innerText = `Parsing & analyzing ${file.name}...`;

    try {
        const response = await fetch('/api/batch', {
            method: 'POST',
            body: formData
        });

        if (progressBar) progressBar.style.width = '85%';
        const json = await response.json();

        if (json.success) {
            if (progressBar) progressBar.style.width = '100%';
            setTimeout(() => {
                if (progressBox) progressBox.classList.add('hidden');
                displayBatchResults(json.summary, json.results);
            }, 300);
        } else {
            alert('Batch processing failed: ' + json.error);
            if (progressBox) progressBox.classList.add('hidden');
        }
    } catch (err) {
        console.error('Batch upload error:', err);
        alert('Network or server error processing batch.');
        if (progressBox) progressBox.classList.add('hidden');
    }
}

async function loadDemoBatchData() {
    const progressBox = document.getElementById('batch-progress-box');
    const progressBar = document.getElementById('batch-progress-bar');
    const statusText = document.getElementById('batch-status-text');

    if (progressBox) progressBox.classList.remove('hidden');
    if (progressBar) progressBar.style.width = '40%';
    if (statusText) statusText.innerText = 'Loading pre-configured multi-channel review dataset...';

    try {
        const res = await fetch('/api/samples');
        const data = await res.json();
        
        if (data.success && data.batch_sample) {
            if (progressBar) progressBar.style.width = '70%';
            
            // Send items to batch endpoint
            const batchRes = await fetch('/api/batch', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ items: data.batch_sample })
            });

            const batchJson = await batchRes.json();
            if (batchJson.success) {
                if (progressBar) progressBar.style.width = '100%';
                setTimeout(() => {
                    if (progressBox) progressBox.classList.add('hidden');
                    displayBatchResults(batchJson.summary, batchJson.results);
                }, 300);
            }
        }
    } catch (err) {
        console.error('Failed to load demo batch:', err);
        if (progressBox) progressBox.classList.add('hidden');
    }
}

function displayBatchResults(summary, results) {
    batchAllResults = results;
    batchCurrentPage = 1;

    const resultsArea = document.getElementById('batch-results-area');
    if (resultsArea) resultsArea.classList.remove('hidden');

    // 1. KPI Cards
    const totalElem = document.getElementById('kpi-total-analyzed');
    const posPctElem = document.getElementById('kpi-pos-pct');
    const neuPctElem = document.getElementById('kpi-neu-pct');
    const negPctElem = document.getElementById('kpi-neg-pct');
    const avgCompElem = document.getElementById('kpi-avg-compound');
    const nssElem = document.getElementById('kpi-net-sentiment');

    if (totalElem) totalElem.innerText = summary.total;
    if (posPctElem) posPctElem.innerText = `${summary.positive_percent}% (${summary.positive_count})`;
    if (neuPctElem) neuPctElem.innerText = `${summary.neutral_percent}% (${summary.neutral_count})`;
    if (negPctElem) negPctElem.innerText = `${summary.negative_percent}% (${summary.negative_count})`;
    if (avgCompElem) avgCompElem.innerText = (summary.average_compound > 0 ? '+' : '') + summary.average_compound.toFixed(2);
    if (nssElem) {
        nssElem.innerText = (summary.net_sentiment_score > 0 ? '+' : '') + summary.net_sentiment_score;
        nssElem.style.color = summary.net_sentiment_score >= 0 ? '#10B981' : '#EF4444';
    }

    // 2. Charts
    renderBatchCharts(summary);

    // 3. Render Table
    renderBatchTable();
}

function renderBatchCharts(summary) {
    const donutCanvas = document.getElementById('batchDonutChart');
    const barCanvas = document.getElementById('batchBarChart');
    const isDark = document.documentElement.classList.contains('dark');
    const textColor = isDark ? '#fbbf24' : '#b45309';

    // Sentiment Donut Chart (Gold Theme)
    if (donutCanvas) {
        if (batchSentimentChart) batchSentimentChart.destroy();
        const ctx = donutCanvas.getContext('2d');
        batchSentimentChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Positive', 'Neutral', 'Negative'],
                datasets: [{
                    data: [summary.positive_count, summary.neutral_count, summary.negative_count],
                    backgroundColor: ['#f59e0b', '#71717a', '#ef4444'],
                    borderWidth: 2,
                    borderColor: isDark ? '#090a0d' : '#ffffff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color: textColor, boxWidth: 12, padding: 12 }
                    }
                },
                cutout: '65%'
            }
        });
        window.batchSentimentChart = batchSentimentChart;
    }

    // Emotions Bar Chart
    if (barCanvas && summary.emotions_distribution) {
        if (batchEmotionChart) batchEmotionChart.destroy();
        const labels = Object.keys(summary.emotions_distribution);
        const dataVals = Object.values(summary.emotions_distribution);
        const colors = ['#f59e0b', '#3b82f6', '#ef4444', '#a855f7', '#fbbf24', '#06b6d4'];

        const ctx = barCanvas.getContext('2d');
        batchEmotionChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Occurrences',
                    data: dataVals,
                    backgroundColor: colors.slice(0, labels.length),
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        ticks: { color: textColor, font: { size: 10 } },
                        grid: { display: false }
                    },
                    y: {
                        ticks: { color: textColor, precision: 0 },
                        grid: { color: isDark ? 'rgba(245, 158, 11, 0.12)' : 'rgba(217, 119, 6, 0.15)' }
                    }
                }
            }
        });
    }
}

function renderBatchTable() {
    const tbody = document.getElementById('batch-table-body');
    const paginationContainer = document.getElementById('batch-pagination');
    const searchVal = (document.getElementById('batch-table-search')?.value || '').toLowerCase();
    const filterVal = document.getElementById('batch-filter-sentiment')?.value || 'all';

    if (!tbody) return;

    // Filter results
    const filtered = batchAllResults.filter(row => {
        const matchesSearch = row.text.toLowerCase().includes(searchVal) || 
                              (row.top_aspect && row.top_aspect.toLowerCase().includes(searchVal));
        const matchesFilter = filterVal === 'all' || 
                              (filterVal === 'positive' && row.overall.label.includes('Positive')) ||
                              (filterVal === 'neutral' && row.overall.label.includes('Neutral')) ||
                              (filterVal === 'negative' && row.overall.label.includes('Negative'));
        return matchesSearch && matchesFilter;
    });

    const totalPages = Math.ceil(filtered.length / ROWS_PER_PAGE) || 1;
    if (batchCurrentPage > totalPages) batchCurrentPage = totalPages;

    const startIndex = (batchCurrentPage - 1) * ROWS_PER_PAGE;
    const pageRows = filtered.slice(startIndex, startIndex + ROWS_PER_PAGE);

    tbody.innerHTML = '';

    if (pageRows.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="5" class="py-6 text-center text-slate-400 text-sm">
                    No matching records found.
                </td>
            </tr>
        `;
        if (paginationContainer) paginationContainer.innerHTML = '';
        return;
    }

    pageRows.forEach(row => {
        const tr = document.createElement('tr');
        tr.className = "border-b border-slate-100 dark:border-slate-800/80 hover:bg-slate-50/60 dark:hover:bg-slate-800/40 transition";
        
        const isPos = row.overall.label.includes('Positive');
        const isNeg = row.overall.label.includes('Negative');
        const badgeColor = isPos 
            ? 'bg-emerald-100 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300' 
            : (isNeg 
                ? 'bg-rose-100 dark:bg-rose-950/60 text-rose-700 dark:text-rose-300' 
                : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300');

        tr.innerHTML = `
            <td class="py-3 px-4 text-xs font-mono text-slate-400">#${row.id}</td>
            <td class="py-3 px-4 text-xs text-slate-800 dark:text-slate-200 font-medium max-w-md truncate" title="${row.text}">
                ${row.text}
            </td>
            <td class="py-3 px-4 text-xs whitespace-nowrap">
                <span class="px-2.5 py-1 rounded-full font-semibold ${badgeColor}">
                    ${row.overall.label}
                </span>
            </td>
            <td class="py-3 px-4 text-xs font-semibold whitespace-nowrap" style="color: ${row.overall.theme_color}">
                ${(row.overall.compound_score > 0 ? '+' : '') + row.overall.compound_score.toFixed(2)}
            </td>
            <td class="py-3 px-4 text-xs text-slate-600 dark:text-slate-300 whitespace-nowrap">
                ${row.dominant_emotion}
            </td>
        `;

        tr.addEventListener('click', () => {
            // Load this row into single live analyzer
            const input = document.getElementById('sentiment-text-input');
            if (input) {
                input.value = row.text;
                updateCharWordCounts();
                document.querySelector('[data-tab="tab-live"]')?.click();
                triggerAnalysis();
            }
        });

        tbody.appendChild(tr);
    });

    // Pagination
    if (paginationContainer) {
        paginationContainer.innerHTML = `
            <span class="text-xs text-slate-500 dark:text-slate-400">
                Showing ${startIndex + 1}-${Math.min(startIndex + ROWS_PER_PAGE, filtered.length)} of ${filtered.length} entries
            </span>
            <div class="flex items-center gap-1.5">
                <button ${batchCurrentPage <= 1 ? 'disabled' : ''} onclick="changeBatchPage(${batchCurrentPage - 1})" class="px-2.5 py-1 rounded text-xs border border-slate-200 dark:border-slate-700 disabled:opacity-40 hover:bg-slate-100 dark:hover:bg-slate-800 transition">
                    Prev
                </button>
                <span class="text-xs font-medium px-2 text-slate-700 dark:text-slate-300">
                    ${batchCurrentPage} / ${totalPages}
                </span>
                <button ${batchCurrentPage >= totalPages ? 'disabled' : ''} onclick="changeBatchPage(${batchCurrentPage + 1})" class="px-2.5 py-1 rounded text-xs border border-slate-200 dark:border-slate-700 disabled:opacity-40 hover:bg-slate-100 dark:hover:bg-slate-800 transition">
                    Next
                </button>
            </div>
        `;
    }
}

window.changeBatchPage = function(newPage) {
    batchCurrentPage = newPage;
    renderBatchTable();
};

function exportBatchToCSV() {
    if (!batchAllResults || batchAllResults.length === 0) return;

    let csvContent = "data:text/csv;charset=utf-8,";
    csvContent += "ID,Text,Sentiment,CompoundScore,Confidence,DominantEmotion,TopAspect\n";

    batchAllResults.forEach(r => {
        const cleanText = `"${r.text.replace(/"/g, '""')}"`;
        const line = [
            r.id,
            cleanText,
            r.overall.label,
            r.overall.compound_score,
            r.overall.confidence,
            r.dominant_emotion,
            r.top_aspect
        ].join(",");
        csvContent += line + "\n";
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `sentix_batch_analysis_${Date.now()}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function exportBatchToJSON() {
    if (!batchAllResults || batchAllResults.length === 0) return;

    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(batchAllResults, null, 2));
    const link = document.createElement("a");
    link.setAttribute("href", dataStr);
    link.setAttribute("download", `sentix_batch_analysis_${Date.now()}.json`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
