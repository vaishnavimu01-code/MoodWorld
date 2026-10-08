# mood_engine.py

MOOD_PROFILES = {
    "Happy": {
        "colors": "bright yellow, orange, turquoise and warm pastel colors",
        "lighting": "bright warm sunlight",
        "atmosphere": "joyful, vibrant, energetic and uplifting",
        "elements": "flowers, open spaces, colorful landscapes and gentle sunlight"
    },

    "Peaceful": {
        "colors": "soft blue, green, lavender and warm white",
        "lighting": "soft natural light",
        "atmosphere": "calm, peaceful, relaxing and harmonious",
        "elements": "trees, gentle water, flowers, soft clouds and open spaces"
    },

    "Romantic": {
        "colors": "rose pink, red, purple and warm gold",
        "lighting": "soft golden evening light",
        "atmosphere": "romantic, intimate, warm and dreamy",
        "elements": "flowers, candles, glowing lights and beautiful scenery"
    },

    "Melancholic": {
        "colors": "muted blue, grey, dark purple and desaturated colors",
        "lighting": "soft diffused overcast light",
        "atmosphere": "quiet, emotional, nostalgic and reflective",
        "elements": "rain, mist, empty streets, distant lights and cloudy skies"
    },

    "Anxious": {
        "colors": "dark blue, grey, black and deep red accents",
        "lighting": "dramatic low-key lighting",
        "atmosphere": "tense, mysterious, uneasy and dramatic",
        "elements": "storm clouds, fog, narrow paths, shadows and dramatic architecture"
    },

    "Excited": {
        "colors": "neon blue, purple, orange and vibrant colors",
        "lighting": "dynamic colorful lighting",
        "atmosphere": "energetic, futuristic, exciting and lively",
        "elements": "city lights, movement, glowing signs and dramatic landscapes"
    },

    "Calm": {
        "colors": "light blue, white, green and pastel colors",
        "lighting": "gentle morning light",
        "atmosphere": "serene, balanced, comfortable and relaxing",
        "elements": "water, trees, clouds, birds and peaceful landscapes"
    },

    "Dreamy": {
        "colors": "lavender, violet, pink, cyan and soft blue",
        "lighting": "ethereal glowing light",
        "atmosphere": "surreal, magical, dreamy and imaginative",
        "elements": "floating objects, glowing plants, stars, clouds and magical scenery"
    },

    "Mysterious": {
        "colors": "deep purple, dark blue, black and silver",
        "lighting": "moody moonlight and dramatic shadows",
        "atmosphere": "mysterious, cinematic, magical and intriguing",
        "elements": "fog, ancient structures, moonlight, forests and hidden pathways"
    },

    "Energetic": {
        "colors": "red, orange, electric blue and vivid colors",
        "lighting": "strong dramatic lighting",
        "atmosphere": "powerful, dynamic, exciting and intense",
        "elements": "motion, dramatic landscapes, glowing architecture and strong visual contrast"
    },

    "Hopeful": {
        "colors": "gold, light blue, green and warm pastel colors",
        "lighting": "beautiful sunrise light",
        "atmosphere": "optimistic, peaceful, inspiring and uplifting",
        "elements": "sunrise, open landscapes, flowers, mountains and birds"
    }
}


def get_mood_profile(mood):
    return MOOD_PROFILES.get(
        mood,
        MOOD_PROFILES["Peaceful"]
    )


def build_world_prompt(
    mood,
    environment,
    time_of_day,
    weather,
    style,
    custom_description=""
):
    profile = get_mood_profile(mood)

    prompt = f"""
Create a stunning {style} world representing the emotion of {mood}.

Environment:
{environment}

Time of day:
{time_of_day}

Weather:
{weather}

Emotional visual characteristics:
{profile['atmosphere']}

Color palette:
{profile['colors']}

Lighting:
{profile['lighting']}

Visual elements:
{profile['elements']}

Additional user description:
{custom_description}

The scene should strongly communicate the emotion of {mood}
through its colors, lighting, environment, atmosphere and composition.

Make the scene visually coherent and immersive.

High quality digital artwork, cinematic composition,
highly detailed environment, beautiful lighting,
realistic textures, atmospheric depth,
professional concept art, visually striking,
no text, no watermark, no people unless specifically requested.
"""

    return " ".join(prompt.split())