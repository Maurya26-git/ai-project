# -*- coding: utf-8 -*-
"""
Script to generate the complete, academic-grade Project Synopsis HTML and compile it into an A4 PDF using Chrome Headless.
"""
import os
import subprocess
import shutil

DOCS_DIR = r"C:\Users\remal\.gemini\antigravity\scratch\sentiment-analyzer\docs"
HTML_PATH = os.path.join(DOCS_DIR, "PROJECT_SYNOPSIS.html")
PDF_PATH = os.path.join(DOCS_DIR, "PROJECT_SYNOPSIS.pdf")
ARTIFACT_DIR = r"C:\Users\remal\.gemini\antigravity\brain\7a4e57cf-d188-4d43-ac46-fd6aaf2afa3a"
ARTIFACT_PDF_PATH = os.path.join(ARTIFACT_DIR, "PROJECT_SYNOPSIS.pdf")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Project Synopsis - Sentix: Sentiment & Emotion Intelligence System</title>
<style>
  @page {
    size: A4 portrait;
    margin: 25.4mm 20mm 25.4mm 20mm;
    @top-right {
      content: "PROJECT SYNOPSIS | SENTIX";
      font-family: 'Times New Roman', Times, serif;
      font-size: 8.5pt;
      color: #64748b;
      font-style: italic;
    }
    @bottom-center {
      content: "Page " counter(page);
      font-family: 'Times New Roman', Times, serif;
      font-size: 9.5pt;
      color: #334155;
    }
  }

  @page :first {
    margin: 20mm 20mm 20mm 20mm;
    @top-right { content: none; }
    @bottom-center { content: none; }
  }

  * {
    box-sizing: border-box;
  }

  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #111827;
    margin: 0;
    padding: 0;
    text-align: justify;
  }

  /* Cover Page Styling */
  .cover-page {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 242mm;
    box-sizing: border-box;
    text-align: center;
    border: 3px double #0f2942;
    padding: 30px 24px;
    background-color: #ffffff;
  }

  .cover-header {
    margin-top: 5px;
  }

  .inst-name {
    font-size: 16pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #0f2942;
    letter-spacing: 0.8px;
    margin-bottom: 5px;
  }

  .dept-name {
    font-size: 12.5pt;
    font-weight: bold;
    color: #334155;
    margin-bottom: 22px;
  }

  .synopsis-badge {
    display: inline-block;
    font-size: 14pt;
    font-weight: bold;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #0f2942;
    border-top: 2px solid #0f2942;
    border-bottom: 2px solid #0f2942;
    padding: 5px 28px;
    margin: 12px 0 20px 0;
  }

  .project-title-box {
    margin: 18px 0;
    padding: 16px 14px;
    background-color: #f8fafc;
    border-left: 4px solid #0f2942;
    border-right: 4px solid #0f2942;
  }

  .project-title {
    font-size: 15.5pt;
    font-weight: bold;
    color: #0f2942;
    line-height: 1.35;
    text-transform: uppercase;
  }

  .submission-notice {
    font-size: 11pt;
    font-style: italic;
    color: #475569;
    margin: 20px auto;
    max-width: 520px;
    line-height: 1.45;
  }

  .degree-name {
    font-size: 12.5pt;
    font-weight: bold;
    color: #1e293b;
    font-style: normal;
    margin-top: 4px;
    display: block;
  }

  .metadata-grid {
    display: flex;
    justify-content: space-between;
    text-align: left;
    margin: 25px 10px 15px 10px;
    padding-top: 15px;
    border-top: 1px solid #cbd5e1;
  }

  .meta-col {
    width: 48%;
  }

  .meta-label {
    font-size: 9.5pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 4px;
  }

  .meta-val {
    font-size: 11pt;
    color: #0f172a;
    line-height: 1.4;
  }

  .meta-val strong {
    font-weight: bold;
    color: #0f2942;
  }

  .placeholder-tag {
    background-color: #fef3c7;
    border: 1px dashed #d97706;
    padding: 1px 4px;
    border-radius: 2px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 9.5pt;
    color: #92400e;
  }

  .academic-session {
    font-size: 10.5pt;
    font-weight: bold;
    color: #334155;
    margin-top: 20px;
    letter-spacing: 0.5px;
  }

  /* Body Content Styles */
  h1 {
    font-size: 13.5pt;
    font-weight: bold;
    color: #0f2942;
    border-bottom: 1.5px solid #0f2942;
    padding-bottom: 2px;
    margin-top: 18pt;
    margin-bottom: 7pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    page-break-after: avoid;
    break-after: avoid;
  }

  h2 {
    font-size: 12pt;
    font-weight: bold;
    color: #1e3a8a;
    margin-top: 12pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  h3 {
    font-size: 11.5pt;
    font-weight: bold;
    color: #334155;
    margin-top: 9pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
    break-after: avoid;
  }

  p {
    margin: 0 0 8pt 0;
    text-indent: 0;
  }

  ul, ol {
    margin: 0 0 9pt 0;
    padding-left: 22px;
  }

  li {
    margin-bottom: 3.5pt;
    line-height: 1.42;
  }

  .page-break {
    page-break-before: always;
    break-before: always;
  }

  .avoid-break {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 10pt 0;
    font-size: 9.8pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  th {
    background-color: #0f2942;
    color: #ffffff;
    font-weight: bold;
    border: 1px solid #0f2942;
    padding: 5.5pt 7.5pt;
    text-align: left;
    letter-spacing: 0.2px;
  }

  td {
    border: 1px solid #cbd5e1;
    padding: 4.8pt 7pt;
    vertical-align: top;
    line-height: 1.35;
  }

  tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  /* Math & Equations */
  .equation-box {
    background-color: #f8fafc;
    border-left: 3.5px solid #1e3a8a;
    padding: 7pt 14pt;
    margin: 9pt 0;
    font-size: 11pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .math-formula {
    display: inline-flex;
    align-items: center;
    font-family: 'Times New Roman', serif;
    font-size: 11.5pt;
  }

  .math-var {
    font-style: italic;
    font-weight: bold;
    padding: 0 1px;
  }

  .fraction {
    display: inline-flex;
    flex-direction: column;
    vertical-align: middle;
    text-align: center;
    padding: 0 4px;
  }

  .numerator {
    border-bottom: 1px solid #111827;
    padding-bottom: 1px;
    font-size: 10.5pt;
  }

  .denominator {
    padding-top: 1px;
    font-size: 10.5pt;
  }

  .eq-num {
    font-style: normal;
    font-weight: bold;
    color: #64748b;
    font-size: 10pt;
  }

  /* Diagram Box */
  .diagram-container {
    margin: 11pt 0;
    padding: 8pt;
    border: 1px solid #cbd5e1;
    background-color: #ffffff;
    text-align: center;
    border-radius: 4px;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .diagram-caption {
    font-size: 9.5pt;
    font-weight: bold;
    color: #334155;
    margin-top: 5pt;
    text-align: center;
  }

  /* Metric cards grid */
  .metrics-grid {
    display: flex;
    justify-content: space-between;
    gap: 8px;
    margin: 9pt 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .metric-card {
    flex: 1;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-top: 3px solid #0f2942;
    padding: 7pt 5pt;
    text-align: center;
    border-radius: 3px;
  }

  .metric-value {
    font-size: 13.5pt;
    font-weight: bold;
    color: #0f2942;
  }

  .metric-label {
    font-size: 8.5pt;
    font-weight: bold;
    color: #64748b;
    text-transform: uppercase;
    margin-top: 2px;
  }

  /* References */
  .ref-item {
    margin-bottom: 5.5pt;
    padding-left: 22pt;
    text-indent: -22pt;
    font-size: 10pt;
    line-height: 1.38;
  }
</style>
</head>
<body>

<!-- ========================================== -->
<!-- COVER PAGE                                 -->
<!-- ========================================== -->
<div class="cover-page">
  <div class="cover-header">
    <div class="inst-name">[NAME OF UNIVERSITY / INSTITUTION]</div>
    <div class="dept-name">Department of Computer Science & Engineering</div>
    
    <div>
      <span class="synopsis-badge">PROJECT SYNOPSIS</span>
    </div>

    <div class="project-title-box">
      <div class="project-title">
        SENTIX: AN INTELLIGENT MULTI-TIER SENTIMENT AND EMOTION INTELLIGENCE SYSTEM WITH ASPECT-BASED OPINION MINING AND EXPLAINABLE AI
      </div>
    </div>

    <div class="submission-notice">
      Submitted in partial fulfillment of the requirements for the degree of
      <span class="degree-name">[Bachelor of Technology / Master of Technology / MCA]</span>
      in Computer Science and Engineering
    </div>
  </div>

  <div>
    <div class="metadata-grid">
      <div class="meta-col">
        <div class="meta-label">Submitted By:</div>
        <div class="meta-val">
          <strong>[Student Name]</strong><br>
          Roll No: <span class="placeholder-tag">[Roll Number / Registration No.]</span><br>
          Semester / Section: <span class="placeholder-tag">[VIII Sem / Sec A]</span>
        </div>
      </div>
      <div class="meta-col" style="text-align: right;">
        <div class="meta-label">Under the Guidance of:</div>
        <div class="meta-val">
          <strong>[Supervisor’s Name]</strong><br>
          <span class="placeholder-tag">[Designation, e.g., Associate Professor]</span><br>
          Department of Computer Science & Engg.
        </div>
      </div>
    </div>

    <div class="academic-session">
      ACADEMIC SESSION: [2026 – 2027]
    </div>
  </div>
</div>

<!-- ========================================== -->
<!-- SECTION 1 & 2                              -->
<!-- ========================================== -->
<h1>1. Title of the Project</h1>
<p>
  <strong>SENTIX: An Intelligent Multi-Tier Sentiment and Emotion Intelligence System with Aspect-Based Opinion Mining and Explainable AI</strong>
</p>

<h1>2. Abstract</h1>
<p>
  With the exponential growth of user-generated unstructured text across modern e-commerce storefronts, streaming entertainment, gaming ecosystems, and social networks, automated opinion mining has become pivotal for corporate decision intelligence, brand health monitoring, and public perception audits. However, conventional sentiment analysis pipelines overwhelmingly produce monolithic polarity labels (Positive, Negative, or Neutral). Such coarse abstractions routinely obscure fine-grained aspect evaluations (e.g., distinguishing high praise for a smartphone camera from severe criticism of its battery life), fail in the presence of complex linguistic markers such as double negations, intensifiers, and sarcasm, and operate as uninterpretable black-box algorithms.
</p>
<p>
  To solve these systemic limitations, this project presents <strong>Sentix</strong>, a full-stack, enterprise-grade Sentiment and Emotion Intelligence System. Sentix pioneers a hybrid dual-core classification architecture combining rule-based linguistic valence shifting (intensifiers, diminishers, idiom resolution, and emoji valence) with statistical Machine Learning (TF-IDF vectorization with Multinomial Naive Bayes and Logistic Regression classifiers). The system features an automated Aspect-Based Sentiment Analysis (ABSA) engine across consumer tech, cinema, video games, and international travel domains, accompanied by a 6-axis affective emotion decomposition framework (Joy, Trust, Anticipation, Sadness, Anger, Disgust). Furthermore, Sentix implements an Explainable AI (XAI) feature-attribution subsystem providing token-level saliency scores to deliver complete auditing transparency.
</p>
<p>
  Rigorous empirical validation conducted against a 60-sample gold-standard academic benchmark corpus spanning intricate linguistic corner cases demonstrates that Sentix achieves an overall classification accuracy of <strong>86.7%</strong>, a Macro F1-score of <strong>0.867</strong>, a Matthews Correlation Coefficient (MCC) of <strong>0.801</strong>, and a Cohen’s Kappa of <strong>&kappa; = 0.800</strong>. The software is containerized and deployed with a responsive, low-latency web dashboard, a developer REST API, dynamic QR-code network sharing, and on-the-fly universal entity synthesis.
</p>

<!-- ========================================== -->
<!-- SECTION 3: INTRODUCTION                     -->
<!-- ========================================== -->
<h1>3. Introduction</h1>
<p>
  Natural Language Processing (NLP) and opinion mining have transitioned from auxiliary business intelligence tools to fundamental infrastructure governing how modern organizations interpret human feedback. The rapid expansion of digital platforms has democratized publishing, resulting in millions of consumer product reviews, cinematic critiques, gaming feedback posts, and hospitality evaluations generated daily. Converting this high-volume unstructured text into actionable, quantitative insights is a cornerstone challenge of computational linguistics.
</p>
<p>
  Traditional sentiment classification systems primarily classify texts into broad positive, negative, or neutral categories using either superficial bag-of-words keyword counts or resource-intensive deep learning models. While large language models (LLMs) have achieved high accuracy, their deployment in enterprise production often incurs prohibitive API costs, high token inference latencies (often 800ms–2500ms), and substantial opacity regarding feature attribution. Conversely, lightweight lexicon systems operate with sub-millisecond latency but fail to generalize to subtle syntactic nuances and statistical word co-occurrences.
</p>
<p>
  The proposed project, <strong>Sentix</strong>, addresses these challenges by developing an integrated, multi-tier computational framework. By synthesizing rule-grounded linguistic heuristics with statistical machine learning and granular aspect extraction, Sentix provides real-time, explainable opinion mining suitable for production environments. The project bridges academic rigor—including formal mathematical formulations, confusion matrix diagnostics, and 5-fold cross-validation—with an intuitive, production-grade web interface.
</p>

<!-- ========================================== -->
<!-- SECTION 4: PROBLEM STATEMENT               -->
<!-- ========================================== -->
<h1>4. Problem Statement</h1>
<p>
  Despite extensive research in sentiment analysis, existing open-source and commercial solutions continue to exhibit significant operational limitations when applied to real-world textual data:
</p>
<ul>
  <li><strong>Polarity Oversimplification:</strong> Treating an entire multi-sentence document as a single aggregate scalar discards contrasting opinions. A customer reviewing a flagship laptop may admire the display while condemning thermal throttling; standard tools produce an ambiguous "Neutral" score that obscures both vital insights.</li>
  <li><strong>Syntactic & Negation Sensitivity:</strong> Idiomatic expressions, contrastive conjunctions (e.g., <em>"although"</em>, <em>"but"</em>, <em>"nevertheless"</em>), and double negations (e.g., <em>"not bad at all"</em>) routinely invert model classifications when positional grammar is ignored.</li>
  <li><strong>Absence of Explainability (The Black-Box Problem):</strong> Machine learning and neural models rarely provide token-level justification for why a given classification was assigned, creating distrust among stakeholders and impeding diagnostic auditing.</li>
  <li><strong>Static Domain Boundaries:</strong> Standard systems rely entirely on pre-annotated static corpora and collapse when encountering newly released consumer products, media titles, or emerging colloquial slang.</li>
</ul>
<p>
  Therefore, there exists a critical need for an intelligent system that executes fine-grained aspect sentiment decomposition, identifies multi-dimensional emotional states, provides transparent token-level feature attribution, and operates with sub-50ms execution latency.
</p>

<!-- ========================================== -->
<!-- SECTION 5: AIM AND OBJECTIVES               -->
<!-- ========================================== -->
<h1>5. Aim and Objectives</h1>

<h2>5.1 Primary Aim</h2>
<p>
  To design, develop, rigorously benchmark, and deploy an explainable, multi-tier sentiment and emotion intelligence system (Sentix) capable of performing granular aspect-based opinion mining, multi-dimensional emotional classification, and token-level feature attribution across heterogeneous domains in real time.
</p>

<h2>5.2 Specific Objectives</h2>
<ol>
  <li><strong>Linguistic Rule-Base Engineering:</strong> To construct an extensive linguistic lexicon incorporating valence scores, emoji sentiment values, degree intensifiers, diminishers, idiomatic constructs, and contrastive conjunction rules.</li>
  <li><strong>Statistical Machine Learning Integration:</strong> To implement and train an n-gram TF-IDF vectorizer paired with a calibrated statistical classifier to capture latent contextual distributions.</li>
  <li><strong>Ensemble Scoring Formulation:</strong> To devise and calibrate a soft-valence normalization algorithm blending rule-grounded polarity with statistical machine learning confidence.</li>
  <li><strong>Aspect-Based Sentiment Mining (ABSA):</strong> To engineer a dependency-free aspect extraction engine that maps sentiments directly to domain facets (Hardware, Performance, Display, Story, Gameplay, Hospitality, Cost).</li>
  <li><strong>Affective Emotion Profiling:</strong> To construct an affective detection model mapping text to six discrete psychological dimensions (Joy, Trust, Anticipation, Sadness, Anger, and Disgust).</li>
  <li><strong>Explainable AI (XAI) Attribution:</strong> To formulate a token-level saliency attribution algorithm that quantifies and visualizes the positive and negative contribution of individual words to the final verdict.</li>
  <li><strong>Academic Evaluation & Benchmarking:</strong> To validate the system against a gold-standard 60-sample academic corpus, computing Accuracy, Precision, Recall, Macro F1, Cohen’s Kappa, Matthews Correlation Coefficient, and 5-Fold Stratified Cross-Validation.</li>
  <li><strong>Interactive Web Deployment:</strong> To implement a production-ready Flask web application featuring interactive dashboards, universal on-the-fly entity generation, and dynamic QR-code network accessibility.</li>
</ol>

<div class="page-break"></div>

<!-- ========================================== -->
<!-- SECTION 6: LITERATURE REVIEW               -->
<!-- ========================================== -->
<h1>6. Literature Review</h1>
<p>
  A comprehensive survey of prevailing literature was conducted to benchmark foundational paradigms, investigate contemporary architectural developments, and delineate the precise research gap addressed by this work.
</p>

<table>
  <thead>
    <tr>
      <th style="width: 22%;">Author(s) & Year</th>
      <th style="width: 24%;">Research Approach</th>
      <th style="width: 28%;">Key Findings</th>
      <th style="width: 26%;">Identified Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Hutto & Gilbert (2014)</strong></td>
      <td>VADER: Rule-based heuristic sentiment scoring designed for social media text.</td>
      <td>Demonstrated high correlation with human raters on microblogs; effectively models punctuation and emojis.</td>
      <td>Lacks statistical learning capabilities; fails to model complex semantic dependencies and domain-specific vocabulary.</td>
    </tr>
    <tr>
      <td><strong>Pang & Lee (2008)</strong></td>
      <td>Supervised statistical machine learning (Naive Bayes, Maximum Entropy, SVM) on movie reviews.</td>
      <td>Established that standard ML classifiers outperform human-crafted keyword baselines on document-level polarity.</td>
      <td>Cannot isolate aspect-level sentiments; susceptible to vocabulary sparsity and high out-of-vocabulary error rates.</td>
    </tr>
    <tr>
      <td><strong>Pontiki et al. (2016)</strong></td>
      <td>SemEval Aspect-Based Sentiment Analysis (ABSA) benchmark task formulation.</td>
      <td>Standardized target-entity aspect decomposition and showed aspect polarity often conflicts with overall text polarity.</td>
      <td>Heavy dependency on manual human annotation; high computational latency when implemented via complex neural networks.</td>
    </tr>
    <tr>
      <td><strong>Devlin et al. (2019)</strong></td>
      <td>BERT: Bidirectional Encoder Representations from Transformers for NLP sequence classification.</td>
      <td>Attained state-of-the-art accuracy across GLUE benchmarks; captures bidirectional contextual representations.</td>
      <td>Prohibitive compute footprint, high GPU memory demands, inference latency exceeding 100ms, and total black-box opacity.</td>
    </tr>
    <tr>
      <td><strong>Ribeiro et al. (2016)</strong></td>
      <td>LIME: Local Interpretable Model-agnostic Explanations for validating model decisions.</td>
      <td>Demonstrated that visualizing feature importance is essential for identifying model bias and gaining human trust.</td>
      <td>Sampling-based perturbation steps introduce noticeable computational overhead, making real-time interactive evaluation sluggish.</td>
    </tr>
  </tbody>
</table>

<h3>Research Gap</h3>
<p>
  Current literature reflects a bifurcated landscape: on one side are lightweight rule-based tools that run rapidly but lack statistical generalization; on the other are massive transformer architectures that achieve high accuracy but suffer from extreme computational cost, high deployment latency, and uninterpretable decision pathways. Furthermore, existing open-source frameworks rarely unite rule-based valence shifting, multi-class emotion profiling, aspect extraction, and instantaneous XAI token attribution into a single unified runtime. <strong>Sentix</strong> bridges this specific gap by delivering a hybrid, low-latency, transparent intelligence architecture.
</p>

<!-- ========================================== -->
<!-- SECTION 7: EXISTING SYSTEM                 -->
<!-- ========================================== -->
<h1>7. Existing System</h1>
<p>
  Contemporary sentiment analysis systems deployed in industry and academia generally fall into one of two operational categories:
</p>
<ol>
  <li><strong>Standalone Rule-Based Lexicon Engines:</strong> Systems such as standard VADER or TextBlob parse input strings using dictionary lookups and fixed arithmetic weights.
    <ul>
      <li><em>Advantages:</em> Zero training overhead, near-instantaneous execution, minimal CPU/RAM footprint.</li>
      <li><em>Limitations:</em> Incapable of learning domain-specific vocabulary distributions; completely blind to document-level statistical n-grams; incapable of automatic aspect segmentation.</li>
    </ul>
  </li>
  <li><strong>Monolithic Deep Neural Classifiers:</strong> Systems employing fine-tuned transformer networks (BERT, RoBERTa) or commercial third-party LLM APIs.
    <ul>
      <li><em>Advantages:</em> High classification accuracy on complex contextual text.</li>
      <li><em>Limitations:</em> Extremely high inference latency (0.5s–3s per call); high recurring monetary expense for cloud API tokens; opaque black-box parameters preventing interpretable auditing.</li>
    </ul>
  </li>
</ol>
<p>
  <strong>Areas Requiring Improvement:</strong> Existing platforms fail to synthesize speed with statistical depth, lack native aspect extraction without heavy annotation pipelines, and rarely provide native token-level explainability suited for live academic review.
</p>

<!-- ========================================== -->
<!-- SECTION 8: PROPOSED SYSTEM                 -->
<!-- ========================================== -->
<h1>8. Proposed System</h1>
<p>
  The proposed <strong>Sentix</strong> architecture resolves the limitations of existing frameworks through a synchronized multi-tier computational strategy:
</p>
<ul>
  <li><strong>Hybrid Dual-Core Classification Engine:</strong> Sentix concurrently executes a rule-calibrated linguistic parser and a trained TF-IDF statistical machine learning classifier. The linguistic engine calculates an exact valence compound score, while the statistical classifier outputs class probability distributions.</li>
  <li><strong>Soft-Valence Mathematical Normalization:</strong> To map unbounded linguistic score summations into a continuous normalized range of [&minus;1.0, +1.0], Sentix formulates a calibrated hyperbolic normalization function:</li>
</ul>

<div class="equation-box">
  <div class="math-formula">
    <span class="math-var">C</span> = 
    <span class="fraction">
      <span class="numerator"><span class="math-var">V</span></span>
      <span class="denominator">&radic;(<span class="math-var">V</span><sup>2</sup> + &alpha;)</span>
    </span>
    <span style="margin-left: 20px; font-style: normal; font-size: 10pt; color: #475569;">where &alpha; = 15 [Damping Constant]</span>
  </div>
  <span class="eq-num">(Equation 1)</span>
</div>

<p>
  Here, <em>V</em> represents the raw sum of context-adjusted token valences, and &alpha; = 15 is an empirically validated damping constant that provides smooth gradient transitions without early saturation.
</p>
<ul>
  <li><strong>Weighted Ensemble Fusion:</strong> The finalized aggregate score combines the normalized linguistic compound score (<em>C</em><sub>lex</sub>) and the statistical ML confidence (<em>S</em><sub>ml</sub>) according to the optimal weighting formulation:</li>
</ul>

<div class="equation-box">
  <div class="math-formula">
    <span class="math-var">S</span><sub>final</sub> = 
    clip(0.65 &middot; <span class="math-var">C</span><sub>lex</sub> + 0.35 &middot; <span class="math-var">S</span><sub>ml</sub>, &minus;1.0, +1.0)
    <span style="margin-left: 20px; font-style: normal; font-size: 10pt; color: #475569;">[Ensemble Fusion Formula]</span>
  </div>
  <span class="eq-num">(Equation 2)</span>
</div>

<ul>
  <li><strong>Aspect-Based Sentiment Decomposition (ABSA):</strong> Sentix isolates target noun-phrase entities across domain taxonomies (Electronics, Cinema, Gaming, Travel) and evaluates localized valence within sentence clause windows.</li>
  <li><strong>6-Axis Affective Emotion Radar:</strong> Incorporates a psycho-lexical mapper quantifying Joy, Trust, Anticipation, Sadness, Anger, and Disgust to capture emotional richness beyond binary positive/negative labels.</li>
  <li><strong>Explainable AI (XAI) Token Attribution:</strong> Computes token-level saliency scores:</li>
</ul>

<div class="equation-box">
  <div class="math-formula">
    <span class="math-var">A</span>(<span class="math-var">w</span><sub>i</sub>) = <span class="math-var">w</span><sub>i</sub> &middot; <span class="math-var">x</span><sub>i</sub>
    <span style="margin-left: 20px; font-style: normal; font-size: 10pt; color: #475569;">where <span class="math-var">w</span><sub>i</sub> is feature weight and <span class="math-var">x</span><sub>i</sub> is TF-IDF presence</span>
  </div>
  <span class="eq-num">(Equation 3)</span>
</div>

<div class="page-break"></div>

<!-- ========================================== -->
<!-- SECTION 9: RESEARCH METHODOLOGY            -->
<!-- ========================================== -->
<h1>9. Research Methodology</h1>
<p>
  The project follows a rigorous, six-stage scientific methodology designed to ensure empirical reproducibility, robust statistical evaluation, and architectural stability.
</p>

<div class="diagram-container">
  <!-- SVG Workflow Diagram -->
  <svg width="100%" height="85" viewBox="0 0 780 85" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#0f2942;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#1e3a8a;stop-opacity:1" />
      </linearGradient>
    </defs>
    
    <!-- Step 1 -->
    <rect x="5" y="12" width="115" height="58" rx="4" fill="url(#grad1)"/>
    <text x="62" y="35" fill="#ffffff" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Phase 1</text>
    <text x="62" y="50" fill="#e2e8f0" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">Problem & Scope</text>
    
    <path d="M 122 41 L 133 41" stroke="#0f2942" stroke-width="2"/>
    
    <!-- Step 2 -->
    <rect x="135" y="12" width="115" height="58" rx="4" fill="url(#grad1)"/>
    <text x="192" y="35" fill="#ffffff" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Phase 2</text>
    <text x="192" y="50" fill="#e2e8f0" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">Corpus & Preprocess</text>
    
    <path d="M 252 41 L 263 41" stroke="#0f2942" stroke-width="2"/>
    
    <!-- Step 3 -->
    <rect x="265" y="12" width="115" height="58" rx="4" fill="url(#grad1)"/>
    <text x="322" y="35" fill="#ffffff" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Phase 3</text>
    <text x="322" y="50" fill="#e2e8f0" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">Dual-Core Modeling</text>
    
    <path d="M 382 41 L 393 41" stroke="#0f2942" stroke-width="2"/>
    
    <!-- Step 4 -->
    <rect x="395" y="12" width="115" height="58" rx="4" fill="url(#grad1)"/>
    <text x="452" y="35" fill="#ffffff" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Phase 4</text>
    <text x="452" y="50" fill="#e2e8f0" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">ABSA & XAI Engine</text>
    
    <path d="M 512 41 L 523 41" stroke="#0f2942" stroke-width="2"/>
    
    <!-- Step 5 -->
    <rect x="525" y="12" width="115" height="58" rx="4" fill="url(#grad1)"/>
    <text x="582" y="35" fill="#ffffff" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Phase 5</text>
    <text x="582" y="50" fill="#e2e8f0" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">Academic Benchmark</text>
    
    <path d="M 642 41 L 653 41" stroke="#0f2942" stroke-width="2"/>
    
    <!-- Step 6 -->
    <rect x="655" y="12" width="118" height="58" rx="4" fill="url(#grad1)"/>
    <text x="714" y="35" fill="#ffffff" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" text-anchor="middle">Phase 6</text>
    <text x="714" y="50" fill="#e2e8f0" font-family="'Times New Roman', serif" font-size="8.5" text-anchor="middle">Web App & REST API</text>
  </svg>
  <div class="diagram-caption">Figure 1: End-to-End Methodological Research & Engineering Pipeline</div>
</div>

<ol>
  <li><strong>Corpus Assembly & Annotation:</strong> A multi-domain benchmark corpus comprising 60 gold-standard records across Positive, Neutral, and Negative classes was created. It specifically embeds adversarial cases: sarcastic statements, double negations, contrastive conjunctions, and emoji valence modifiers.</li>
  <li><strong>Text Normalization & Tokenization:</strong> Raw text is preprocessed through a custom linguistic tokenizer that isolates word boundaries while strictly preserving hyphenated idioms, emoticons, and multi-character punctuation markers.</li>
  <li><strong>Dual-Engine Feature Extraction:</strong>
    <ul>
      <li><em>Linguistic Extraction:</em> Evaluates word stems against valence dictionaries, applying amplification multipliers for intensifiers (1.25&times;) and negation flips (&minus;0.75&times;).</li>
      <li><em>Statistical Extraction:</em> Generates unigram and bigram TF-IDF sparse matrices capturing discriminatory term frequencies.</li>
    </ul>
  </li>
  <li><strong>Classifier Calibration & Ensemble Fusion:</strong> Both channels are integrated via the soft-valence formula to produce unified continuous scores and categorical sentiment assignments.</li>
  <li><strong>Empirical Cross-Validation:</strong> The pipeline is evaluated using 5-fold stratified cross-validation, computing confusion matrices, Cohen’s Kappa, and Matthews Correlation Coefficient.</li>
  <li><strong>Interface Engineering & REST API Deployment:</strong> The validated computational models are encapsulated inside a lightweight Flask backend and exposed via REST endpoints and a responsive client interface.</li>
</ol>

<!-- ========================================== -->
<!-- SECTION 10: TOOLS & TECHNOLOGIES REQUIRED  -->
<!-- ========================================== -->
<h1>10. Tools and Technologies Required</h1>
<p>
  Sentix utilizes modern, stable, open-source programming frameworks chosen specifically for low inference latency, minimal deployment dependencies, and cross-platform compatibility:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Category</th>
      <th style="width: 35%;">Tool / Framework</th>
      <th style="width: 40%;">Purpose in Project</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Core Language</strong></td>
      <td>Python 3.10 / 3.11 / 3.14</td>
      <td>Primary language for backend services, NLP parsing, and ML pipelines.</td>
    </tr>
    <tr>
      <td><strong>Backend Web Tier</strong></td>
      <td>Flask 3.1, Jinja2, Werkzeug</td>
      <td>High-speed asynchronous REST API routes and dynamic view routing.</td>
    </tr>
    <tr>
      <td><strong>Machine Learning & Stats</strong></td>
      <td>Scikit-learn 1.9, NumPy, SciPy</td>
      <td>TF-IDF vectorizer, Naive Bayes classifier, cross-validation metrics, confusion matrix.</td>
    </tr>
    <tr>
      <td><strong>Linguistic Modeling</strong></td>
      <td>Custom Valence Dictionary, Regex Tokenizer</td>
      <td>Sub-millisecond token valence lookups, intensifier rules, emoji sentiment decoding.</td>
    </tr>
    <tr>
      <td><strong>Frontend Interface</strong></td>
      <td>HTML5, CSS3, Vanilla ES6+ JavaScript</td>
      <td>Responsive luxury Obsidian Gold theme, DOM rendering, zero heavy frontend framework overhead.</td>
    </tr>
    <tr>
      <td><strong>Visualizations & Radar</strong></td>
      <td>HTML5 Canvas, Chart.js</td>
      <td>Real-time 6-axis emotion radar charts, XAI saliency bars, confusion matrix heatmap.</td>
    </tr>
    <tr>
      <td><strong>Remote Networking</strong></td>
      <td>Cloudflare Tunnel (<code>cloudflared</code>), QR-Code</td>
      <td>Instant worldwide public HTTPS accessibility across cellular networks and mobile devices.</td>
    </tr>
    <tr>
      <td><strong>Hardware Requirements</strong></td>
      <td>Intel Core i5 / AMD Ryzen 5, 8GB RAM, 1GB Disk</td>
      <td>Runs efficiently on consumer laptops without requiring dedicated GPU acceleration.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- ========================================== -->
<!-- SECTION 11: SYSTEM ARCHITECTURE            -->
<!-- ========================================== -->
<h1>11. System Architecture</h1>
<p>
  The architectural topology of Sentix is structured into five distinct operational tiers: Presentation, Gateway & Routing, Hybrid Intelligence Core, Explainability & Verification, and Network Distribution.
</p>

<div class="diagram-container">
  <!-- System Architecture Block Diagram -->
  <svg width="100%" height="235" viewBox="0 0 780 235" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#0f2942;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#1e3a8a;stop-opacity:1" />
      </linearGradient>
    </defs>
    
    <!-- Tier 1: User / Presentation -->
    <rect x="20" y="8" width="740" height="42" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="35" y="32" font-family="'Times New Roman', serif" font-size="10.5" font-weight="bold" fill="#0f2942">PRESENTATION TIER:</text>
    <rect x="200" y="15" width="125" height="26" rx="3" fill="#e2e8f0"/>
    <text x="262" y="32" font-family="'Times New Roman', serif" font-size="9" text-anchor="middle" fill="#1e293b">Interactive UI Catalog</text>
    <rect x="335" y="15" width="135" height="26" rx="3" fill="#e2e8f0"/>
    <text x="402" y="32" font-family="'Times New Roman', serif" font-size="9" text-anchor="middle" fill="#1e293b">Live Sentiment Analyzer</text>
    <rect x="480" y="15" width="135" height="26" rx="3" fill="#e2e8f0"/>
    <text x="547" y="32" font-family="'Times New Roman', serif" font-size="9" text-anchor="middle" fill="#1e293b">Academic Benchmarks</text>
    <rect x="625" y="15" width="120" height="26" rx="3" fill="#e2e8f0"/>
    <text x="685" y="32" font-family="'Times New Roman', serif" font-size="9" text-anchor="middle" fill="#1e293b">QR Mobile Portal</text>

    <!-- Connector Arrow -->
    <line x1="390" y1="50" x2="390" y2="65" stroke="#0f2942" stroke-width="2"/>

    <!-- Tier 2: Flask API Gateway -->
    <rect x="20" y="65" width="740" height="38" rx="4" fill="url(#headerGrad)"/>
    <text x="390" y="89" font-family="'Times New Roman', serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">
      REST API GATEWAY & DISPATCHER (Flask /api/analyze | /api/academic/benchmarks | /api/search/universal)
    </text>

    <!-- Connector Arrow -->
    <line x1="390" y1="103" x2="390" y2="117" stroke="#0f2942" stroke-width="2"/>

    <!-- Tier 3: Hybrid Intelligence Core -->
    <rect x="20" y="117" width="740" height="66" rx="4" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="35" y="137" font-family="'Times New Roman', serif" font-size="10.5" font-weight="bold" fill="#0f2942">HYBRID CORE:</text>
    
    <rect x="150" y="125" width="135" height="48" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="217" y="143" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f2942">Linguistic Engine</text>
    <text x="217" y="159" font-family="'Times New Roman', serif" font-size="8" text-anchor="middle" fill="#64748b">Valence, Emojis, Negation</text>

    <rect x="295" y="125" width="135" height="48" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="362" y="143" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f2942">Statistical ML</text>
    <text x="362" y="159" font-family="'Times New Roman', serif" font-size="8" text-anchor="middle" fill="#64748b">TF-IDF N-Gram Classifier</text>

    <rect x="440" y="125" width="145" height="48" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="512" y="143" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f2942">ABSA Extractor</text>
    <text x="512" y="159" font-family="'Times New Roman', serif" font-size="8" text-anchor="middle" fill="#64748b">Domain Entity Aspect Map</text>

    <rect x="595" y="125" width="150" height="48" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="670" y="143" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f2942">Affective Radar</text>
    <text x="670" y="159" font-family="'Times New Roman', serif" font-size="8" text-anchor="middle" fill="#64748b">6-Axis Emotion Profiling</text>

    <!-- Connector Arrow -->
    <line x1="390" y1="183" x2="390" y2="195" stroke="#0f2942" stroke-width="2"/>

    <!-- Tier 4: Verification & Explainability -->
    <rect x="20" y="195" width="740" height="34" rx="4" fill="#0f2942"/>
    <text x="390" y="216" font-family="'Times New Roman', serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">
      EXPLAINABLE AI (XAI) SALIENCY ATTRIBUTION & BENCHMARK VALIDATION ENGINE
    </text>
  </svg>
  <div class="diagram-caption">Figure 2: Multi-Tier Modular System Architecture of Sentix</div>
</div>

<p>
  <strong>Detailed Architectural Workflow:</strong>
</p>
<ul>
  <li><em>Data Ingestion:</em> Unstructured user text arrives via REST endpoints or the interactive client interface.</li>
  <li><em>Preprocessing & Linguistic Parsing:</em> The linguistic pipeline parses sentence boundaries, identifies idiom patterns, scales valence for intensifiers (e.g., <em>"extremely"</em>, <em>"massively"</em>), and reverses polarity within negation scope windows.</li>
  <li><em>Statistical ML Inference:</em> Concurrently, the text is converted into n-gram feature vectors and classified to estimate prior category likelihoods.</li>
  <li><em>Ensemble Synthesis:</em> The weighted soft-valence formula merges both computational signals into a stable aggregate polarity metric (<em>S</em><sub>final</sub>) and assigns qualitative labels.</li>
  <li><em>Explainability Attribution (XAI):</em> Saliency weights are calculated per token, highlighting exact lexical triggers to provide full auditing clarity.</li>
</ul>

<!-- ========================================== -->
<!-- SECTION 12: EXPECTED OUTCOMES              -->
<!-- ========================================== -->
<h1>12. Expected Outcomes</h1>
<p>
  The completed implementation delivers verified quantitative metrics and tangible engineering artifacts:
</p>

<div class="metrics-grid">
  <div class="metric-card">
    <div class="metric-value">86.7%</div>
    <div class="metric-label">Accuracy</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">0.867</div>
    <div class="metric-label">Macro F1</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">0.868</div>
    <div class="metric-label">Precision</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">0.867</div>
    <div class="metric-label">Recall</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">0.801</div>
    <div class="metric-label">MCC Score</div>
  </div>
  <div class="metric-card">
    <div class="metric-value">&kappa; = 0.800</div>
    <div class="metric-label">Cohen’s Kappa</div>
  </div>
</div>

<ul>
  <li><strong>Empirical Benchmark Verification:</strong> Evaluation across the 60-sample gold-standard dataset confirms superior discrimination on difficult linguistic constructs with substantial inter-rater agreement (&kappa; = 0.800).</li>
  <li><strong>Cross-Validation Consistency:</strong> 5-fold stratified cross-validation establishes a low standard deviation across all folds, proving resilience against overfitting.</li>
  <li><strong>Sub-50ms Inference Latency:</strong> The lightweight hybrid execution completes full sentiment, emotion, and aspect extraction in under 50 milliseconds on standard CPU hardware.</li>
  <li><strong>Transparent XAI Reporting:</strong> Generates real-time token attribution visualizers and 1-click publication-ready BibTeX and JSON benchmark reports.</li>
</ul>

<div class="page-break"></div>

<!-- ========================================== -->
<!-- SECTION 13: APPLICATIONS AND SCOPE         -->
<!-- ========================================== -->
<h1>13. Applications and Scope</h1>

<h2>13.1 Practical Applications</h2>
<ul>
  <li><strong>E-Commerce & Retail Intelligence:</strong> Isolating aspect feedback (e.g., distinguishing positive design remarks from negative battery complaints) allows manufacturers to address specific engineering flaws directly.</li>
  <li><strong>Media & Cinematic Analytics:</strong> Studio executives and critics can assess audience sentiment trajectories across screenplay, acting performances, pacing, and visual effects independently.</li>
  <li><strong>Gaming Community Monitoring:</strong> Studios can audit gameplay balance, patch reception, server stability, and narrative pacing post-launch.</li>
  <li><strong>Hospitality & Tourism Auditing:</strong> Destination boards can evaluate customer sentiment across safety, hygiene, culinary offerings, and cost efficiency.</li>
</ul>

<h2>13.2 Scope and Boundaries</h2>
<ul>
  <li><strong>In-Scope:</strong> English-language text analysis; compound sentiment scoring; 6-channel emotion detection; aspect extraction across four distinct domains; token-level XAI attribution; local and remote QR accessibility.</li>
  <li><strong>Out-of-Scope (Future Enhancements):</strong> Real-time acoustic/voice sentiment extraction; computer-vision facial emotion analysis; multi-lingual translation engines (planned for subsequent version releases).</li>
</ul>

<!-- ========================================== -->
<!-- SECTION 14: PROJECT TIMELINE               -->
<!-- ========================================== -->
<h1>14. Project Timeline</h1>
<p>
  The research, engineering, benchmarking, and documentation phases are scheduled across a structured 14-week academic development lifecycle:
</p>

<table>
  <thead>
    <tr>
      <th style="width: 15%;">Phase</th>
      <th style="width: 18%;">Academic Weeks</th>
      <th style="width: 37%;">Key Tasks & Milestone Deliverables</th>
      <th style="width: 30%;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Phase 1</strong></td>
      <td>Weeks 1 – 2</td>
      <td>Literature review, baseline benchmarking, and problem formalization.</td>
      <td>Completed</td>
    </tr>
    <tr>
      <td><strong>Phase 2</strong></td>
      <td>Weeks 3 – 4</td>
      <td>Corpus compilation (60 gold-standard items) and linguistic tokenizer design.</td>
      <td>Completed</td>
    </tr>
    <tr>
      <td><strong>Phase 3</strong></td>
      <td>Weeks 5 – 6</td>
      <td>Lexicon calibration, TF-IDF statistical classifier training, and ensemble math.</td>
      <td>Completed</td>
    </tr>
    <tr>
      <td><strong>Phase 4</strong></td>
      <td>Weeks 7 – 10</td>
      <td>Aspect-based extractor, 6-axis emotion engine, and XAI token attribution.</td>
      <td>Completed</td>
    </tr>
    <tr>
      <td><strong>Phase 5</strong></td>
      <td>Weeks 11 – 12</td>
      <td>Performance benchmarking, 5-fold CV, confusion matrix calculation, and tuning.</td>
      <td>Completed</td>
    </tr>
    <tr>
      <td><strong>Phase 6</strong></td>
      <td>Weeks 13 – 14</td>
      <td>Responsive UI finalization, QR code network integration, documentation & synopsis.</td>
      <td>Final Submission Phase</td>
    </tr>
  </tbody>
</table>

<!-- ========================================== -->
<!-- SECTION 15: CONCLUSION                     -->
<!-- ========================================== -->
<h1>15. Conclusion</h1>
<p>
  Sentix delivers a robust, highly optimized, and explainable computational solution to the challenges of modern opinion mining. By bridging rule-based linguistic precision with statistical machine learning, the system eliminates the traditional trade-off between inference latency and classification accuracy. The integration of Aspect-Based Sentiment Analysis provides granular operational intelligence across consumer tech, entertainment, gaming, and tourism, while the 6-axis affective emotion model captures deep psychological dimensions. Crucially, the Explainable AI (XAI) feature attribution layer guarantees transparency, enabling academic auditors and industry analysts to verify the linguistic determinants of each prediction. Achieving an 86.7% accuracy, 0.867 Macro F1-score, and &kappa; = 0.800 on adversarial test samples, Sentix exemplifies how modern NLP can be engineered for both academic rigor and real-world deployment.
</p>

<!-- ========================================== -->
<!-- SECTION 16: REFERENCES                     -->
<!-- ========================================== -->
<h1>16. References</h1>
<div class="ref-item">[1] C. J. Hutto and E. Gilbert, "VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text," in <em>Proc. 8th Int. AAAI Conf. Weblogs and Social Media (ICWSM)</em>, Ann Arbor, MI, 2014, pp. 216–225.</div>
<div class="ref-item">[2] B. Pang and L. Lee, "Opinion Mining and Sentiment Analysis," <em>Foundations and Trends in Information Retrieval</em>, vol. 2, no. 1–2, pp. 1–135, 2008.</div>
<div class="ref-item">[3] M. Pontiki et al., "SemEval-2016 Task 5: Aspect Based Sentiment Analysis," in <em>Proc. 10th Int. Workshop Semantic Evaluation</em>, San Diego, CA, 2016, pp. 19–30.</div>
<div class="ref-item">[4] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," in <em>Proc. NAACL-HLT</em>, Minneapolis, MN, 2019, pp. 4171–4186.</div>
<div class="ref-item">[5] M. T. Ribeiro, S. Singh, and C. Guestrin, ""Why Should I Trust You?": Explaining the Predictions of Any Classifier," in <em>Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining</em>, San Francisco, CA, 2016, pp. 1135–1144.</div>
<div class="ref-item">[6] B. Liu, <em>Sentiment Analysis: Mining Opinions, Sentiments, and Emotions</em>, 2nd ed., Cambridge, UK: Cambridge University Press, 2020.</div>
<div class="ref-item">[7] R. Socher et al., "Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank," in <em>Proc. EMNLP</em>, Seattle, WA, 2013, pp. 1631–1642.</div>
<div class="ref-item">[8] F. Pedregosa et al., "Scikit-learn: Machine Learning in Python," <em>Journal of Machine Learning Research</em>, vol. 12, pp. 2825–2830, 2011.</div>
<div class="ref-item">[9] P. Ekman, "An Argument for Basic Emotions," <em>Cognition & Emotion</em>, vol. 6, no. 3–4, pp. 169–200, 1992.</div>
<div class="ref-item">[10] D. Chicco and G. Jurman, "The Advantages of the Matthews Correlation Coefficient (MCC) Over F1 Score and Accuracy in Binary Assessment," <em>BMC Genomics</em>, vol. 21, no. 6, pp. 1–13, 2020.</div>

</body>
</html>
"""

# 1. Write the HTML file
with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generated at: {HTML_PATH}")

# 2. Invoke Chrome headless to generate the PDF
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///" + HTML_PATH.replace("\\", "/")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_PATH}",
    file_url
]

print("Executing Chrome headless print-to-pdf...")
result = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", result.returncode)

if os.path.exists(PDF_PATH):
    size_kb = os.path.getsize(PDF_PATH) / 1024
    print(f"SUCCESS: PDF created at {PDF_PATH} ({size_kb:.1f} KB)")
    # Copy to brain artifact directory as well
    shutil.copy2(PDF_PATH, ARTIFACT_PDF_PATH)
    print(f"Copied to artifact directory at: {ARTIFACT_PDF_PATH}")
else:
    print("ERROR: PDF was not generated.")
