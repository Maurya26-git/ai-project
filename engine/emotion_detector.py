"""
Multi-Class Emotion Detection Engine
Categorizes text into 6 primary affective states:
Joy, Sadness, Anger, Fear, Surprise, Trust
"""
import re

EMOTION_KEYWORDS = {
    "Joy": {
        "words": [
            "happy", "joy", "delight", "delighted", "love", "loved", "loving", "excited",
            "thrilled", "wonderful", "amazing", "great", "excellent", "smile", "smiling",
            "laugh", "laughing", "ecstatic", "glad", "celebrate", "pleased", "cheerful",
            "blessed", "enjoy", "enjoyed", "fun", "radiant", "satisfaction", "content"
        ],
        "emojis": ["😀", "😃", "😄", "😁", "😆", "😂", "🤣", "😊", "😍", "🥰", "🥳", "🎉", "✨", "💖", "❤️"],
        "color": "#10B981"  # Emerald green
    },
    "Sadness": {
        "words": [
            "sad", "unhappy", "depressed", "sorrow", "grief", "gloomy", "heartbroken",
            "disappointed", "disappointment", "crying", "tears", "hopeless", "lonely",
            "miserable", "hurt", "pain", "regret", "pity", "mourn", "despair", "down",
            "tragic", "loss", "lost", "ruined", "broken"
        ],
        "emojis": ["😢", "😭", "😔", "😞", "💔", "🙁", "☹️", "🥺", "😓", "😿"],
        "color": "#3B82F6"  # Blue
    },
    "Anger": {
        "words": [
            "angry", "mad", "furious", "outrage", "outraged", "hate", "hated", "rage",
            "annoyed", "annoying", "frustrated", "frustrating", "irritated", "irritating",
            "infuriating", "pissed", "rude", "scam", "cheat", "disgusted", "toxic",
            "offensive", "intolerable", "garbage", "trash", "terrible", "worst", "unacceptable"
        ],
        "emojis": ["😡", "😠", "🤬", "😤", "👿", "🖕", "💢"],
        "color": "#EF4444"  # Red
    },
    "Fear": {
        "words": [
            "fear", "afraid", "scared", "terrified", "panic", "anxious", "anxiety",
            "nervous", "worry", "worried", "dread", "frightened", "horrified", "threat",
            "dangerous", "hazard", "risk", "risky", "uncertain", "alarm", "creepy"
        ],
        "emojis": ["😨", "😰", "😱", "🫣", "😬", "🥶", "⚠️"],
        "color": "#8B5CF6"  # Purple
    },
    "Surprise": {
        "words": [
            "surprise", "surprised", "shocked", "astonished", "stunned", "unexpected",
            "unbelievable", "wonder", "jaw-dropping", "breathtaking", "unreal", "whoa",
            "wow", "mindblown", "sudden", "curious", "intriguing", "remarkable"
        ],
        "emojis": ["😮", "😲", "😯", "🤯", "😳", "🤩", "🫢"],
        "color": "#F59E0B"  # Amber / Yellow
    },
    "Trust": {
        "words": [
            "trust", "reliable", "honest", "recommend", "recommended", "faithful",
            "proven", "solid", "loyal", "guaranteed", "secure", "safe", "confident",
            "authentic", "genuine", "praise", "respect", "grateful", "gratitude", "thank"
        ],
        "emojis": ["🤝", "👌", "🛡️", "✅", "🙌", "💪", "🏆", "💯"],
        "color": "#06B6D4"  # Cyan
    }
}

class EmotionDetector:
    def __init__(self):
        self.categories = EMOTION_KEYWORDS

    def detect(self, text: str) -> dict:
        if not text or not text.strip():
            return {
                "dominant": "Neutral",
                "dominant_color": "#64748B",
                "breakdown": [
                    {"emotion": name, "score": 0.0, "percentage": 0, "color": data["color"]}
                    for name, data in self.categories.items()
                ]
            }

        text_lower = text.lower()
        words = re.findall(r'\b[a-z\'-]+\b', text_lower)
        scores = {k: 0.0 for k in self.categories}

        # Match words
        for w in words:
            for emotion, data in self.categories.items():
                if w in data["words"]:
                    scores[emotion] += 1.0

        # Match emojis
        for char in text:
            for emotion, data in self.categories.items():
                if char in data["emojis"]:
                    scores[emotion] += 1.8

        total_score = sum(scores.values())

        if total_score == 0:
            # Default fallback when no explicit emotion cues found
            return {
                "dominant": "Neutral / Balanced",
                "dominant_color": "#64748B",
                "breakdown": [
                    {"emotion": name, "score": 0.0, "percentage": round(100 / len(self.categories)), "color": data["color"]}
                    for name, data in self.categories.items()
                ]
            }

        breakdown = []
        for name, data in self.categories.items():
            pct = round((scores[name] / total_score) * 100)
            breakdown.append({
                "emotion": name,
                "score": round(scores[name], 2),
                "percentage": pct,
                "color": data["color"]
            })

        # Sort descending by score
        breakdown.sort(key=lambda x: x["score"], reverse=True)
        dominant_item = breakdown[0]

        return {
            "dominant": dominant_item["emotion"],
            "dominant_color": dominant_item["color"],
            "breakdown": breakdown
        }
