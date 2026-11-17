"""
Comprehensive Sentiment Lexicon & Linguistic Rules
Includes word valences, emojis, intensifiers, diminishers, negations, and idiomatic expressions.
"""

# Base word valence scale: -4.0 (most negative) to +4.0 (most positive)
WORD_VALENCE = {
    # Strong positive (+3.0 to +4.0)
    "spectacular": 3.8, "masterpiece": 3.9, "phenomenal": 3.7, "breathtaking": 3.8,
    "outstanding": 3.6, "exceptional": 3.6, "magnificent": 3.7, "perfection": 3.9,
    "perfect": 3.5, "extraordinary": 3.6, "brilliant": 3.4, "flawless": 3.7,
    "superb": 3.5, "delightful": 3.2, "wonderful": 3.3, "fabulous": 3.3,
    "incredible": 3.4, "marvelous": 3.4, "triumphant": 3.3, "exquisite": 3.5,
    "unbeatable": 3.4, "stellar": 3.3, "groundbreaking": 3.4, "game-changer": 3.5,
    "gamechanger": 3.5, "masterful": 3.5, "legendary": 3.4, "flawlessly": 3.5,
    "invaluable": 3.2, "sublime": 3.4, "immaculate": 3.6, "radiant": 3.0,
    "thrilled": 3.3, "ecstatic": 3.5, "overjoyed": 3.5, "euphoric": 3.6,

    # Moderate positive (+1.5 to +2.9)
    "excellent": 2.8, "amazing": 2.8, "awesome": 2.7, "great": 2.4, "fantastic": 2.8,
    "love": 2.9, "loved": 2.8, "loves": 2.8, "loving": 2.7, "lovely": 2.5,
    "beautiful": 2.6, "best": 2.9, "better": 1.7, "good": 1.9, "nice": 1.7,
    "happy": 2.4, "glad": 1.8, "pleased": 2.1, "satisfying": 2.2, "satisfied": 2.2,
    "impressive": 2.5, "impressed": 2.4, "innovative": 2.4, "effective": 2.1,
    "efficient": 2.2, "reliable": 2.4, "smooth": 2.0, "clean": 1.8, "sleek": 2.1,
    "fast": 1.7, "blazing": 2.2, "responsive": 2.1, "intuitive": 2.3, "seamless": 2.5,
    "helpful": 2.0, "friendly": 2.2, "supportive": 2.1, "kind": 2.0, "generous": 2.2,
    "fun": 2.1, "enjoyable": 2.3, "enjoyed": 2.2, "entertaining": 2.1, "charming": 2.2,
    "solid": 1.8, "worth": 1.9, "worthy": 1.9, "recommend": 2.3, "recommended": 2.4,
    "recommendable": 2.2, "valuable": 2.3, "favorite": 2.5, "superior": 2.4,
    "prompt": 1.8, "convenient": 2.0, "durable": 2.2, "affordable": 2.1,
    "bargain": 2.0, "positive": 2.0, "prosperous": 2.1, "beneficial": 2.1,
    "success": 2.4, "successful": 2.4, "gain": 1.6, "win": 2.2, "winner": 2.3,
    "winning": 2.2, "honor": 2.1, "proud": 2.2, "pride": 2.0, "cheer": 1.9,
    "cheerful": 2.1, "bright": 1.8, "vibrant": 2.2, "fresh": 1.8, "upbeat": 2.0,
    "underrated": 2.2, "top-notch": 2.8, "first-rate": 2.7, "high-grade": 2.1,
    "neat": 1.7, "cool": 1.8, "solidly": 1.9, "smart": 1.9, "clever": 2.0,

    # Mild positive (+0.5 to +1.4)
    "okay": 0.6, "fine": 0.8, "decent": 1.1, "fair": 0.7, "passable": 0.6,
    "acceptable": 0.9, "adequate": 0.8, "sufficient": 0.8, "usable": 1.0,
    "intact": 0.8, "functional": 1.1, "tidy": 1.0, "polite": 1.2, "mild": 0.5,
    "calm": 1.1, "stable": 1.2, "steady": 1.1, "promising": 1.4, "hopeful": 1.4,
    "standard": 0.5, "normal": 0.4, "comfortable": 1.4, "comfort": 1.3,

    # Mild negative (-0.5 to -1.4)
    "mediocre": -1.2, "bland": -1.1, "dull": -1.2, "boring": -1.4, "slow": -1.1,
    "subpar": -1.4, "lacking": -1.2, "limited": -0.8, "clunky": -1.3, "awkward": -1.2,
    "pricey": -0.9, "costly": -0.8, "expensive": -0.7, "noisy": -1.1, "plain": -0.6,
    "messy": -1.2, "confusing": -1.3, "confused": -1.1, "tedious": -1.4, "tiresome": -1.3,
    "unremarkable": -1.0, "ordinary": -0.5, "hesitant": -0.8, "vague": -0.9,

    # Moderate negative (-1.5 to -2.9)
    "bad": -2.2, "poor": -2.0, "worse": -2.1, "broken": -2.3, "damaged": -2.2,
    "buggy": -2.1, "glitchy": -2.0, "laggy": -1.9, "crash": -2.4, "crashed": -2.5,
    "crashing": -2.4, "fail": -2.3, "failed": -2.4, "failing": -2.3, "failure": -2.5,
    "faulty": -2.2, "defective": -2.4, "flawed": -2.0, "disappointed": -2.4,
    "disappointing": -2.4, "disappointment": -2.5, "annoying": -2.1, "annoyed": -2.0,
    "frustrating": -2.3, "frustrated": -2.3, "frustration": -2.3, "useless": -2.6,
    "worthless": -2.8, "waste": -2.5, "wasted": -2.4, "rude": -2.4, "impolite": -2.0,
    "unhelpful": -2.2, "unfriendly": -2.1, "unreliable": -2.4, "unresponsive": -2.3,
    "complicated": -1.7, "difficult": -1.6, "painful": -2.2, "uncomfortable": -1.8,
    "ugly": -2.1, "hate": -2.8, "hated": -2.8, "hating": -2.7, "hates": -2.8,
    "angry": -2.3, "upset": -2.0, "sad": -2.0, "sorry": -1.5, "grief": -2.3,
    "fear": -2.1, "anxious": -1.9, "nervous": -1.6, "worry": -1.7, "worried": -1.8,
    "scared": -2.1, "problem": -1.7, "problems": -1.8, "issue": -1.5, "issues": -1.6,
    "error": -1.8, "errors": -1.9, "defect": -2.2, "flaw": -1.9, "weak": -1.7,
    "loss": -1.9, "lost": -1.8, "losing": -1.8, "struggle": -1.8, "trouble": -1.9,
    "overrated": -1.9, "overpriced": -2.0, "shoddy": -2.3, "cheated": -2.5,

    # Strong negative (-3.0 to -4.0)
    "terrible": -3.4, "horrible": -3.5, "awful": -3.4, "abysmal": -3.7, "dreadful": -3.6,
    "disastrous": -3.6, "catastrophic": -3.8, "atrocious": -3.7, "appalling": -3.6,
    "disgusting": -3.5, "repulsive": -3.4, "revolting": -3.5, "horrendous": -3.6,
    "nightmare": -3.5, "unacceptable": -3.2, "scam": -3.7, "fraud": -3.8,
    "garbage": -3.4, "trash": -3.3, "rubbish": -3.2, "crap": -3.3, "pathetic": -3.4,
    "intolerable": -3.3, "infuriating": -3.5, "outrageous": -3.4, "toxic": -3.4,
    "ruined": -3.2, "ruin": -3.1, "destroy": -3.2, "destroyed": -3.3, "worst": -3.7,
    "despicable": -3.6, "loathsome": -3.7, "scandalous": -3.5, "vile": -3.6
}

# Emojis and their sentiment valence
EMOJI_VALENCE = {
    "😀": 2.0, "😃": 2.2, "😄": 2.4, "😁": 2.3, "😆": 2.2, "😅": 1.5,
    "😂": 2.2, "🤣": 2.5, "😊": 2.4, "😇": 2.5, "🙂": 1.2, "😉": 1.8,
    "😍": 3.4, "🥰": 3.3, "😘": 2.8, "😋": 1.9, "😎": 2.3, "🤩": 3.2,
    "🥳": 3.0, "👍": 2.2, "👍🏻": 2.2, "👍🏼": 2.2, "👍🏽": 2.2, "👍🏾": 2.2, "👍🏿": 2.2,
    "👏": 2.4, "🙌": 2.6, "🎉": 2.8, "✨": 2.4, "🚀": 2.7, "🔥": 2.8,
    "❤️": 3.2, "💖": 3.2, "💕": 2.9, "💯": 3.0, "⭐": 2.0, "🌟": 2.3,
    "💪": 2.2, "🏆": 2.8, "👌": 1.9, "🤝": 2.0, "🍻": 2.0, "🥂": 2.2,
    "😐": -0.6, "😑": -0.8, "😶": -0.5, "🙄": -1.8, "😏": 0.4, "😒": -1.7,
    "🤔": 0.2, "🤨": -0.8, "😬": -1.3, "🤥": -2.2, "😌": 1.5, "😔": -1.8,
    "😪": -1.2, "😴": -0.5, "😷": -1.4, "🤒": -1.8, "🤕": -2.0, "🤢": -2.8,
    "🤮": -3.5, "🤧": -1.4, "🥵": -1.2, "🥶": -1.2, "🥴": -1.1, "😵": -1.5,
    "🤯": 1.2, "🤠": 1.4, "😕": -1.5, "😟": -1.9, "🙁": -1.8, "☹️": -2.2,
    "😮": 0.8, "😯": 0.7, "😲": 1.2, "😳": -0.6, "🥺": 0.8, "😦": -1.4,
    "😧": -1.6, "😨": -2.2, "😰": -2.1, "😥": -1.8, "😢": -2.2, "😭": -2.4,
    "😱": -2.6, "😖": -2.2, "😣": -2.0, "😞": -2.1, "😓": -1.7, "😩": -2.3,
    "😫": -2.4, "🥱": -1.2, "😤": -1.8, "😡": -3.2, "😠": -2.8, "🤬": -3.6,
    "😈": 0.5, "👿": -2.0, "💀": -1.5, "☠️": -2.2, "💩": -2.8, "🤡": -2.0,
    "👎": -2.5, "👎🏻": -2.5, "👎🏼": -2.5, "👎🏽": -2.5, "👎🏾": -2.5, "👎🏿": -2.5,
    "💔": -2.8, "🚫": -1.8, "❌": -1.9, "⚠️": -1.2, "📉": -2.0, "📈": 2.0
}

# Intensifiers (Boosters) - multiply valence by these factors
INTENSIFIERS = {
    "absolutely": 1.45,
    "extremely": 1.45,
    "exceptionally": 1.45,
    "incredibly": 1.40,
    "unbelievably": 1.40,
    "massively": 1.35,
    "tremendously": 1.35,
    "immensely": 1.35,
    "insanely": 1.35,
    "deeply": 1.30,
    "hugely": 1.30,
    "vastly": 1.30,
    "very": 1.28,
    "really": 1.25,
    "truly": 1.25,
    "so": 1.22,
    "totally": 1.28,
    "completely": 1.28,
    "entirely": 1.25,
    "super": 1.30,
    "ultra": 1.35,
    "highly": 1.28,
    "especially": 1.20,
    "remarkably": 1.30,
    "substantially": 1.20,
    "fully": 1.20
}

# Diminishers (Downtoners) - reduce valence
DIMINISHERS = {
    "barely": 0.45,
    "hardly": 0.45,
    "scarcely": 0.45,
    "rarely": 0.50,
    "seldom": 0.55,
    "slightly": 0.60,
    "somewhat": 0.65,
    "mildly": 0.65,
    "marginally": 0.60,
    "partially": 0.70,
    "a bit": 0.65,
    "a little": 0.65,
    "kind of": 0.70,
    "kinda": 0.70,
    "sort of": 0.70,
    "sorta": 0.70
}

# Negation words (inverts sentiment of subsequent words within a sliding window)
NEGATIONS = {
    "not", "never", "no", "none", "neither", "nor", "nothing", "nowhere",
    "hardly", "scarcely", "barely", "doesn't", "don't", "didn't",
    "isn't", "aren't", "wasn't", "weren't", "hasn't", "haven't",
    "hadn't", "won't", "wouldn't", "can't", "cannot", "couldn't",
    "shouldn't", "mustn't", "without", "lack", "lacks", "lacking",
    "devoid", "fail", "failed", "refuse", "refused"
}

# Idioms & Multi-word expressions with precomputed valence
IDIOMS = {
    "worth every penny": 3.4,
    "second to none": 3.5,
    "state of the art": 3.0,
    "out of this world": 3.3,
    "piece of cake": 2.4,
    "over the moon": 3.2,
    "breath of fresh air": 3.0,
    "hit the nail on the head": 2.8,
    "ahead of the curve": 2.7,
    "gold standard": 3.5,
    "top drawer": 3.0,
    "bang for the buck": 2.8,
    "value for money": 2.7,

    "waste of money": -3.3,
    "waste of time": -3.4,
    "cost an arm and a leg": -2.4,
    "pain in the neck": -2.7,
    "down the drain": -2.8,
    "fell short": -2.3,
    "falls short": -2.3,
    "missed the mark": -2.4,
    "left a bad taste": -2.8,
    "add insult to injury": -3.0,
    "not worth it": -2.7,
    "not up to par": -2.2,
    "under the weather": -1.8,
    "rip off": -3.5,
    "ripoff": -3.5
}

# Contrastive conjunctions (give higher weight to what follows)
CONTRASTIVE_CONJUNCTIONS = {
    "but", "however", "although", "though", "yet", "except", "nevertheless", "nonetheless", "despite"
}
