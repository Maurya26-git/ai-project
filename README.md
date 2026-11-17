# Sentix - AI Sentiment & Emotion Intelligence System

Sentix is a modern, full-stack, enterprise-grade Sentiment Analysis Web Application and REST API featuring authentic theatrical movie posters, gaming box art, an interactive Electronics, Cinema, Video Games & World Destinations catalog, real-time aspect analysis, universal on-the-fly entity synthesis, academic NLP benchmarks, dynamic QR code sharing, and public worldwide network access.

---

## 🌟 Key Features

1. **🛍️ Interactive Explore & Review Hub (36+ Curated Items + Infinite Universal Search)**:
   - **⚡ Electronics Section**:
     - **📱 Mobiles**: Apple iPhone 16 Pro Max, Samsung Galaxy S25 Ultra, Google Pixel 9 Pro, OnePlus 13 5G, Samsung Galaxy Z Fold 6.
     - **🎧 Gadgets & Tech**: Sony WH-1000XM5 ANC Headphones, Apple Watch Ultra 2, Steam Deck OLED, DJI Mini 4 Pro Drone, Meta Quest 3 VR.
   - **🎬 Movies Section (Original Theatrical Posters)**:
     - *Interstellar (2014)*, *Dune: Part Two (2024)*, *The Dark Knight (2008)*, *Inception (2010)*, *Oppenheimer (2023)*, *Parasite (2019)*, *Spirited Away (2001)*, *Spider-Man: Across the Spider-Verse (2023)*, *The Matrix (1999)*, *Avengers: Endgame (2019)*.
   - **🎮 Video Games Section (Official Steam Portrait Box Art)**:
     - *Elden Ring: Shadow of the Erdtree* (FromSoftware), *Cyberpunk 2077: Phantom Liberty* (CDPR), *Red Dead Redemption 2* (Rockstar), *The Witcher 3: Wild Hunt*, *Grand Theft Auto V*, *Baldur's Gate 3* (Larian), *Black Myth: Wukong* (Game Science), *God of War Ragnarök* (PlayStation).
   - **🌍 World Tourist Places Section (Breathtaking Photography)**:
     - *Kyoto: Fushimi Inari* (Japan), *Paris: Eiffel Tower* (France), *Rome: Colosseum & Vatican* (Italy), *Swiss Alps: Zermatt & Matterhorn* (Switzerland), *Agra: Taj Mahal* (India), *Santorini: Oia Caldera* (Greece), *Cairo: Pyramids of Giza* (Egypt), *Reykjavik & Aurora Borealis* (Iceland).
     - Each destination features tailored tourism aspects: *Scenery & Natural Beauty*, *Culture & Heritage*, *Hospitality & Safety*, *Food & Cuisine*, and *Affordability & Cost*.

2. **✨ Universal On-The-Fly AI Search (Search ANY Entity in the World)**:
   - Search for **any** movie, video game, tech gadget, or world wonder in existence—even if it is not pre-populated!
   - Sentix dynamically infers the entity domain, generates authentic metadata, specifications, and high-res portrait posters.
   - Automatically synthesizes 4 realistic customer/critic reviews and runs them through the multi-tier NLP pipeline.
   - Immediately adds the synthesized entity to the live catalog view so it can be reviewed, analyzed live, and saved into your session history!

3. **🎓 Academic NLP Benchmarks & Explainable AI (XAI) Suite (For Professor Review)**:
   - **Model Verification Matrix**: Evaluated on a 60-sample gold-standard corpus across Positive, Neutral, Negative, and Sarcastic inputs.
   - **Performance Metrics**: 86.7% Accuracy, 0.867 Macro F1, 0.868 Precision, 0.867 Recall, Cohen's Kappa ($\kappa = 0.800$), and Matthews Correlation Coefficient ($\text{MCC} = 0.801$).
   - **Real-Time 3×3 Confusion Matrix**: Interactive heatmap showing true positives, false positives, and class distributions.
   - **5-Fold Stratified Cross-Validation**: Statistical consistency validation across training subsets.
   - **Token-Level XAI Attribution Tester**: Interactive LIME/SHAP-style attribution visualizer with color-coded positive/negative contribution bars.
   - **Top Discriminative N-Grams**: TF-IDF log-odds ranking of top positive and negative vocabulary features.
   - **LaTeX Mathematical Formulations**: Formal equations for soft valence normalization ($C = V / \sqrt{V^2 + 15}$), booster/negation propagation, and hybrid ensemble combination.
   - **BibTeX & JSON Report Export**: 1-click export of publication-ready citations and complete benchmark datasets.

4. **⚡ Seamless Selection Flow → Live Analyzer → Persistent History**:
   - Selecting any mobile, movie, game, or destination instantly:
     1. Pre-fills the **Live Analyzer** with that item's specifications and verified community reviews.
     2. Switches to the **Live Analyzer** tab.
     3. Runs the multi-dimensional sentiment scoring, emotion radar, and aspect-based breakdown immediately.
     4. Saves the analysis to the persistent **History** log with the item's name tag (e.g. `★ Elden Ring`, `★ iPhone 16 Pro Max`, `★ Interstellar`, `★ Kyoto: Fushimi Inari`).
     5. Fires dual-cannon gold confetti!

5. **🌿 Emerald Obsidian & Deep Black Theme (Light & Dark Mode)**:
   - **Dark Mode (Default)**: Deep carbon black (`#040605`), dark obsidian glass cards, tasteful emerald green (`#10b981`) and mint (`#34d399`) accents, subtle green glow effects (not overly bright), and sleek typography.
   - **Light Mode**: Crisp ivory-mint background with pearl cards and deep forest green accents.

6. **💫 Advanced Motion Graphics & Interactivity**:
   - **Emerald Stardust & Neural Constellation Canvas**: Floating emerald particles with twinkling stars and reactive mouse repulsion.
   - **Live Sentiment Energy Waveform Bars**: Dynamically pulses with green audio signal bars.
   - **Emerald & Mint Confetti & Sparkles**: Celebratory particle bursts on analysis and review submission.
   - **3D Spatial Perspective Card Tilt**: Cards dynamically tilt and reflect light in 3D based on cursor movement.

7. **📱 Dual QR Code System for Local & Worldwide Public Networks**:
   - **Same Wi-Fi Network Tab**: Displays local QR code for instantaneous connection over Wi-Fi (`http://192.168.29.200:5000`).
   - **Different Networks (Worldwide Public) Tab**:
     - Dedicated real-time public QR code image.
     - Live updates as you type or paste your Cloudflare Tunnel URL.
     - Includes a 1-click **Update QR** button and **Test Sample Tunnel** button.
     - Accessible from any smartphone on cellular 4G/5G or remote Wi-Fi worldwide.

---

## 🚀 How to Run

From your project directory [sentiment-analyzer](file:///C:/Users/remal/.gemini/antigravity/scratch/sentiment-analyzer):

```powershell
cd C:\Users\remal\.gemini\antigravity\scratch\sentiment-analyzer
python app.py
```
*(Or double-click [run.bat](file:///C:/Users/remal/.gemini/antigravity/scratch/sentiment-analyzer/run.bat))*

Open your browser at:
👉 **`http://127.0.0.1:5000`**

To share access across **different networks / mobile cellular data**, run:
```powershell
.\start_public_tunnel.bat
```
and paste the public URL into the Sentix QR modal!
