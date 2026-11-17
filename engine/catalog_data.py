"""
Sentix Unified Knowledge Catalog
Electronics (Mobiles, Gadgets), Movies (by Genre), Video Games (by Genre),
and World Tourist Destinations (by Country/Region).
"""

CATALOG_ITEMS = {
    # =========================================================================
    # 1. ELECTRONICS: MOBILES & GADGETS
    # =========================================================================
    "iphone-16-pro-max": {
        "id": "iphone-16-pro-max",
        "type": "electronics",
        "category": "mobiles",
        "category_label": "Mobile Smartphone",
        "title": "Apple iPhone 16 Pro Max",
        "tagline": "Grade 5 Titanium, A18 Pro Chip, 48MP Fusion Camera, Camera Control",
        "badge": "Flagship Mobile",
        "rating": 4.8,
        "price": "$1,199",
        "image": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Camera & Imaging", "Battery & Power", "Build Quality & Design", "Performance & Speed"],
        "reviews": [
            {
                "id": "r1",
                "author": "Marcus Vance",
                "rating": 5,
                "date": "2 days ago",
                "text": "The camera on this phone is truly phenomenal with crisp 48MP detail and low-light portraits! The battery easily lasts a day and a half with heavy photography."
            },
            {
                "id": "r2",
                "author": "Elena Rostova",
                "rating": 4,
                "date": "1 week ago",
                "text": "The display is radiant and the A18 Pro chip handles 4K video editing effortlessly. However, the device is slightly heavy and iOS 18 has occasional minor bugs."
            },
            {
                "id": "r3",
                "author": "Jordan K.",
                "rating": 5,
                "date": "2 weeks ago",
                "text": "Best smartphone upgrade I have made in three years! Titanium finish feels premium and the Camera Control button is very intuitive."
            }
        ]
    },
    "samsung-galaxy-s25-ultra": {
        "id": "samsung-galaxy-s25-ultra",
        "type": "electronics",
        "category": "mobiles",
        "category_label": "Mobile Smartphone",
        "title": "Samsung Galaxy S25 Ultra",
        "tagline": "Snapdragon 8 Elite, Galaxy AI, Built-in S-Pen, 200MP Quad Camera",
        "badge": "AI Powerhouse",
        "rating": 4.7,
        "price": "$1,299",
        "image": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Display & Screen", "Performance & Speed", "Camera & Imaging", "Battery & Power"],
        "reviews": [
            {
                "id": "r4",
                "author": "David Chen",
                "rating": 5,
                "date": "3 days ago",
                "text": "The flat anti-reflective AMOLED display is out of this world! Glare is nonexistent under bright sunlight, and the zoom camera is unmatched."
            },
            {
                "id": "r5",
                "author": "Chloe Simmons",
                "rating": 4,
                "date": "5 days ago",
                "text": "Galaxy AI features like Circle to Search and live translation work seamlessly. The phone is quite large to hold with one hand, but battery life is rock solid."
            }
        ]
    },
    "google-pixel-9-pro": {
        "id": "google-pixel-9-pro",
        "type": "electronics",
        "category": "mobiles",
        "category_label": "Mobile Smartphone",
        "title": "Google Pixel 9 Pro",
        "tagline": "Tensor G4, Gemini AI Engine, Super Res Zoom, Matte Finish",
        "badge": "Clean Android",
        "rating": 4.6,
        "price": "$999",
        "image": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Software & Interface", "Camera & Imaging", "Build Quality & Design"],
        "reviews": [
            {
                "id": "r6",
                "author": "Alex Thorne",
                "rating": 5,
                "date": "4 days ago",
                "text": "Pure Android experience with zero bloatware! The Magic Editor and night sight photo processing consistently blow me away."
            },
            {
                "id": "r7",
                "author": "Nina Patel",
                "rating": 4,
                "date": "1 week ago",
                "text": "Compact size feels great in hand and call screening is a lifesaver. Charging speed is slightly slower than rivals, but overall fantastic phone."
            }
        ]
    },
    "oneplus-13": {
        "id": "oneplus-13",
        "type": "electronics",
        "category": "mobiles",
        "category_label": "Mobile Smartphone",
        "title": "OnePlus 13 5G",
        "tagline": "6000mAh Glacier Battery, 100W SuperVOOC, Hasselblad Camera",
        "badge": "Speed King",
        "rating": 4.7,
        "price": "$899",
        "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Battery & Power", "Performance & Speed", "Price & Value"],
        "reviews": [
            {
                "id": "r8",
                "author": "Ryan Gomez",
                "rating": 5,
                "date": "2 days ago",
                "text": "Charging from 1% to 100% in 25 minutes feels like sci-fi! The 6000mAh battery easily provides two full days of heavy battery life."
            }
        ]
    },
    "galaxy-z-fold-6": {
        "id": "galaxy-z-fold-6",
        "type": "electronics",
        "category": "mobiles",
        "category_label": "Foldable Smartphone",
        "title": "Samsung Galaxy Z Fold 6",
        "tagline": "7.6-inch Dynamic AMOLED 2X, Armor Aluminum, Dual-Screen Multitasking",
        "badge": "Next-Gen Foldable",
        "rating": 4.6,
        "price": "$1,899",
        "image": "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Display & Screen", "Build Quality & Design", "Performance & Speed"],
        "reviews": [
            {
                "id": "r8b",
                "author": "Derrick Holt",
                "rating": 5,
                "date": "3 days ago",
                "text": "Multitasking across three apps simultaneously on the inner screen is a productivity superpower. The new squared-off titanium edges feel much more durable!"
            }
        ]
    },
    "sony-wh1000xm5": {
        "id": "sony-wh1000xm5",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "Audio & Gadgets",
        "title": "Sony WH-1000XM5 ANC Headphones",
        "tagline": "Industry Leading Noise Cancelling, Auto NC Optimizer, 30h Battery",
        "badge": "Top Audio Gadget",
        "rating": 4.9,
        "price": "$398",
        "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Audio & Sound", "Build Quality & Design", "Battery & Power"],
        "reviews": [
            {
                "id": "r9",
                "author": "Liam Vance",
                "rating": 5,
                "date": "1 day ago",
                "text": "The active noise cancellation is pure magic. It silences loud airplane engines and noisy coffee shops completely. The plush earcups feel like clouds."
            },
            {
                "id": "r10",
                "author": "Sophie Taylor",
                "rating": 4,
                "date": "1 week ago",
                "text": "Outstanding soundstage with punchy, controlled bass. The headband doesn't fold as compactly as the XM4, but the sound quality is top-notch."
            }
        ]
    },
    "apple-watch-ultra-2": {
        "id": "apple-watch-ultra-2",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "Wearable Gadget",
        "title": "Apple Watch Ultra 2",
        "tagline": "Rugged 49mm Titanium Case, 3000 Nits Display, Precision Dual-GPS",
        "badge": "Adventure Tech",
        "rating": 4.8,
        "price": "$799",
        "image": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Build Quality & Design", "Battery & Power", "Display & Screen"],
        "reviews": [
            {
                "id": "r11",
                "author": "Brendan Scott",
                "rating": 5,
                "date": "3 days ago",
                "text": "Incredible durability! Used it for mountain hiking and scuba diving. The screen is remarkably bright under blazing sun and battery lasts 3 full days."
            }
        ]
    },
    "steam-deck-oled": {
        "id": "steam-deck-oled",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "Gaming Tech",
        "title": "Steam Deck OLED (1TB)",
        "tagline": "90Hz HDR OLED, 50Wh Battery, Wi-Fi 6E, Custom AMD APU",
        "badge": "Gaming Gadget",
        "rating": 4.9,
        "price": "$649",
        "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Display & Screen", "Performance & Speed", "Price & Value"],
        "reviews": [
            {
                "id": "r12",
                "author": "Julian M.",
                "rating": 5,
                "date": "4 days ago",
                "text": "The OLED panel with infinite blacks and 90Hz refresh rate completely transforms portable PC gaming. Runs Cyberpunk and Elden Ring like a dream!"
            }
        ]
    },
    "dji-mini-4-pro": {
        "id": "dji-mini-4-pro",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "Drone Tech",
        "title": "DJI Mini 4 Pro Drone",
        "tagline": "Under 249g, Omnidirectional Obstacle Sensing, 4K/60fps HDR",
        "badge": "Aerial Tech",
        "rating": 4.8,
        "price": "$759",
        "image": "https://images.unsplash.com/photo-1527977966376-1c8408f9f108?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Camera & Imaging", "Performance & Speed", "Build Quality & Design"],
        "reviews": [
            {
                "id": "r13",
                "author": "Hannah Bell",
                "rating": 5,
                "date": "1 week ago",
                "text": "The obstacle avoidance sensors make flying virtually crash-proof. Video quality in 4K D-Log M is stunning and folds up smaller than a water bottle."
            }
        ]
    },
    "meta-quest-3": {
        "id": "meta-quest-3",
        "type": "electronics",
        "category": "gadgets",
        "category_label": "VR / Mixed Reality",
        "title": "Meta Quest 3 (512GB)",
        "tagline": "Snapdragon XR2 Gen 2, Full-Color 4K+ Infinite Display Passthrough",
        "badge": "Mixed Reality",
        "rating": 4.7,
        "price": "$499",
        "image": "https://images.unsplash.com/photo-1622979135225-d2ba269bc1df?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Display & Screen", "Performance & Speed", "Gameplay & Combat"],
        "reviews": [
            {
                "id": "r14",
                "author": "Trevor Wright",
                "rating": 5,
                "date": "5 days ago",
                "text": "The pancake lenses deliver crystal clarity from edge to edge with zero god rays. Mixed reality passthrough turns your living room into an alien battlefield!"
            }
        ]
    },

    # =========================================================================
    # 2. MOVIES (OFFICIAL HIGH-RES THEATRICAL POSTERS)
    # =========================================================================
    "interstellar": {
        "id": "interstellar",
        "type": "movie",
        "category": "sci-fi",
        "category_label": "Sci-Fi Masterpiece",
        "title": "Interstellar (2014)",
        "tagline": "Mankind was born on Earth. It was never meant to die here.",
        "badge": "Sci-Fi Classic",
        "director": "Christopher Nolan",
        "duration": "169 min",
        "rating": 4.9,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "aspects_preset": ["Story & Narrative", "Graphics & Visuals", "Soundtrack & Audio", "Direction & Acting"],
        "reviews": [
            {
                "id": "m1",
                "author": "CinemaLover99",
                "rating": 5,
                "date": "3 days ago",
                "text": "A breathtaking cinematic triumph! Hans Zimmer's pipe organ soundtrack evokes overwhelming emotional weight, and the gargantua black hole visualization is scientific art."
            },
            {
                "id": "m2",
                "author": "Dr. Sarah Weiss",
                "rating": 5,
                "date": "1 week ago",
                "text": "Deeply moving emotional core intertwined with theoretical physics. Matthew McConaughey delivers an unforgettable, tear-jerking performance."
            }
        ]
    },
    "dune-part-two": {
        "id": "dune-part-two",
        "type": "movie",
        "category": "sci-fi",
        "category_label": "Sci-Fi Epic",
        "title": "Dune: Part Two (2024)",
        "tagline": "Long live the fighters.",
        "badge": "Modern Epic",
        "director": "Denis Villeneuve",
        "duration": "166 min",
        "rating": 4.9,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/1pdfLvk8qq94mgBqGuOlbtV9LiP.jpg",
        "aspects_preset": ["Graphics & Visuals", "Soundtrack & Audio", "Story & Narrative", "Direction & Acting"],
        "reviews": [
            {
                "id": "m3",
                "author": "Greg Morales",
                "rating": 5,
                "date": "2 days ago",
                "text": "Unbelievable scale and grandeur! Denis Villeneuve has crafted the Lord of the Rings of sci-fi cinema. The sand worm riding sequence is absolute movie magic."
            },
            {
                "id": "m4",
                "author": "Jessica Hall",
                "rating": 5,
                "date": "5 days ago",
                "text": "Timothée Chalamet and Zendaya command every frame. The sound design rattles your entire chest with majestic intensity."
            }
        ]
    },
    "the-dark-knight": {
        "id": "the-dark-knight",
        "type": "movie",
        "category": "action",
        "category_label": "Action / Crime Thriller",
        "title": "The Dark Knight (2008)",
        "tagline": "Why so serious?",
        "badge": "Masterpiece",
        "director": "Christopher Nolan",
        "duration": "152 min",
        "rating": 5.0,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "aspects_preset": ["Direction & Acting", "Story & Narrative", "Soundtrack & Audio"],
        "reviews": [
            {
                "id": "m5",
                "author": "Patrick Bateman",
                "rating": 5,
                "date": "4 days ago",
                "text": "Heath Ledger's Joker is the greatest villain performance in the history of cinema. A razor-sharp psychological crime thriller disguised as a superhero movie."
            }
        ]
    },
    "inception": {
        "id": "inception",
        "type": "movie",
        "category": "sci-fi",
        "category_label": "Sci-Fi Heist",
        "title": "Inception (2010)",
        "tagline": "Your mind is the scene of the crime.",
        "badge": "Mind-Bending",
        "director": "Christopher Nolan",
        "duration": "148 min",
        "rating": 4.8,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
        "aspects_preset": ["Story & Narrative", "Graphics & Visuals", "Soundtrack & Audio"],
        "reviews": [
            {
                "id": "m6",
                "author": "Tyler Durden",
                "rating": 5,
                "date": "1 week ago",
                "text": "The rotating hallway fight scene with zero gravity is unforgettable. Intricate multi-layered dream heist that keeps you glued to the screen until that spinning totem."
            }
        ]
    },
    "oppenheimer": {
        "id": "oppenheimer",
        "type": "movie",
        "category": "thriller",
        "category_label": "Historical Drama / Thriller",
        "title": "Oppenheimer (2023)",
        "tagline": "The world forever changes.",
        "badge": "7 Oscar Winner",
        "director": "Christopher Nolan",
        "duration": "180 min",
        "rating": 4.8,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "aspects_preset": ["Direction & Acting", "Soundtrack & Audio", "Story & Narrative"],
        "reviews": [
            {
                "id": "m7",
                "author": "Arthur Miller",
                "rating": 5,
                "date": "3 days ago",
                "text": "Cillian Murphy's thousand-yard stare embodies the haunting dilemma of Prometheus. Ludwig Göransson's violin score creates unbearable, gripping tension."
            }
        ]
    },
    "parasite": {
        "id": "parasite",
        "type": "movie",
        "category": "thriller",
        "category_label": "Black Comedy / Thriller",
        "title": "Parasite (2019)",
        "tagline": "Act like you own the place.",
        "badge": "Palme d'Or Winner",
        "director": "Bong Joon-ho",
        "duration": "132 min",
        "rating": 4.9,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
        "aspects_preset": ["Story & Narrative", "Direction & Acting"],
        "reviews": [
            {
                "id": "m8",
                "author": "Kevin Song",
                "rating": 5,
                "date": "6 days ago",
                "text": "A masterclass in genre-bending and social satire. The mid-film plot twist completely shifts the atmosphere into an edge-of-your-seat thriller."
            }
        ]
    },
    "spirited-away": {
        "id": "spirited-away",
        "type": "movie",
        "category": "animation",
        "category_label": "Animation / Fantasy",
        "title": "Spirited Away (2001)",
        "tagline": "Tunnel into a mystical bathhouse of spirits.",
        "badge": "Ghibli Classic",
        "director": "Hayao Miyazaki",
        "duration": "125 min",
        "rating": 4.9,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
        "aspects_preset": ["Graphics & Visuals", "Soundtrack & Audio", "Story & Narrative"],
        "reviews": [
            {
                "id": "m9",
                "author": "Aoi Miyazaki",
                "rating": 5,
                "date": "5 days ago",
                "text": "Joe Hisaishi's piano soundtrack 'One Summer's Day' brings tears to my eyes every single time. Hand-drawn animation filled with poetic wonder and soul."
            }
        ]
    },
    "across-the-spider-verse": {
        "id": "across-the-spider-verse",
        "type": "movie",
        "category": "animation",
        "category_label": "Animation / Superhero",
        "title": "Spider-Man: Across the Spider-Verse",
        "tagline": "It's how you wear the mask that matters.",
        "badge": "Visual Revolution",
        "director": "Kemp Powers, Joaquim Dos Santos",
        "duration": "140 min",
        "rating": 4.8,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg",
        "aspects_preset": ["Graphics & Visuals", "Soundtrack & Audio", "Direction & Acting"],
        "reviews": [
            {
                "id": "m10",
                "author": "Miles M.",
                "rating": 5,
                "date": "2 days ago",
                "text": "Every single frame could be hanging in a contemporary modern art museum. Combining watercolor Gwen Stacy dimensions with punk rock animation is pure genius."
            }
        ]
    },
    "the-matrix": {
        "id": "the-matrix",
        "type": "movie",
        "category": "sci-fi",
        "category_label": "Sci-Fi Cyberpunk",
        "title": "The Matrix (1999)",
        "tagline": "Welcome to the Real World.",
        "badge": "Cyberpunk Icon",
        "director": "Lana & Lilly Wachowski",
        "duration": "136 min",
        "rating": 4.9,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
        "aspects_preset": ["Story & Narrative", "Graphics & Visuals", "Gameplay & Combat"],
        "reviews": [
            {
                "id": "m11",
                "author": "Neo Anderson",
                "rating": 5,
                "date": "4 days ago",
                "text": "Pioneered bullet time and existential philosophical cinema. Keanu Reeves and Hugo Weaving deliver electric performances that redefined 21st century action."
            }
        ]
    },
    "avengers-endgame": {
        "id": "avengers-endgame",
        "type": "movie",
        "category": "action",
        "category_label": "Action / Superhero Epic",
        "title": "Avengers: Endgame (2019)",
        "tagline": "Part of the journey is the end.",
        "badge": "Box Office Giant",
        "director": "Anthony & Joe Russo",
        "duration": "181 min",
        "rating": 4.8,
        "image": "https://image.tmdb.org/t/p/w600_and_h900_bestv2/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
        "aspects_preset": ["Graphics & Visuals", "Direction & Acting", "Story & Narrative"],
        "reviews": [
            {
                "id": "m12",
                "author": "Tony Stark Fan",
                "rating": 5,
                "date": "1 week ago",
                "text": "The portal battle sequence and 'Avengers Assemble' scene gives goosebumps no matter how many times you watch it. Emotional, grand, and deeply satisfying."
            }
        ]
    },

    # =========================================================================
    # 3. VIDEO GAMES (OFFICIAL BOX ART POSTERS)
    # =========================================================================
    "elden-ring": {
        "id": "elden-ring",
        "type": "game",
        "category": "action-rpg",
        "category_label": "Action RPG / Soulslike",
        "title": "Elden Ring: Shadow of the Erdtree",
        "tagline": "Rise, Tarnished, and be guided by grace to brandish the Elden Ring.",
        "badge": "Game of the Year",
        "developer": "FromSoftware",
        "platform": "PC / PS5 / Xbox",
        "rating": 4.9,
        "price": "$59.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/library_600x900_2x.jpg",
        "aspects_preset": ["Gameplay & Combat", "World & Exploration", "Graphics & Visuals", "Soundtrack & Audio"],
        "reviews": [
            {
                "id": "g1",
                "author": "TarnishedOne",
                "rating": 5,
                "date": "2 days ago",
                "text": "FromSoftware's crowning achievement! The Lands Between offers peerless open-world discovery, punishing yet fair combat boss fights, and haunting art direction."
            },
            {
                "id": "g2",
                "author": "MaleniaSlayer",
                "rating": 5,
                "date": "5 days ago",
                "text": "Exploration feels truly magical. You see a glowing castle in the distance and you can actually journey there. Combat builds offer infinite replayability!"
            }
        ]
    },
    "cyberpunk-2077": {
        "id": "cyberpunk-2077",
        "type": "game",
        "category": "sci-fi",
        "category_label": "Open World / Sci-Fi RPG",
        "title": "Cyberpunk 2077: Phantom Liberty",
        "tagline": "Night City can swallow you whole. Become a mercenary outlaw.",
        "badge": "Ray-Tracing Showcase",
        "developer": "CD Projekt RED",
        "platform": "PC / PS5 / Xbox Series X",
        "rating": 4.8,
        "price": "$49.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1091500/library_600x900_2x.jpg",
        "aspects_preset": ["Graphics & Visuals", "Story & Narrative", "Performance & Optimization", "Gameplay & Combat"],
        "reviews": [
            {
                "id": "g3",
                "author": "JohnnySilverhand",
                "rating": 5,
                "date": "1 day ago",
                "text": "With the 2.0 overhaul and Phantom Liberty, Night City is the most immersive, breathtaking sci-fi open world ever created. Full path-tracing graphics look like real life!"
            },
            {
                "id": "g4",
                "author": "NetrunnerV",
                "rating": 5,
                "date": "4 days ago",
                "text": "Idris Elba and Keanu Reeves deliver phenomenal acting. Gunplay is tight, vehicle handling is responsive, and Dogtown's espionage storyline is top tier."
            }
        ]
    },
    "red-dead-redemption-2": {
        "id": "red-dead-redemption-2",
        "type": "game",
        "category": "open-world",
        "category_label": "Open World Western",
        "title": "Red Dead Redemption 2",
        "tagline": "Outlaws for life. America, 1899. The end of the wild west era.",
        "badge": "Narrative Masterpiece",
        "developer": "Rockstar Games",
        "platform": "PC / PS4 / Xbox",
        "rating": 5.0,
        "price": "$59.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1174180/library_600x900_2x.jpg",
        "aspects_preset": ["Story & Narrative", "World & Exploration", "Graphics & Visuals", "Direction & Acting"],
        "reviews": [
            {
                "id": "g5",
                "author": "ArthurMorgan",
                "rating": 5,
                "date": "3 days ago",
                "text": "The greatest story ever told in interactive entertainment. Arthur Morgan's character arc brings grown men to tears. The physics, wildlife simulation, and environmental details are astonishing."
            }
        ]
    },
    "the-witcher-3": {
        "id": "the-witcher-3",
        "type": "game",
        "category": "action-rpg",
        "category_label": "Action RPG / Dark Fantasy",
        "title": "The Witcher 3: Wild Hunt (Complete)",
        "tagline": "In a world torn by war, track down the Child of Prophecy.",
        "badge": "RPG Benchmark",
        "developer": "CD Projekt RED",
        "platform": "PC / PS5 / Switch",
        "rating": 4.9,
        "price": "$39.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/292030/library_600x900_2x.jpg",
        "aspects_preset": ["Story & Narrative", "Soundtrack & Audio", "World & Exploration"],
        "reviews": [
            {
                "id": "g6",
                "author": "GeraltOfRivia",
                "rating": 5,
                "date": "5 days ago",
                "text": "The Bloody Baron storyline sets the gold standard for quest writing. Slavic folk soundtrack is mesmerizing, and the Blood & Wine DLC is an entire masterpiece in itself."
            }
        ]
    },
    "gta-v": {
        "id": "gta-v",
        "type": "game",
        "category": "open-world",
        "category_label": "Action / Open World Heist",
        "title": "Grand Theft Auto V",
        "tagline": "Welcome to Los Santos. Trouble follows everywhere.",
        "badge": "All-Time Best Seller",
        "developer": "Rockstar Games",
        "platform": "PC / PS5 / Xbox Series X",
        "rating": 4.8,
        "price": "$29.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/271590/library_600x900_2x.jpg",
        "aspects_preset": ["Gameplay & Combat", "World & Exploration", "Story & Narrative"],
        "reviews": [
            {
                "id": "g7",
                "author": "MichaelTownley",
                "rating": 5,
                "date": "2 days ago",
                "text": "Multi-protagonist heists, satirical radio stations, and endless mayhem in Los Santos. Even a decade after release, it remains endlessly fun with friends."
            }
        ]
    },
    "baldurs-gate-3": {
        "id": "baldurs-gate-3",
        "type": "game",
        "category": "action-rpg",
        "category_label": "CRPG / D&D Fantasy",
        "title": "Baldur's Gate 3",
        "tagline": "Gather your party. Mysterious abilities awaken inside you.",
        "badge": "GOTY Winner",
        "developer": "Larian Studios",
        "platform": "PC / PS5 / Xbox Series X",
        "rating": 5.0,
        "price": "$59.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1086940/library_600x900_2x.jpg",
        "aspects_preset": ["Story & Narrative", "Gameplay & Combat", "Direction & Acting"],
        "reviews": [
            {
                "id": "g8",
                "author": "AstarionFan",
                "rating": 5,
                "date": "3 days ago",
                "text": "Unprecedented player freedom! Every encounter has a dozen distinct creative outcomes. Voice acting and companion romance storylines are unmatched in gaming history."
            }
        ]
    },
    "black-myth-wukong": {
        "id": "black-myth-wukong",
        "type": "game",
        "category": "action-rpg",
        "category_label": "Action / Mythological Soulslike",
        "title": "Black Myth: Wukong",
        "tagline": "Confront your destiny in Journey to the West.",
        "badge": "Unreal Engine 5 Showcase",
        "developer": "Game Science",
        "platform": "PC / PS5",
        "rating": 4.8,
        "price": "$59.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2358720/library_600x900_2x.jpg",
        "aspects_preset": ["Graphics & Visuals", "Gameplay & Combat", "Performance & Optimization"],
        "reviews": [
            {
                "id": "g9",
                "author": "DestinedOne",
                "rating": 5,
                "date": "1 day ago",
                "text": "Staggering visual fidelity with Unreal Engine 5 Nanite and Lumen! Staff combat feels snappy and acrobatic, and boss designs from Chinese mythology are awe-inspiring."
            }
        ]
    },
    "god-of-war-ragnarok": {
        "id": "god-of-war-ragnarok",
        "type": "game",
        "category": "action-rpg",
        "category_label": "Action Adventure / Norse Mythology",
        "title": "God of War Ragnarök",
        "tagline": "The Norse saga concludes. Kratos and Atreus face the twilight of the gods.",
        "badge": "PlayStation Titan",
        "developer": "Santa Monica Studio",
        "platform": "PS5 / PS4 / PC",
        "rating": 4.9,
        "price": "$69.99",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2322010/library_600x900_2x.jpg",
        "aspects_preset": ["Gameplay & Combat", "Story & Narrative", "Graphics & Visuals", "Soundtrack & Audio"],
        "reviews": [
            {
                "id": "g10",
                "author": "GhostOfSparta",
                "rating": 5,
                "date": "4 days ago",
                "text": "The Leviathan Axe and Blades of Chaos feel so visceral through the DualSense haptic feedback. Emotional father-son tale woven seamlessly with thunderous cinematic boss fights."
            }
        ]
    },

    # =========================================================================
    # 4. WORLD TOURIST DESTINATIONS (BY COUNTRY & REGION)
    # =========================================================================
    "kyoto-japan": {
        "id": "kyoto-japan",
        "type": "travel",
        "category": "japan",
        "category_label": "Japan / East Asia",
        "title": "Kyoto: Fushimi Inari & Arashiyama",
        "tagline": "Historic temples, 10,000 vermilion Torii gates, serene bamboo groves",
        "badge": "UNESCO Heritage",
        "country": "Japan",
        "best_season": "Spring (Cherry Blossoms) & Autumn",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Scenery & Natural Beauty", "Culture & Heritage", "Hospitality & Safety", "Food & Cuisine"],
        "reviews": [
            {
                "id": "t1",
                "author": "TravelerMaya",
                "rating": 5,
                "date": "2 days ago",
                "text": "Walking through the Fushimi Inari shrine at sunrise is a spiritual, life-changing experience. The quiet bamboo forest in Arashiyama and matcha tea ceremonies are unforgettable!"
            },
            {
                "id": "t2",
                "author": "Kenji Sato",
                "rating": 5,
                "date": "1 week ago",
                "text": "Incredibly clean, peaceful, and exceptionally safe. Public transportation with the JR pass is effortless, and traditional Kaiseki dinners are culinary art."
            }
        ]
    },
    "paris-france": {
        "id": "paris-france",
        "type": "travel",
        "category": "france",
        "category_label": "France / Europe",
        "title": "Paris: Eiffel Tower & The Louvre",
        "tagline": "The City of Light, world-class art, Haussmann architecture, Seine cruises",
        "badge": "Iconic Capital",
        "country": "France",
        "best_season": "May - September",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Culture & Heritage", "Scenery & Natural Beauty", "Food & Cuisine", "Affordability & Cost"],
        "reviews": [
            {
                "id": "t3",
                "author": "Emily Laurent",
                "rating": 5,
                "date": "3 days ago",
                "text": "Seeing the Eiffel Tower sparkle on the hour from the Trocadéro is pure romance! Croissants from local boulangeries and wandering Montmartre exceeded every dream."
            },
            {
                "id": "t4",
                "author": "Markus Weber",
                "rating": 4,
                "date": "5 days ago",
                "text": "The Louvre's art collection is staggering. Peak summer crowds and metro ticket lines can be intense, but the architecture and bistros make it well worth it."
            }
        ]
    },
    "rome-italy": {
        "id": "rome-italy",
        "type": "travel",
        "category": "italy",
        "category_label": "Italy / Southern Europe",
        "title": "Rome: Colosseum & Vatican City",
        "tagline": "The Eternal City, ancient gladiatorial arenas, Trevi Fountain, authentic pasta",
        "badge": "Ancient Wonder",
        "country": "Italy",
        "best_season": "April - June & Sept - Oct",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Culture & Heritage", "Food & Cuisine", "Scenery & Natural Beauty"],
        "reviews": [
            {
                "id": "t5",
                "author": "Giovanni Rossi",
                "rating": 5,
                "date": "4 days ago",
                "text": "Every cobblestone street feels like an open-air museum. Tossing a coin into Trevi Fountain and tasting authentic Carbonara in Trastevere is absolute bliss."
            }
        ]
    },
    "swiss-alps-zermatt": {
        "id": "swiss-alps-zermatt",
        "type": "travel",
        "category": "switzerland",
        "category_label": "Switzerland / Alps",
        "title": "Swiss Alps: Zermatt & The Matterhorn",
        "tagline": "Pyramidal alpine peaks, glacier hiking, Gornergrat railway, scenic fondue",
        "badge": "Alpine Majesty",
        "country": "Switzerland",
        "best_season": "Winter (Skiing) & Summer (Hiking)",
        "rating": 5.0,
        "image": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Scenery & Natural Beauty", "Hospitality & Safety", "Affordability & Cost"],
        "reviews": [
            {
                "id": "t6",
                "author": "Liam Anderson",
                "rating": 5,
                "date": "1 day ago",
                "text": "Unquestionably the most breathtaking mountain scenery on Earth. The reflection of the Matterhorn in Lake Riffelsee is postcard perfection. Punctual trains and pristine air!"
            }
        ]
    },
    "taj-mahal-india": {
        "id": "taj-mahal-india",
        "type": "travel",
        "category": "india",
        "category_label": "India / South Asia",
        "title": "Agra & Jaipur: Taj Mahal & Palace of Winds",
        "tagline": "Ivory-white marble mausoleum of eternal love, royal Rajasthani fortresses",
        "badge": "7 Wonders of the World",
        "country": "India",
        "best_season": "October - March",
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Culture & Heritage", "Scenery & Natural Beauty", "Food & Cuisine", "Affordability & Cost"],
        "reviews": [
            {
                "id": "t7",
                "author": "Ananya Sharma",
                "rating": 5,
                "date": "3 days ago",
                "text": "Seeing the Taj Mahal glow pink at sunrise takes your breath away. The intricate marble inlay work and the architectural symmetry are sheer genius. Incredible food and warmth!"
            }
        ]
    },
    "santorini-greece": {
        "id": "santorini-greece",
        "type": "travel",
        "category": "greece",
        "category_label": "Greece / Mediterranean",
        "title": "Santorini: Oia Sunsets & Aegean Sea",
        "tagline": "Whitewashed cliffside villas, cobalt blue domes, volcanic caldera views",
        "badge": "Mediterranean Jewel",
        "country": "Greece",
        "best_season": "May - October",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Scenery & Natural Beauty", "Hospitality & Safety", "Food & Cuisine"],
        "reviews": [
            {
                "id": "t8",
                "author": "Dimitris Alexiou",
                "rating": 5,
                "date": "5 days ago",
                "text": "The caldera sunsets in Oia are legendary. Sipping Greek wine overlooking the endless sapphire Aegean sea while the golden hour illuminates the whitewashed houses is unforgettable."
            }
        ]
    },
    "pyramids-giza-egypt": {
        "id": "pyramids-giza-egypt",
        "type": "travel",
        "category": "egypt",
        "category_label": "Egypt / North Africa",
        "title": "Giza: Great Pyramids & The Sphinx",
        "tagline": "4,500-year-old ancient wonder, pharaohs' tombs, Sahara desert vistas",
        "badge": "Ancient Wonder of the World",
        "country": "Egypt",
        "best_season": "November - April",
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Culture & Heritage", "Scenery & Natural Beauty", "Affordability & Cost"],
        "reviews": [
            {
                "id": "t9",
                "author": "Tariq Mansour",
                "rating": 5,
                "date": "1 week ago",
                "text": "Standing before the Great Pyramid of Khufu makes you realize how colossal human history is. The preservation across four millennia is awe-inspiring."
            }
        ]
    },
    "iceland-aurora-borealis": {
        "id": "iceland-aurora-borealis",
        "type": "travel",
        "category": "iceland",
        "category_label": "Iceland / Nordic",
        "title": "Iceland: Northern Lights & Blue Lagoon",
        "tagline": "Dancing emerald aurora borealis, geothermal hot springs, glaciers & waterfalls",
        "badge": "Geothermal Wonder",
        "country": "Iceland",
        "best_season": "Sept - March (Aurora) & June - Aug (Midnight Sun)",
        "rating": 5.0,
        "image": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=700&auto=format&fit=crop&q=80",
        "aspects_preset": ["Scenery & Natural Beauty", "Hospitality & Safety", "Culture & Heritage"],
        "reviews": [
            {
                "id": "t10",
                "author": "Freja Lindstrom",
                "rating": 5,
                "date": "4 days ago",
                "text": "Watching the green auroras dance across the starry Arctic sky while soaking in warm geothermal springs is otherworldly! Waterfalls like Skógafoss are thunderous and majestic."
            }
        ]
    }
}
