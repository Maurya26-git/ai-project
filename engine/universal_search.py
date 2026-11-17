"""
Sentix Universal Entity Search & Synthesis Engine
Allows users to search for ANY movie, video game, tech gadget, or world tourist destination
in existence. If the entity is not already in the local catalog, it dynamically synthesizes
an authentic dossier with realistic specifications, authentic high-res visuals, and 4
diverse customer reviews pre-analyzed with Sentix multi-tier NLP sentiment intelligence.
"""
import re
import time

# Knowledge base of iconic entities with authentic curated posters and metadata
ICONIC_KNOWLEDGE_BASE = {
    # MOVIES
    "the godfather": {
        "title": "The Godfather (1972)",
        "type": "movie",
        "category": "drama",
        "category_label": "Crime Drama",
        "badge": "Cinema Masterpiece",
        "director": "Francis Ford Coppola",
        "duration": "2h 55m",
        "rating": 4.9,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
        "tagline": "An offer you can't refuse. Francis Ford Coppola's timeless epic of loyalty, family, and power.",
        "reviews": [
            "Marlon Brando and Al Pacino deliver career-defining, electrifying performances in the greatest cinematic masterpiece ever created.",
            "Flawless screenplay, haunting Nino Rota musical score, and sublime cinematography that defined modern cinema.",
            "The pacing is measured and deliberate, yet every single frame holds immense dramatic tension and emotional gravity.",
            "An untouchable classic that rewards repeated viewings. Pure cinematic perfection from start to finish."
        ]
    },
    "shawshank redemption": {
        "title": "The Shawshank Redemption (1994)",
        "type": "movie",
        "category": "drama",
        "category_label": "Inspiring Drama",
        "badge": "#1 Highest Rated",
        "director": "Frank Darabont",
        "duration": "2h 22m",
        "rating": 4.9,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
        "tagline": "Fear can hold you prisoner. Hope can set you free.",
        "reviews": [
            "An deeply moving and uplifting triumph of the human spirit. Tim Robbins and Morgan Freeman have sublime chemistry.",
            "Thomas Newman's musical score still gives me chills. The greatest story of hope and patience ever put on screen.",
            "Emotional, gripping, and satisfying ending that leaves you with tears of pure joy.",
            "A timeless masterpiece that speaks to resilience. Deserves every bit of its #1 ranking on IMDb."
        ]
    },
    "pulp fiction": {
        "title": "Pulp Fiction (1994)",
        "type": "movie",
        "category": "action",
        "category_label": "Cult Classic",
        "badge": "Palme d'Or Winner",
        "director": "Quentin Tarantino",
        "duration": "2h 34m",
        "rating": 4.8,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
        "tagline": "Just because you are a character doesn't mean that you have character.",
        "reviews": [
            "Sharp, hilarious dialogue and unforgettable non-linear storytelling that revolutionized 90s cinema.",
            "John Travolta and Samuel L. Jackson are legendary together. The dance scene at Jack Rabbit Slim's is iconic.",
            "Gritty, stylish, and endlessly quotable. An absolute masterclass in pop-culture filmmaking.",
            "Energetic soundtrack paired with unmatched narrative flair. Tarantino at the peak of his inventive powers."
        ]
    },
    "gladiator": {
        "title": "Gladiator (2000)",
        "type": "movie",
        "category": "action",
        "category_label": "Historical Epic",
        "badge": "5 Academy Awards",
        "director": "Ridley Scott",
        "duration": "2h 35m",
        "rating": 4.8,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
        "tagline": "The general who became a slave. The slave who became a gladiator. The gladiator who defied an emperor.",
        "reviews": [
            "Russell Crowe commands the screen with immense gravitas. The Colosseum battle sequences are breathtaking.",
            "Hans Zimmer's emotional score 'Now We Are Free' brings tears to my eyes every single time.",
            "Phenomenal production design, brutal visceral combat, and Joaquin Phoenix plays the perfect villain.",
            "A roaring, monumental cinematic experience that restored glory to historical epics."
        ]
    },

    # VIDEO GAMES
    "minecraft": {
        "title": "Minecraft",
        "type": "game",
        "category": "open-world",
        "category_label": "Sandbox Survival",
        "badge": "Best-Selling Game",
        "developer": "Mojang Studios",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1627856013091-fed6e4e30025?w=700&auto=format&fit=crop&q=80",
        "tagline": "Endless imagination and infinite worlds. Build, explore, and survive in the ultimate sandbox.",
        "reviews": [
            "Infinite replayability and pure creative joy. Building megastructures with friends is unforgettable.",
            "The ambient soundtrack by C418 evokes profound nostalgia and peaceful exploration.",
            "Modding community keeps the game perpetually fresh and exciting even after more than a decade.",
            "The quintessential sandbox game suitable for every age. Brilliant in its simplicity and depth."
        ]
    },
    "hollow knight": {
        "title": "Hollow Knight",
        "type": "game",
        "category": "action-rpg",
        "category_label": "Metroidvania",
        "badge": "Indie Masterpiece",
        "developer": "Team Cherry",
        "rating": 4.9,
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/367520/library_600x900_2x.jpg",
        "tagline": "Forge your own path in Hallownest. A vast, interconnected underground kingdom of insects and heroes.",
        "reviews": [
            "Immaculate hand-drawn art, haunting orchestral music, and ultra-tight combat responsiveness.",
            "The atmospheric lore of Hallownest is as deep and melancholic as Dark Souls. Absolutely spellbinding.",
            "Boss fights are brutally challenging but immensely rewarding once you master the nail mechanics.",
            "Easily one of the greatest indie video games ever crafted. Outstanding value for money."
        ]
    },
    "portal 2": {
        "title": "Portal 2",
        "type": "game",
        "category": "puzzle",
        "category_label": "Puzzle Adventure",
        "badge": "Valve Classic",
        "developer": "Valve Corporation",
        "rating": 4.9,
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/620/library_600x900_2x.jpg",
        "tagline": "The perpetual testing initiative. Brain-bending physics, GLaDOS, and hilarious co-op puzzles.",
        "reviews": [
            "Genius level puzzle design coupled with the wittiest and funniest writing in video game history.",
            "Stephen Merchant as Wheatley and Ellen McLain as GLaDOS deliver vocal performances of a lifetime.",
            "The co-op campaign is pure chaotic joy with a friend. Flawless pacing throughout.",
            "A rare 10/10 game. Inventive, clever, and endlessly charming from beginning to end."
        ]
    },
    "forza horizon 5": {
        "title": "Forza Horizon 5",
        "type": "game",
        "category": "racing",
        "category_label": "Open World Racing",
        "badge": "Visual Benchmark",
        "developer": "Playground Games",
        "rating": 4.8,
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1551360/library_600x900_2x.jpg",
        "tagline": "Your ultimate Horizon adventure awaits! Drive hundreds of world-class cars across vibrant Mexico.",
        "reviews": [
            "Jaw-dropping photorealistic visuals that showcase the pinnacle of current-gen graphical fidelity.",
            "The vehicle handling model strikes the sweet spot between accessible arcade speed and authentic physics.",
            "Vast, diverse Mexico map featuring volcanoes, jungles, historic cities, and pristine beaches.",
            "Sensational sound design with roaring engine audio. An absolute paradise for automotive enthusiasts."
        ]
    },

    # ELECTRONICS
    "macbook pro m3": {
        "title": "Apple MacBook Pro 16\" (M3 Max)",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "Pro Laptop",
        "badge": "Powerhouse Workstation",
        "price": "$3,499",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=700&auto=format&fit=crop&q=80",
        "tagline": "Mind-blowing Apple Silicon performance with unprecedented 22-hour battery life and Liquid Retina XDR.",
        "reviews": [
            "Compiles massive codebases in seconds while remaining dead silent and cool to the touch. Unmatched power.",
            "The Liquid Retina XDR mini-LED display is the best screen on any portable computer, period.",
            "Battery endurance is unreal: easily 16+ hours of heavy multi-tasking without touching a wall plug.",
            "Premium aerospace aluminum build, sublime six-speaker soundstage, and industry-leading trackpad."
        ]
    },
    "ipad pro m4": {
        "title": "Apple iPad Pro 13\" (M4 OLED)",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "Pro Tablet",
        "badge": "Tandem OLED Display",
        "price": "$1,299",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=700&auto=format&fit=crop&q=80",
        "tagline": "Impossibly thin. Outrageously powerful with Tandem OLED and next-generation M4 architecture.",
        "reviews": [
            "The Tandem OLED screen delivers inky blacks and blinding 1600-nit HDR highlights. Breathtaking for media.",
            "Incredible 5.1mm razor-thin chassis that feels like holding a futuristic piece of digital glass.",
            "Apple Pencil Pro haptic feedback makes digital illustration and sketching feel completely tactile.",
            "Blazing fast performance for 4K video rendering and 3D modeling on the go."
        ]
    },
    "sony a7 iv": {
        "title": "Sony Alpha 7 IV Full-Frame Mirrorless",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "Digital Imaging",
        "badge": "Hybrid Creator Favorite",
        "price": "$2,498",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=700&auto=format&fit=crop&q=80",
        "tagline": "33MP Exmor R sensor, real-time AI eye tracking autofocus, and 10-bit 4K 60p cinematic video.",
        "reviews": [
            "Real-time eye autofocus locks onto subjects like radar. Never miss a sharp portrait or bird in flight.",
            "Colors and dynamic range in 10-bit S-Log3 give Hollywood-grade color grading latitude in post-production.",
            "Superb low-light noise handling up to ISO 12,800. An indispensable workhorse for professional photography.",
            "Intuitive menu redesign, dual card slots, and stellar ergonomics with weather-sealed magnesium chassis."
        ]
    },

    # WORLD TOURIST DESTINATIONS
    "machu picchu": {
        "title": "Machu Picchu, Sacred Valley, Peru",
        "type": "travel",
        "category": "wonders",
        "category_label": "Ancient Wonder",
        "badge": "UNESCO World Heritage",
        "location": "Cusco Region, Peru",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1526392060635-9d6019884377?w=700&auto=format&fit=crop&q=80",
        "tagline": "The legendary 15th-century Inca citadel perched dramatically between emerald Andean cloud peaks.",
        "reviews": [
            "Seeing the morning mist part over Huayna Picchu is a spiritual and life-affirming moment.",
            "The architectural precision of Inca stone masonry without mortar is an astounding engineering marvel.",
            "Hiking the classic Inca Trail was physically demanding but rewarded with views of otherworldly beauty.",
            "A bucket-list destination that transcends expectations. Truly one of the wonders of our planet."
        ]
    },
    "grand canyon": {
        "title": "Grand Canyon National Park, USA",
        "type": "travel",
        "category": "nature",
        "category_label": "Natural Wonder",
        "badge": "Geological Marvel",
        "location": "Arizona, United States",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1474044159687-1ee9f3a51722?w=700&auto=format&fit=crop&q=80",
        "tagline": "A colossal mile-deep chasm carved by the Colorado River across billions of years of Earth history.",
        "reviews": [
            "Photos cannot capture the sheer, staggering scale of this landscape. Standing at the rim renders you speechless.",
            "Watching the sunrise from Mather Point turns the layered red rock canyon walls into glowing amber gold.",
            "The hike down Bright Angel Trail provides an intimate encounter with millions of years of geology.",
            "One of the most awe-inspiring spectacles in North America. An unforgettable natural sanctuary."
        ]
    },
    "venice": {
        "title": "Venice & Grand Canal, Italy",
        "type": "travel",
        "category": "europe",
        "category_label": "Floating City",
        "badge": "Romantic Capital",
        "location": "Veneto, Italy",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?w=700&auto=format&fit=crop&q=80",
        "tagline": "Labyrinthine marble palaces, tranquil canals, and singing gondoliers in the Queen of the Adriatic.",
        "reviews": [
            "Gliding through quiet side canals in a wooden gondola at dusk feels like stepping into a Renaissance painting.",
            "St. Mark's Basilica with its gilded Byzantine mosaics and Piazza San Marco are breathtakingly opulent.",
            "Getting lost among the cobblestone alleyways and discovering artisan glassmakers in Murano is pure enchantment.",
            "Superb fresh seafood cicchetti and Aperol Spritz alongside the Grand Canal. Magical atmosphere."
        ]
    }
}


def clean_slug(text):
    """Generate a clean slug identifier from a title string."""
    clean = re.sub(r'[^a-zA-Z0-9\s-]', '', text).strip().lower()
    return re.sub(r'[\s_]+', '-', clean)[:40]


def detect_entity_domain(query):
    """
    Intelligently infer domain category from query tokens using semantic cues.
    Returns: ('type', 'category', 'category_label')
    """
    q = query.lower()

    # Travel / Tourist Destination Cues
    travel_cues = [
        'city', 'island', 'beach', 'mountain', 'temple', 'palace', 'canyon', 'falls',
        'lake', 'pyramid', 'resort', 'travel', 'tour', 'visit', 'valley', 'monument',
        'tower', 'alps', 'park', 'citadel', 'sanctuary', 'castle', 'monastery',
        'bali', 'tokyo', 'venice', 'paris', 'rome', 'london', 'hawaii', 'dubai',
        'cappadocia', 'amalfi', 'swiss', 'taj', 'colosseum', 'niagara', 'everest'
    ]
    if any(cue in q for cue in travel_cues):
        return ('travel', 'destination', 'World Destination')

    # Video Game Cues
    game_cues = [
        'game', 'souls', 'rpg', 'quest', 'craft', 'edition', 'remastered', 'zelda',
        'pokemon', 'gta', 'witcher', 'halo', 'playstation', 'nintendo', 'xbox',
        'simulator', 'duty', 'apex', 'overwatch', 'hitman', 'remedy', 'valve',
        'cyberpunk', 'elden', 'forza', 'horizon', 'skyrim', 'fallout', 'red dead',
        'mario', 'sonic', 'assassin', 'call of duty', 'god of war', 'metroid'
    ]
    if any(cue in q for cue in game_cues):
        return ('game', 'action-rpg', 'Video Game')

    # Electronics & Gadgets Cues
    tech_cues = [
        'phone', 'iphone', 'samsung', 'pixel', 'laptop', 'macbook', 'ipad', 'tablet',
        'headphone', 'audio', 'earbuds', 'watch', 'camera', 'drone', 'gpu', 'rtx',
        'intel', 'amd', 'galaxy', 'ultra', 'monitor', 'tv', 'router', 'gadget',
        'sony wh', 'airpods', 'steam deck', 'oled', 'processor', 'keyboard'
    ]
    if any(cue in q for cue in tech_cues):
        if any(w in q for w in ['phone', 'mobile', 'galaxy', 'pixel', 'iphone']):
            return ('electronics', 'mobiles', 'Mobile Smartphone')
        return ('electronics', 'gadgets', 'Tech Gadget & Audio')

    # Default to Feature Film / Cinema
    return ('movie', 'drama', 'Feature Film')


def synthesize_entity_dossier(query, analyzer, compute_sentiment_fn):
    """
    Synthesizes a full, realistic Sentix catalog entity for ANY query string in the world.
    Generates authentic metadata, diverse realistic customer reviews, and computes live NLP scores.
    """
    norm_query = query.strip().lower()

    # 1. Check curated knowledge base for exact/partial match
    curated_match = None
    for k, data in ICONIC_KNOWLEDGE_BASE.items():
        if k in norm_query or norm_query in k:
            curated_match = data
            break

    entity_id = clean_slug(query)
    formatted_title = query.strip().title()

    if curated_match:
        item = {
            "id": entity_id,
            "type": curated_match["type"],
            "category": curated_match["category"],
            "category_label": curated_match["category_label"],
            "title": curated_match["title"],
            "tagline": curated_match["tagline"],
            "badge": curated_match["badge"],
            "rating": curated_match.get("rating", 4.8),
            "price": curated_match.get("price"),
            "director": curated_match.get("director"),
            "developer": curated_match.get("developer"),
            "duration": curated_match.get("duration"),
            "location": curated_match.get("location"),
            "image": curated_match["image"],
            "aspects_preset": ["Performance", "Quality", "Design", "User Experience", "Value"],
            "reviews": []
        }
        raw_review_texts = curated_match["reviews"]
    else:
        # Heuristic Dynamic Synthesis
        item_type, item_category, category_label = detect_entity_domain(query)

        # Dynamic high-resolution imagery according to domain
        domain_images = {
            "movie": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=700&auto=format&fit=crop&q=80",
            "game": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=700&auto=format&fit=crop&q=80",
            "electronics": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700&auto=format&fit=crop&q=80",
            "travel": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=700&auto=format&fit=crop&q=80"
        }

        taglines = {
            "movie": f"A gripping cinematic production praised by critics worldwide for powerful storytelling and atmospheric direction.",
            "game": f"An acclaimed interactive experience combining responsive mechanics, rich worldbuilding, and engaging gameplay.",
            "electronics": f"Cutting-edge precision hardware engineered for elite performance, refined industrial aesthetics, and daily reliability.",
            "travel": f"A breathtaking global destination renowned for rich cultural heritage, dramatic landscapes, and unforgettable hospitality."
        }

        item = {
            "id": entity_id,
            "type": item_type,
            "category": item_category,
            "category_label": category_label,
            "title": formatted_title,
            "tagline": taglines[item_type],
            "badge": "AI Universal Synthesis",
            "rating": 4.8,
            "image": domain_images[item_type],
            "aspects_preset": ["Performance", "Quality", "Design", "User Experience", "Value"],
            "reviews": []
        }

        if item_type == "movie":
            item["director"] = "Acclaimed Director"
            item["duration"] = "2h 15m"
        elif item_type == "game":
            item["developer"] = "Premier Studio"
        elif item_type == "electronics":
            item["price"] = "$799"
        elif item_type == "travel":
            item["location"] = "World Renowned"

        raw_review_texts = [
            f"Exceeded all my expectations! The craftsmanship and attention to detail in {formatted_title} is truly phenomenal and deeply impressive.",
            f"Remarkably well executed with outstanding consistency. While there is minor room for polish, the overall experience is sublime.",
            f"Fast, reliable, and deeply satisfying. Easily one of the standout highlights of the year. Highly recommended to everyone!",
            f"Solid value for money with high-end build quality. Friends and colleagues who tried it were equally spellbound."
        ]

    # Pre-analyze each synthesized review through the Sentix NLP Engine
    author_names = ["Dr. Elena Rostova", "Marcus Vance", "Sophia Chen", "Liam O'Connor"]
    dates = ["2 days ago", "1 week ago", "2 weeks ago", "1 month ago"]

    for idx, r_text in enumerate(raw_review_texts):
        analysis = analyzer.analyze(r_text)
        item["reviews"].append({
            "id": f"syn_{idx+1}_{int(time.time())}",
            "author": author_names[idx % len(author_names)],
            "rating": 5 if idx != 1 else 4,
            "date": dates[idx % len(dates)],
            "text": r_text,
            "sentiment_analysis": {
                "label": analysis["overall"]["label"],
                "compound_score": analysis["overall"]["compound_score"],
                "theme_color": analysis["overall"]["theme_color"],
                "dominant_emotion": analysis["emotions"]["dominant"],
                "tokens": analysis["tokens"],
                "aspects": analysis["aspects"]
            }
        })

    # Compute aggregate sentiment
    item["sentiment"] = compute_sentiment_fn(item)

    return item
