"""
Sentix - Modern Sentiment Analysis Web Application & API Server
Enhanced with Interactive Catalog (Electronics & Movies), Review Engine,
Dynamic QR Code Generator, and Network Discovery.
"""
import os
import io
import csv
import json
import time
import socket
from flask import Flask, request, jsonify, render_template, send_from_directory, Response
import qrcode
import qrcode.image.svg

from engine.analyzer import SentimentAnalyzer
from engine.catalog_data import CATALOG_ITEMS
from engine.universal_search import synthesize_entity_dossier
from engine.academic_benchmarks import (
    run_academic_evaluation,
    explain_text_attribution,
    get_lexical_feature_weights,
    get_academic_citation
)

app = Flask(__name__, static_folder='static', template_folder='templates')
analyzer = SentimentAnalyzer()

START_TIME = time.time()

# Deep copy of catalog to store live reviews added by users during runtime
LIVE_CATALOG = json.loads(json.dumps(CATALOG_ITEMS))

def get_local_ip():
    """Detect the machine's local IPv4 address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

LOCAL_IP = get_local_ip()

def compute_item_sentiment(item):
    """Compute aggregate sentiment metrics across all reviews for an item."""
    reviews = item.get("reviews", [])
    if not reviews:
        return {
            "score": 0.0,
            "label": "Neutral",
            "pos_percent": 50,
            "neg_percent": 20,
            "neu_percent": 30,
            "dominant_emotion": "Neutral",
            "review_count": 0,
            "aspects": []
        }

    comp_sum = 0.0
    pos_c = 0
    neg_c = 0
    neu_c = 0
    emotions_map = {}
    aspects_map = {}

    processed_reviews = []
    for r in reviews:
        # Check if already analyzed, otherwise analyze
        if "sentiment_analysis" not in r:
            analysis = analyzer.analyze(r["text"])
            r["sentiment_analysis"] = {
                "label": analysis["overall"]["label"],
                "compound_score": analysis["overall"]["compound_score"],
                "theme_color": analysis["overall"]["theme_color"],
                "dominant_emotion": analysis["emotions"]["dominant"],
                "tokens": analysis["tokens"],
                "aspects": analysis["aspects"]
            }

        s = r["sentiment_analysis"]
        comp = s["compound_score"]
        comp_sum += comp

        if "Positive" in s["label"]:
            pos_c += 1
        elif "Negative" in s["label"]:
            neg_c += 1
        else:
            neu_c += 1

        emo = s["dominant_emotion"]
        emotions_map[emo] = emotions_map.get(emo, 0) + 1

        for asp in s["aspects"]:
            name = asp["aspect"]
            if name not in aspects_map:
                aspects_map[name] = {"sum": 0.0, "count": 0}
            aspects_map[name]["sum"] += asp["score"]
            aspects_map[name]["count"] += 1

        processed_reviews.append(r)

    total = len(reviews)
    avg_compound = round(comp_sum / total, 2)
    pos_pct = round((pos_c / total) * 100)
    neg_pct = round((neg_c / total) * 100)
    neu_pct = 100 - pos_pct - neg_pct

    # Determine dominant emotion
    dom_emotion = max(emotions_map.items(), key=lambda x: x[1])[0] if emotions_map else "Joy"

    # Aggregated aspects
    aspect_list = []
    for name, data in aspects_map.items():
        avg_asp_score = round(data["sum"] / data["count"], 2)
        aspect_list.append({
            "aspect": name,
            "score": avg_asp_score,
            "sentiment": "Positive" if avg_asp_score > 0.1 else ("Negative" if avg_asp_score < -0.1 else "Neutral")
        })

    # Overall label
    if avg_compound >= 0.5:
        lbl = "Strongly Positive"
        theme = "#10B981"
    elif avg_compound >= 0.1:
        lbl = "Positive"
        theme = "#34D399"
    elif avg_compound <= -0.5:
        lbl = "Strongly Negative"
        theme = "#EF4444"
    elif avg_compound <= -0.1:
        lbl = "Negative"
        theme = "#F87171"
    else:
        lbl = "Neutral"
        theme = "#94A3B8"

    return {
        "score": avg_compound,
        "label": lbl,
        "theme_color": theme,
        "pos_percent": pos_pct,
        "neu_percent": neu_pct,
        "neg_percent": neg_pct,
        "dominant_emotion": dom_emotion,
        "review_count": total,
        "aspects": aspect_list,
        "reviews": processed_reviews
    }


# Precompute initial sentiment on startup
for it_id, it_obj in LIVE_CATALOG.items():
    it_obj["sentiment"] = compute_item_sentiment(it_obj)

# Predefined single preset samples
PRESET_SAMPLES = [
    {
        "id": "tech_review",
        "category": "Tech Hardware",
        "title": "Smartphone Mixed Review",
        "badge": "Mixed Nuance",
        "text": "The camera on this phone is truly phenomenal with breathtaking low-light shots and crisp 4K video! The OLED screen is radiant and super responsive. However, the battery life drains in less than 5 hours with regular use, and customer service was completely rude and unhelpful when I requested a replacement charger."
    },
    {
        "id": "glowing_review",
        "category": "E-Commerce",
        "title": "5-Star Noise Cancelling Headphones",
        "badge": "Strongly Positive",
        "text": "Hands down the best purchase I have made all year! 🎧 The active noise cancelling is pure magic on noisy flights, the soundstage is warm with punchy bass, and the battery easily lasts 30+ hours. Worth every single penny! Highly recommended! 🚀✨"
    },
    {
        "id": "angry_ticket",
        "category": "Customer Support",
        "title": "Cancelled Flight Support Rant",
        "badge": "Strongly Negative",
        "text": "Worst experience of my entire life. Our flight was abruptly cancelled without any notification, we waited 4 hours in the freezing cold, and the gate agent refused to issue a refund or hotel voucher. Utterly appalling and unacceptable treatment. I am demanding a full refund and compensation immediately! 😡🤬"
    },
    {
        "id": "sarcastic_tweet",
        "category": "Social Media",
        "title": "Sarcastic OS Update Reaction",
        "badge": "Sarcasm Detected",
        "text": "Oh wonderful, another mandatory software update that took 45 minutes to install and managed to break Bluetooth and delete my custom shortcuts! Just what I needed before my morning presentation. Truly brilliant engineering! 👏🙄"
    },
    {
        "id": "saas_b2b",
        "category": "Enterprise B2B",
        "title": "Project Management Tool Review",
        "badge": "Constructive",
        "text": "The automation workflows and real-time sprint boards have saved our team dozens of hours each week. The UI is clean, modern, and intuitive. However, the reporting export to CSV is slightly clunky and could use more customizable filtering options."
    },
    {
        "id": "movie_critic",
        "category": "Entertainment",
        "title": "Sci-Fi Film Critique",
        "badge": "Appreciative",
        "text": "A visually spectacular cinematic triumph! The director crafts an immaculate dystopian atmosphere accompanied by an evocative, haunting musical score. While the pacing during the second act is slightly slow, the triumphant finale more than makes up for it."
    }
]

# Sample Batch Dataset
SAMPLE_BATCH_DATA = [
    {"id": 1, "source": "Amazon", "aspect": "Audio", "text": "Unbelievable sound clarity and booming bass! Best headphones ever. 5/5 stars!"},
    {"id": 2, "source": "Amazon", "aspect": "Build", "text": "Cheap plastic hinge snapped within two weeks. Very disappointing and fragile."},
    {"id": 3, "source": "Twitter", "aspect": "Delivery", "text": "Package arrived on Wednesday as indicated in the shipping tracking."},
    {"id": 4, "source": "Support", "aspect": "Service", "text": "Sarah from customer support resolved my refund in under 2 minutes. Wonderful service!"},
    {"id": 5, "source": "Twitter", "aspect": "Software", "text": "Oh fantastic, another app crash right when I was finishing checkout. Amazing... /s"},
    {"id": 6, "source": "Website", "aspect": "Pricing", "text": "Great value for money. Significantly more affordable than competing brands."},
    {"id": 7, "source": "Support", "aspect": "Service", "text": "Held on the phone for 45 minutes only to be disconnected. Infuriatingly poor service."},
    {"id": 8, "source": "Amazon", "aspect": "Battery", "text": "Battery life lasts easily 3 days on a single charge. Super convenient!"},
    {"id": 9, "source": "Reddit", "aspect": "Display", "text": "The screen is bright, crisp, and vibrant even outdoors under sunlight."},
    {"id": 10, "source": "Website", "aspect": "Usability", "text": "Setup was straightforward, took less than five minutes with clear instructions."}
]


@app.route('/')
def index():
    return render_template('index.html', local_ip=LOCAL_IP)


@app.route('/api/analyze', methods=['POST'])
def analyze_single():
    try:
        data = request.get_json(force=True, silent=True) or {}
        text = data.get("text", "")
        gemini_api_key = data.get("gemini_api_key", None)

        if not text or not text.strip():
            return jsonify({"success": False, "error": "Text cannot be empty."}), 400

        result = analyzer.analyze(text, gemini_api_key=gemini_api_key)
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# =============================================================================
# CATALOG & INTERACTIVE REVIEW APIS (ELECTRONICS & MOVIES)
# =============================================================================
@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    """List catalog items filtered by type, category, or search query."""
    item_type = request.args.get('type', None) # 'electronics' or 'movie'
    category = request.args.get('category', None) # 'mobiles', 'gadgets', 'sci-fi', etc.
    search = request.args.get('search', '').strip().lower()

    items_list = []
    for it_id, it in LIVE_CATALOG.items():
        if item_type and it.get('type') != item_type:
            continue
        if category and category != 'all' and it.get('category') != category:
            continue
        if search:
            combined_text = f"{it.get('title', '')} {it.get('tagline', '')} {it.get('category_label', '')}".lower()
            if search not in combined_text:
                continue

        # Prepare summary item
        summary_item = {
            "id": it["id"],
            "type": it["type"],
            "category": it["category"],
            "category_label": it["category_label"],
            "title": it["title"],
            "tagline": it["tagline"],
            "badge": it["badge"],
            "rating": it["rating"],
            "price": it.get("price"),
            "director": it.get("director"),
            "duration": it.get("duration"),
            "image": it["image"],
            "sentiment": it["sentiment"]
        }
        items_list.append(summary_item)

    return jsonify({
        "success": True,
        "count": len(items_list),
        "items": items_list
    })


@app.route('/api/catalog/<item_id>', methods=['GET'])
def get_catalog_item(item_id):
    """Retrieve full details, reviews, and aggregated sentiment for one item."""
    item = LIVE_CATALOG.get(item_id)
    if not item:
        return jsonify({"success": False, "error": f"Item '{item_id}' not found."}), 404

    # Ensure sentiment is up to date
    item["sentiment"] = compute_item_sentiment(item)
    return jsonify({"success": True, "item": item})


@app.route('/api/catalog/<item_id>/review', methods=['POST'])
def add_catalog_review(item_id):
    """Submit a user review for an item, analyze it instantly, and update aggregate sentiment."""
    item = LIVE_CATALOG.get(item_id)
    if not item:
        return jsonify({"success": False, "error": f"Item '{item_id}' not found."}), 404

    data = request.get_json(force=True, silent=True) or {}
    text = data.get("text", "").strip()
    author = data.get("author", "Verified Reviewer").strip() or "Verified Reviewer"
    rating = int(data.get("rating", 5))

    if not text:
        return jsonify({"success": False, "error": "Review text cannot be empty."}), 400

    # Run Sentix sentiment analysis on the user's review
    analysis = analyzer.analyze(text)

    new_review = {
        "id": f"usr_{int(time.time()*1000)}",
        "author": author,
        "rating": rating,
        "date": "Just now",
        "text": text,
        "sentiment_analysis": {
            "label": analysis["overall"]["label"],
            "compound_score": analysis["overall"]["compound_score"],
            "theme_color": analysis["overall"]["theme_color"],
            "dominant_emotion": analysis["emotions"]["dominant"],
            "tokens": analysis["tokens"],
            "aspects": analysis["aspects"]
        }
    }

    # Prepend new review
    item.setdefault("reviews", []).insert(0, new_review)

    # Recalculate item-level sentiment
    item["sentiment"] = compute_item_sentiment(item)

    return jsonify({
        "success": True,
        "message": "Review submitted and analyzed successfully!",
        "review": new_review,
        "item_sentiment": item["sentiment"],
        "detailed_analysis": analysis
    })


# =============================================================================
# UNIVERSAL SEARCH & ON-THE-FLY ENTITY SYNTHESIS
# =============================================================================
@app.route('/api/universal-search', methods=['GET', 'POST'])
def universal_search():
    """
    Search for ANY entity across movies, games, gadgets, and world destinations.
    If the entity is in LIVE_CATALOG, returns it. If not, dynamically synthesizes
    an authentic dossier with realistic specs, high-res posters, and pre-analyzed reviews!
    """
    if request.method == 'POST':
        data = request.get_json(force=True, silent=True) or {}
        query = data.get('query') or data.get('q', '')
        force = data.get('force', False)
    else:
        query = request.args.get('q', '').strip()
        force = request.args.get('force', 'false').lower() == 'true'

    if not query:
        return jsonify({"success": False, "error": "Query parameter 'q' is required."}), 400

    q_lower = query.lower()

    # If not forcing synthesis, check if an existing item matches title or id
    if not force:
        for it_id, it in LIVE_CATALOG.items():
            if q_lower == it_id.lower() or q_lower == it.get('title', '').lower():
                it['sentiment'] = compute_item_sentiment(it)
                return jsonify({"success": True, "source": "existing", "item": it})

    # Synthesize entity on the fly
    synthesized_item = synthesize_entity_dossier(query, analyzer, compute_item_sentiment)

    # Cache into LIVE_CATALOG so it persists, can be reviewed, and appears in catalog
    LIVE_CATALOG[synthesized_item['id']] = synthesized_item

    return jsonify({
        "success": True,
        "source": "synthesized",
        "item": synthesized_item
    })


# =============================================================================
# ACADEMIC NLP BENCHMARKS & EXPLAINABLE AI (XAI)
# =============================================================================
@app.route('/api/academic-metrics', methods=['GET', 'POST'])
def academic_metrics():
    """Returns academic NLP evaluation metrics: Accuracy, F1, 3x3 Confusion Matrix, Cross-Validation."""
    res = run_academic_evaluation(analyzer)
    return jsonify(res)


@app.route('/api/academic-explain', methods=['POST'])
def academic_explain():
    """Explainable AI (XAI) token-level attribution bars for any sentence."""
    data = request.get_json(force=True, silent=True) or {}
    text = data.get('text', '').strip()
    if not text:
        return jsonify({"error": "Text is required"}), 400
    res = explain_text_attribution(analyzer, text)
    return jsonify(res)


@app.route('/api/academic-features', methods=['GET'])
def academic_features():
    """Top discriminative positive and negative TF-IDF n-grams."""
    res = get_lexical_feature_weights(analyzer)
    return jsonify(res)


@app.route('/api/academic-citation', methods=['GET'])
def academic_citation():
    """BibTeX citation and LaTeX math specifications."""
    res = get_academic_citation()
    return jsonify(res)


# =============================================================================
# NETWORK DISCOVERY & QR CODE GENERATION
# =============================================================================
@app.route('/api/network-info', methods=['GET'])
def get_network_info():
    """Returns local network details and instructions for worldwide access."""
    port = int(os.environ.get("PORT", 5000))
    return jsonify({
        "success": True,
        "local_ip": LOCAL_IP,
        "port": port,
        "local_url": f"http://{LOCAL_IP}:{port}",
        "tunnel": {
            "recommended_tool": "Cloudflare Tunnel (cloudflared)",
            "command": f"cloudflared tunnel --url http://127.0.0.1:{port}",
            "description": "Zero-config public HTTPS tunnel accessible from any smartphone or cellular network."
        }
    })


@app.route('/api/qrcode', methods=['GET'])
def generate_qr_code():
    """Generates an SVG QR code for any target URL on demand."""
    target_url = request.args.get('url', f"http://{LOCAL_IP}:5000").strip()
    
    factory = qrcode.image.svg.SvgPathImage
    qr_img = qrcode.make(target_url, image_factory=factory, box_size=10, border=2)
    svg_data = qr_img.to_string()

    return Response(
        svg_data,
        mimetype="image/svg+xml",
        headers={"Cache-Control": "no-cache"}
    )


# =============================================================================
# BATCH, COMPARE & UTILITIES
# =============================================================================
@app.route('/api/batch', methods=['POST'])
def analyze_batch():
    try:
        texts_to_process = []
        if 'file' in request.files:
            uploaded_file = request.files['file']
            filename = uploaded_file.filename.lower()
            text_column = request.form.get('column_name', 'text').strip()

            if filename.endswith('.csv'):
                stream = io.StringIO(uploaded_file.stream.read().decode('utf-8', errors='ignore'))
                reader = csv.DictReader(stream)
                fieldnames = reader.fieldnames or []
                chosen_col = None
                for col in [text_column, 'text', 'review', 'comment', 'feedback', 'content', 'message', 'tweet']:
                    for f in fieldnames:
                        if f.strip().lower() == col.lower():
                            chosen_col = f
                            break
                    if chosen_col:
                        break
                
                if not chosen_col and fieldnames:
                    chosen_col = fieldnames[0]

                for idx, row in enumerate(reader):
                    val = row.get(chosen_col, '') if chosen_col else ''
                    if val and val.strip():
                        texts_to_process.append({"id": idx + 1, "text": val.strip(), "meta": row})
                    if len(texts_to_process) >= 500:
                        break

            elif filename.endswith('.json'):
                content = uploaded_file.stream.read().decode('utf-8', errors='ignore')
                raw_json = json.loads(content)
                if isinstance(raw_json, list):
                    for idx, item in enumerate(raw_json):
                        if isinstance(item, str):
                            texts_to_process.append({"id": idx + 1, "text": item.strip(), "meta": {}})
                        elif isinstance(item, dict):
                            val = item.get('text') or item.get('review') or item.get('comment') or str(item)
                            texts_to_process.append({"id": idx + 1, "text": str(val).strip(), "meta": item})
                if len(texts_to_process) >= 500:
                    texts_to_process = texts_to_process[:500]

        else:
            data = request.get_json(force=True, silent=True) or {}
            items = data.get("items", [])
            for idx, item in enumerate(items):
                if isinstance(item, str) and item.strip():
                    texts_to_process.append({"id": idx + 1, "text": item.strip(), "meta": {}})
                elif isinstance(item, dict):
                    t = item.get("text", "")
                    if t and t.strip():
                        texts_to_process.append({"id": idx + 1, "text": t.strip(), "meta": item})

        if not texts_to_process:
            return jsonify({"success": False, "error": "No valid text entries found to analyze."}), 400

        results = []
        pos_count = 0
        neu_count = 0
        neg_count = 0
        compound_sum = 0.0
        emotion_counts = {}
        aspect_counts = {}

        for entry in texts_to_process:
            t = entry["text"]
            analysis = analyzer.analyze(t, gemini_api_key=None)
            label = analysis["overall"]["label"]
            comp = analysis["overall"]["compound_score"]
            compound_sum += comp

            if "Positive" in label:
                pos_count += 1
            elif "Negative" in label:
                neg_count += 1
            else:
                neu_count += 1

            dom_emotion = analysis["emotions"]["dominant"]
            emotion_counts[dom_emotion] = emotion_counts.get(dom_emotion, 0) + 1

            for asp in analysis["aspects"]:
                asp_name = asp["aspect"]
                if asp_name not in aspect_counts:
                    aspect_counts[asp_name] = {"positive": 0, "negative": 0, "neutral": 0}
                aspect_counts[asp_name][asp["sentiment"].lower()] += 1

            results.append({
                "id": entry["id"],
                "text": t,
                "overall": analysis["overall"],
                "ml_model": analysis["ml_model"],
                "dominant_emotion": dom_emotion,
                "top_aspect": analysis["aspects"][0]["aspect"] if analysis["aspects"] else "General",
                "meta": entry["meta"]
            })

        total = len(results)
        pos_pct = round((pos_count / total) * 100, 1)
        neu_pct = round((neu_count / total) * 100, 1)
        neg_pct = round((neg_count / total) * 100, 1)
        avg_compound = round(compound_sum / total, 3)
        nss = round(pos_pct - neg_pct, 1)

        summary = {
            "total": total,
            "positive_count": pos_count,
            "positive_percent": pos_pct,
            "neutral_count": neu_count,
            "neutral_percent": neu_pct,
            "negative_count": neg_count,
            "negative_percent": neg_pct,
            "average_compound": avg_compound,
            "net_sentiment_score": nss,
            "emotions_distribution": emotion_counts,
            "aspects_distribution": aspect_counts
        }

        return jsonify({
            "success": True,
            "summary": summary,
            "results": results
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/compare', methods=['POST'])
def compare_texts():
    try:
        data = request.get_json(force=True, silent=True) or {}
        text_a = data.get("text_a", "").strip()
        text_b = data.get("text_b", "").strip()
        label_a = data.get("label_a", "Item A").strip() or "Item A"
        label_b = data.get("label_b", "Item B").strip() or "Item B"

        if not text_a or not text_b:
            return jsonify({"success": False, "error": "Both text fields are required for comparison."}), 400

        res_a = analyzer.analyze(text_a)
        res_b = analyzer.analyze(text_b)

        delta_compound = round(res_b["overall"]["compound_score"] - res_a["overall"]["compound_score"], 3)
        better_sentiment = label_b if delta_compound > 0 else (label_a if delta_compound < 0 else "Equal")

        return jsonify({
            "success": True,
            "comparison": {
                "label_a": label_a,
                "label_b": label_b,
                "delta_compound": delta_compound,
                "higher_sentiment": better_sentiment,
                "analysis_a": res_a,
                "analysis_b": res_b
            }
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/samples', methods=['GET'])
def get_samples():
    return jsonify({
        "success": True,
        "single_presets": PRESET_SAMPLES,
        "batch_sample": SAMPLE_BATCH_DATA
    })


@app.route('/api/sample-csv', methods=['GET'])
def download_sample_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "source", "aspect", "text"])
    for row in SAMPLE_BATCH_DATA:
        writer.writerow([row["id"], row["source"], row["aspect"], row["text"]])
    
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=sentix_sample_reviews.csv"}
    )


@app.route('/api/stats', methods=['GET'])
def get_stats():
    uptime_sec = round(time.time() - START_TIME)
    return jsonify({
        "success": True,
        "system": "Sentix Sentiment AI Platform",
        "version": "2.5.0",
        "uptime_seconds": uptime_sec,
        "engine": {
            "lexicon_entries": len(analyzer.word_valence) + len(analyzer.emoji_valence),
            "emotions_supported": len(analyzer.emotion_detector.categories),
            "aspect_categories": len(analyzer.aspect_extractor.aspect_catalogs),
            "ml_model": "TF-IDF + Balanced Logistic Regression",
            "gemini_integration": "Google Gemini 2.5 Flash API (Configurable)",
            "catalog_items": len(LIVE_CATALOG)
        }
    })


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "timestamp": time.time()})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Sentix running locally on: http://127.0.0.1:{port}")
    print(f"📱 Local WiFi Network Access: http://{LOCAL_IP}:{port}")
    print(f"🌍 Worldwide Remote Access: Run 'cloudflared tunnel --url http://127.0.0.1:{port}'")
    app.run(host='0.0.0.0', port=port, debug=False)
