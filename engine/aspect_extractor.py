"""
Aspect-Based Sentiment Analysis (ABSA) Engine
Extracts domain entities and evaluates sentiment specifically associated with each aspect.
"""
import re

COMMON_ASPECTS = {
    "Battery & Power": [
        "battery", "battery life", "charging", "charger", "charge", "power", "runtime"
    ],
    "Performance & Speed": [
        "performance", "speed", "fast", "slow", "processor", "chip", "lag", "laggy",
        "smoothness", "framerate", "fps", "response time", "multitasking"
    ],
    "Display & Screen": [
        "screen", "display", "resolution", "brightness", "oled", "amoled", "colors",
        "refresh rate", "touchscreen", "panel", "viewing angle"
    ],
    "Camera & Imaging": [
        "camera", "photo", "photos", "picture", "pictures", "video", "lens", "zoom",
        "night mode", "portrait", "sensor", "image quality"
    ],
    "Audio & Sound": [
        "sound", "audio", "speaker", "speakers", "microphone", "mic", "volume",
        "bass", "treble", "headphones", "clarity", "noise cancelling", "anc"
    ],
    "Build Quality & Design": [
        "build", "design", "look", "looks", "material", "materials", "durability",
        "finish", "weight", "ergonomics", "feel", "case", "sturdy", "compact"
    ],
    "Customer Support": [
        "support", "customer service", "staff", "representative", "helpdesk",
        "assistance", "agent", "refund", "warranty", "response"
    ],
    "Price & Value": [
        "price", "cost", "value", "expensive", "cheap", "affordable", "deal",
        "bargain", "worth", "pricing", "money"
    ],
    "Shipping & Delivery": [
        "shipping", "delivery", "packaging", "package", "arrived", "courier",
        "transit", "dispatch"
    ],
    "Software & Interface": [
        "software", "app", "application", "ui", "interface", "navigation", "bug",
        "bugs", "update", "updates", "setup", "installation", "features"
    ],
    "Gameplay & Combat": [
        "gameplay", "combat", "mechanics", "controls", "boss", "bosses", "moveset",
        "gunplay", "handling", "difficulty", "mechanic"
    ],
    "Graphics & Visuals": [
        "graphics", "visuals", "cinematography", "vfx", "cgi", "textures", "ray tracing",
        "art style", "visual effects", "fidelity", "resolution"
    ],
    "Story & Narrative": [
        "story", "plot", "lore", "writing", "characters", "narrative", "dialogue",
        "storyline", "ending", "script", "twist"
    ],
    "Performance & Optimization": [
        "fps", "framerate", "optimization", "stutter", "crashes", "bugs", "glitches",
        "loading times", "optimized"
    ],
    "Soundtrack & Audio": [
        "soundtrack", "ost", "score", "music", "audio", "voice acting", "sound design",
        "composer"
    ],
    "World & Exploration": [
        "world", "exploration", "open world", "map", "environment", "quest", "quests",
        "immersion", "atmosphere", "side quests"
    ],
    "Direction & Acting": [
        "acting", "actor", "actress", "performance", "performances", "direction",
        "director", "pacing", "cast"
    ]
}

class AspectExtractor:
    def __init__(self, valence_dict=None):
        self.aspect_catalogs = COMMON_ASPECTS
        self.valence = valence_dict or {}

    def extract_aspects(self, text: str, word_valences: dict) -> list:
        if not text or not text.strip():
            return []

        text_lower = text.lower()
        # Split text into sentence clauses (by punctuation and contrastive conjunctions)
        clauses = re.split(r'[,;.!?]|\b(?:but|however|although|though|except|yet)\b', text_lower)
        found_aspects = []
        seen_aspect_names = set()

        for clause in clauses:
            clause = clause.strip()
            if not clause:
                continue

            # Check which aspect belongs to this clause
            for category, keywords in self.aspect_catalogs.items():
                if category in seen_aspect_names:
                    continue

                for kw in keywords:
                    pattern = r'\b' + re.escape(kw) + r'\b'
                    if re.search(pattern, clause):
                        # Calculate sentiment score for this specific clause
                        clause_score = self._score_clause(clause, word_valences)
                        
                        label = "Neutral"
                        if clause_score >= 0.15:
                            label = "Positive"
                        elif clause_score <= -0.15:
                            label = "Negative"

                        found_aspects.append({
                            "aspect": category,
                            "keyword": kw,
                            "sentiment": label,
                            "score": round(clause_score, 2),
                            "clause": clause[:80] + ("..." if len(clause) > 80 else "")
                        })
                        seen_aspect_names.add(category)
                        break

        # If no standard aspect category matched, extract generic key nouns if sentiment words surround them
        if not found_aspects:
            found_aspects = self._extract_generic_aspects(text_lower, word_valences)

        return found_aspects

    def _score_clause(self, clause: str, word_valences: dict) -> float:
        words = re.findall(r'\b[a-z\'-]+\b', clause)
        if not words:
            return 0.0

        score = 0.0
        negated = False
        intensifier = 1.0

        for w in words:
            if w in {"not", "never", "no", "hardly", "barely", "isn't", "wasn't", "doesn't", "won't", "cannot"}:
                negated = True
                continue
            if w in {"very", "extremely", "super", "really", "incredibly", "absolutely"}:
                intensifier = 1.4
                continue

            v = word_valences.get(w, 0.0)
            if v != 0.0:
                if negated:
                    v = -v * 0.8
                    negated = False
                v *= intensifier
                intensifier = 1.0
                score += v

        # Normalize score between -1.0 and 1.0
        normalized = score / max(1.0, len(words) * 0.4)
        return max(-1.0, min(1.0, normalized))

    def _extract_generic_aspects(self, text: str, word_valences: dict) -> list:
        # Heuristic search for "ADJ NOUN" or "NOUN is ADJ"
        aspects = []
        sentences = re.split(r'[.!?]+', text)
        for s in sentences:
            tokens = re.findall(r'\b[a-z]{3,}\b', s)
            for i, tok in enumerate(tokens):
                v = word_valences.get(tok, 0.0)
                if abs(v) >= 1.5:
                    # Look at adjacent tokens
                    target_words = []
                    if i > 0:
                        target_words.append(tokens[i-1])
                    if i < len(tokens) - 1:
                        target_words.append(tokens[i+1])
                    
                    for candidate in target_words:
                        if candidate not in word_valences and len(candidate) > 3:
                            sentiment = "Positive" if v > 0 else "Negative"
                            aspects.append({
                                "aspect": candidate.capitalize(),
                                "keyword": candidate,
                                "sentiment": sentiment,
                                "score": round(v / 4.0, 2),
                                "clause": f"...{candidate} is {tok}..."
                            })
                            if len(aspects) >= 3:
                                return aspects
        return aspects
