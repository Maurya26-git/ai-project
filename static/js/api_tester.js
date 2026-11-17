/**
 * Sentix - Interactive API Playground & Documentation
 */

const CODE_TEMPLATES = {
    curl: `curl -X POST "http://127.0.0.1:5000/api/analyze" \\
  -H "Content-Type: application/json" \\
  -d '{
    "text": "The camera on this phone is truly phenomenal with crisp 4K video!"
  }'`,

    python: `import requests

url = "http://127.0.0.1:5000/api/analyze"
payload = {
    "text": "The camera on this phone is truly phenomenal with crisp 4K video!"
}

response = requests.post(url, json=payload)
data = response.json()
print("Sentiment:", data["data"]["overall"]["label"])
print("Compound:", data["data"]["overall"]["compound_score"])
print("Dominant Emotion:", data["data"]["emotions"]["dominant"])`,

    javascript: `fetch('http://127.0.0.1:5000/api/analyze', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    text: 'The camera on this phone is truly phenomenal with crisp 4K video!'
  })
})
.then(res => res.json())
.then(json => console.log(json.data));`
};

document.addEventListener('DOMContentLoaded', () => {
    initApiTester();
});

function initApiTester() {
    const codeSnippetElem = document.getElementById('api-code-snippet');
    const copyBtn = document.getElementById('btn-copy-code');
    const langTabs = document.querySelectorAll('.api-lang-tab');

    // Default to Python
    if (codeSnippetElem) codeSnippetElem.innerText = CODE_TEMPLATES.python;

    langTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const lang = tab.getAttribute('data-lang');
            langTabs.forEach(t => {
                t.classList.remove('bg-indigo-600', 'text-white');
                t.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');
            });
            tab.classList.add('bg-indigo-600', 'text-white');
            tab.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');

            if (codeSnippetElem && CODE_TEMPLATES[lang]) {
                codeSnippetElem.innerText = CODE_TEMPLATES[lang];
            }
        });
    });

    copyBtn?.addEventListener('click', () => {
        if (!codeSnippetElem) return;
        navigator.clipboard.writeText(codeSnippetElem.innerText).then(() => {
            const originalText = copyBtn.innerHTML;
            copyBtn.innerHTML = '<i data-lucide="check" class="w-3.5 h-3.5 text-emerald-400"></i> Copied!';
            if (window.lucide) lucide.createIcons();
            setTimeout(() => {
                copyBtn.innerHTML = originalText;
                if (window.lucide) lucide.createIcons();
            }, 2000);
        });
    });

    // Test form runner
    const runTestBtn = document.getElementById('btn-run-api-test');
    runTestBtn?.addEventListener('click', runInteractiveApiTest);
}

async function runInteractiveApiTest() {
    const endpoint = document.getElementById('api-test-endpoint')?.value || '/api/analyze';
    const payloadText = document.getElementById('api-test-payload')?.value || '{}';
    const responseBox = document.getElementById('api-test-response');
    const statusBox = document.getElementById('api-test-status');

    if (responseBox) responseBox.innerText = 'Sending request...';

    try {
        let options = {
            method: endpoint.includes('stats') || endpoint.includes('samples') ? 'GET' : 'POST',
            headers: { 'Content-Type': 'application/json' }
        };

        if (options.method === 'POST') {
            options.body = payloadText;
        }

        const start = performance.now();
        const res = await fetch(endpoint, options);
        const duration = Math.round(performance.now() - start);

        const data = await res.json();

        if (statusBox) {
            statusBox.innerHTML = `Status: <span class="${res.ok ? 'text-emerald-500' : 'text-rose-500'} font-bold">${res.status} ${res.statusText}</span> · Latency: <strong>${duration}ms</strong>`;
        }

        if (responseBox) {
            responseBox.innerText = JSON.stringify(data, null, 2);
        }
    } catch (err) {
        if (responseBox) responseBox.innerText = 'Error: ' + err.message;
    }
}
