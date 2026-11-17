"""
Core Sentiment Intelligence Engine
Integrates lexicon rules, ML statistical classification, emotion analysis,
aspect-based sentiment extraction, and optional LLM insights.
"""
import re
import math
from .lexicon import (
    WORD_VALENCE, EMOJI_VALENCE, INTENSIFIERS, DIMINISHERS,
    NEGATIONS, IDIOMS, CONTRASTIVE_CONJUNCTIONS
)
from .emotion_detector import EmotionDetector
from .aspect_extractor import AspectExtractor
from .ml_classifier import MLSentimentClassifier
from .gemini_client import GeminiSentimentClient

class SentimentAnalyzer:
    def __init__(self):
        self.word_valence = WORD_VALENCE
        self.emoji_valence = EMOJI_VALENCE
        self.emotion_detector = EmotionDetector()
        self.aspect_extractor = AspectExtractor(self.word_valence)
        self.ml_classifier = MLSentimentClassifier()
        self.gemini_client = GeminiSentimentClient()

    def analyze(self, text: str, gemini_api_key: str = None) -> dict:
        if not text or not text.strip():
            return self._empty_result()

        raw_text = text.strip()
        
        # 1. Linguistic & Lexicon Analysis
        lex_result = self._score_lexicon(raw_text)

        # 2. Machine Learning Classifier
        ml_result = self.ml_classifier.predict(raw_text)

        # 3. Emotion Detection
        emotion_result = self.emotion_detector.detect(raw_text)

        # 4. Aspect-Based Sentiment Analysis (ABSA)
        aspects = self.aspect_extractor.extract_aspects(raw_text, self.word_valence)

        # 5. Sarcasm & Tone Heuristics
        sarcasm_detected, tone_traits = self._detect_tone_and_sarcasm(raw_text, lex_result["compound"])

        # 6. Ensemble Overall Score
        # Blend lexicon compound score and ML confidence
        ml_score = 0.0
        if ml_result["label"] == "Positive":
            ml_score = ml_result["confidence"]
        elif ml_result["label"] == "Negative":
            ml_score = -ml_result["confidence"]
        
        # Weighted ensemble compound score
        blended_compound = round((lex_result["compound"] * 0.65) + (ml_score * 0.35), 3)
        blended_compound = max(-1.0, min(1.0, blended_compound))

        # Overall Label
        if blended_compound >= 0.50:
            overall_label = "Strongly Positive"
            theme_color = "#10B981"  # Emerald
        elif blended_compound >= 0.10:
            overall_label = "Positive"
            theme_color = "#34D399"  # Mint
        elif blended_compound <= -0.50:
            overall_label = "Strongly Negative"
            theme_color = "#EF4444"  # Red
        elif blended_compound <= -0.10:
            overall_label = "Negative"
            theme_color = "#F87171"  # Coral
        else:
            overall_label = "Neutral"
            theme_color = "#94A3B8"  # Slate

        confidence = round(min(0.99, max(0.55, abs(blended_compound) * 0.5 + ml_result["confidence"] * 0.5)), 2)

        # 7. Optional Gemini LLM Deep Insights
        gemini_result = None
        if gemini_api_key or self.gemini_client.is_available():
            gemini_result = self.gemini_client.analyze_deep(raw_text, api_key=gemini_api_key)

        words_list = re.findall(r'\b\w+\b', raw_text)
        reading_time = max(1, round(len(words_list) / 3.5))

        return {
            "text": raw_text,
            "overall": {
                "label": overall_label,
                "compound_score": blended_compound,
                "normalized_score": round((blended_compound + 1.0) * 50, 1), # 0 to 100
                "confidence": confidence,
                "confidence_percent": int(confidence * 100),
                "theme_color": theme_color,
                "positive_score": lex_result["pos_ratio"],
                "neutral_score": lex_result["neu_ratio"],
                "negative_score": lex_result["neg_ratio"],
                "subjectivity": lex_result["subjectivity"]
            },
            "ml_model": ml_result,
            "emotions": emotion_result,
            "aspects": aspects,
            "tokens": lex_result["tokens"],
            "sarcasm_detected": sarcasm_detected,
            "tone_descriptors": tone_traits,
            "metrics": {
                "word_count": len(words_list),
                "character_count": len(raw_text),
                "reading_time_sec": reading_time,
                "sentence_count": len(re.split(r'[.!?]+', raw_text)) - 1 or 1
            },
            "gemini_insights": gemini_result
        }

    def _score_lexicon(self, text: str) -> dict:
        tokens_meta = []
        text_lower = text.lower()

        # Check for multi-word idioms
        idiom_matches = []
        for idiom, val in IDIOMS.items():
            if idiom in text_lower:
                idiom_matches.append((idiom, val))

        # Split text into tokens with regex keeping punctuation
        raw_tokens = re.findall(r"[\w'-]+|[^\w\s]", text)
        
        pos_sum = 0.0
        neg_sum = 0.0
        neu_count = 0
        emotional_count = 0

        negation_active = False
        negation_window = 0
        intensifier_val = 1.0
        contrast_boost = 1.0

        for token in raw_tokens:
            token_lower = token.lower()

            # Check contrastive conjunctions (e.g., 'but', 'however')
            if token_lower in CONTRASTIVE_CONJUNCTIONS:
                contrast_boost = 1.35
                tokens_meta.append({
                    "text": token, "type": "conjunction", "score": 0.0, "tooltip": "Contrastive shift"
                })
                continue

            # Check negation
            if token_lower in NEGATIONS:
                negation_active = True
                negation_window = 3
                tokens_meta.append({
                    "text": token, "type": "negation", "score": 0.0, "tooltip": "Inverts sentiment"
                })
                continue

            # Check intensifier
            if token_lower in INTENSIFIERS:
                intensifier_val = INTENSIFIERS[token_lower]
                tokens_meta.append({
                    "text": token, "type": "intensifier", "score": 0.0, "tooltip": f"Amplifier (x{intensifier_val})"
                })
                continue

            # Check diminisher
            if token_lower in DIMINISHERS:
                intensifier_val = DIMINISHERS[token_lower]
                tokens_meta.append({
                    "text": token, "type": "diminisher", "score": 0.0, "tooltip": f"Softener (x{intensifier_val})"
                })
                continue

            # Lookup word or emoji valence
            valence = self.word_valence.get(token_lower, None)
            if valence is None and token in self.emoji_valence:
                valence = self.emoji_valence[token]

            if valence is not None:
                # Apply negation if active
                if negation_active and negation_window > 0:
                    valence = -valence * 0.85
                    negation_window -= 1
                    if negation_window == 0:
                        negation_active = False
                
                # Apply intensifier & contrast boost
                valence = valence * intensifier_val * contrast_boost
                intensifier_val = 1.0

                # All-caps emphasis bonus (e.g. AMAZING vs amazing)
                if token.isupper() and len(token) > 1:
                    valence *= 1.25

                emotional_count += 1
                if valence > 0:
                    pos_sum += valence
                    t_type = "positive"
                elif valence < 0:
                    neg_sum += abs(valence)
                    t_type = "negative"
                else:
                    neu_count += 1
                    t_type = "neutral"

                tokens_meta.append({
                    "text": token,
                    "type": t_type,
                    "score": round(valence, 2),
                    "tooltip": f"Valence: {round(valence, 2)}"
                })
            else:
                if negation_window > 0:
                    negation_window -= 1
                    if negation_window == 0:
                        negation_active = False

                if re.match(r"^\w+$", token):
                    neu_count += 1
                tokens_meta.append({
                    "text": token, "type": "neutral", "score": 0.0, "tooltip": "Neutral"
                })

        # Add idiom contributions
        for idiom, ival in idiom_matches:
            emotional_count += 2
            if ival > 0:
                pos_sum += ival * 1.5
            else:
                neg_sum += abs(ival) * 1.5

        # Punctuation emphasis (e.g. !!! or ???)
        exclamation_count = text.count("!")
        if exclamation_count >= 2:
            if pos_sum > neg_sum:
                pos_sum += min(1.5, exclamation_count * 0.25)
            elif neg_sum > pos_sum:
                neg_sum += min(1.5, exclamation_count * 0.25)

        # Compute normalized compound score using hyperbolic tangent / sigmoid curve
        diff = pos_sum - neg_sum
        alpha = 15.0
        compound = diff / math.sqrt((diff * diff) + alpha)
        compound = round(max(-1.0, min(1.0, compound)), 3)

        total_valence = pos_sum + neg_sum + (neu_count * 0.5)
        if total_valence > 0:
            pos_ratio = round(pos_sum / total_valence, 3)
            neg_ratio = round(neg_sum / total_valence, 3)
            neu_ratio = round((neu_count * 0.5) / total_valence, 3)
        else:
            pos_ratio, neg_ratio, neu_ratio = 0.0, 0.0, 1.0

        # Subjectivity: ratio of emotional tokens vs total words
        total_words = max(1, neu_count + emotional_count)
        subjectivity = round(min(1.0, (emotional_count * 1.6) / total_words), 2)

        return {
            "compound": compound,
            "pos_ratio": pos_ratio,
            "neg_ratio": neg_ratio,
            "neu_ratio": neu_ratio,
            "subjectivity": subjectivity,
            "tokens": tokens_meta
        }

    def _detect_tone_and_sarcasm(self, text: str, compound: float) -> tuple:
        text_lower = text.lower()
        sarcasm = False
        traits = []

        # Sarcasm markers
        sarcastic_phrases = [
            "yeah right", "oh sure", "just what i needed", "thanks a lot",
            "great job breaking", "so thrilled that it broke", "brilliant /s",
            "as expected from this disaster", "what a surprise"
        ]
        for sp in sarcastic_phrases:
            if sp in text_lower:
                sarcasm = True
                break

        # Contradiction check: extreme positive word with extreme negative word
        has_strong_pos = any(w in text_lower for w in ["spectacular", "masterpiece", "brilliant", "wonderful", "genius"])
        has_strong_neg = any(w in text_lower for w in ["terrible", "worst", "waste", "broke", "garbage", "trash", "nightmare"])
        if has_strong_pos and has_strong_neg:
            sarcasm = True

        if sarcasm:
            traits.append("Sarcastic / Ironical")

        # Tone descriptors
        if compound >= 0.6:
            traits.append("Enthusiastic")
            traits.append("Vibrant")
        elif compound >= 0.2:
            traits.append("Positive")
            traits.append("Optimistic")
        elif compound <= -0.6:
            traits.append("Critical")
            traits.append("Frustrated")
        elif compound <= -0.2:
            traits.append("Disappointed")
            traits.append("Concerned")
        else:
            traits.append("Objective")
            traits.append("Informational")

        if text.count("!") >= 2:
            traits.append("Emphatic")
        if text.count("?") >= 2:
            traits.append("Inquisitive")

        return sarcasm, traits[:4]

    def _empty_result(self) -> dict:
        return {
            "text": "",
            "overall": {
                "label": "Neutral",
                "compound_score": 0.0,
                "normalized_score": 50.0,
                "confidence": 0.5,
                "confidence_percent": 50,
                "theme_color": "#94A3B8",
                "positive_score": 0.0,
                "neutral_score": 1.0,
                "negative_score": 0.0,
                "subjectivity": 0.0
            },
            "ml_model": {"label": "Neutral", "confidence": 0.5, "probabilities": {"positive": 0.33, "neutral": 0.34, "negative": 0.33}},
            "emotions": self.emotion_detector.detect(""),
            "aspects": [],
            "tokens": [],
            "sarcasm_detected": False,
            "tone_descriptors": ["Neutral"],
            "metrics": {"word_count": 0, "character_count": 0, "reading_time_sec": 0, "sentence_count": 0},
            "gemini_insights": None
        }
