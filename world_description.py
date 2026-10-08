# world_description.py


def generate_description(
    mood,
    environment,
    time_of_day,
    weather,
    style,
    custom_description=""
):
    descriptions = {
        "Happy": (
            "The generated world represents happiness through bright colors, "
            "warm illumination and an open, welcoming environment."
        ),

        "Peaceful": (
            "The generated world represents a peaceful state of mind using "
            "soft colors, gentle lighting and a calm natural environment."
        ),

        "Romantic": (
            "The generated world creates a romantic atmosphere through warm "
            "lighting, soft colors and intimate visual elements."
        ),

        "Melancholic": (
            "The generated world expresses a melancholic mood through muted "
            "colors, soft lighting, atmospheric weather and a quiet environment."
        ),

        "Anxious": (
            "The generated world reflects anxiety through darker colors, "
            "dramatic lighting, shadows and an unsettling atmosphere."
        ),

        "Excited": (
            "The generated world communicates excitement through vibrant "
            "colors, dynamic lighting and energetic environmental elements."
        ),

        "Calm": (
            "The generated world expresses calmness through gentle colors, "
            "soft natural lighting and harmonious environmental details."
        ),

        "Dreamy": (
            "The generated world creates a dreamlike experience using "
            "ethereal lighting, magical colors and surreal environmental details."
        ),

        "Mysterious": (
            "The generated world creates a mysterious atmosphere through "
            "deep colors, dramatic shadows, fog and cinematic lighting."
        ),

        "Energetic": (
            "The generated world communicates energy through vivid colors, "
            "strong lighting and dynamic environmental composition."
        ),

        "Hopeful": (
            "The generated world expresses hope through warm light, open "
            "landscapes and optimistic colors."
        )
    }

    opening = descriptions.get(
        mood,
        descriptions["Peaceful"]
    )

    custom_part = ""

    if custom_description.strip():
        custom_part = (
            f" The user's additional idea was: "
            f"{custom_description.strip()}."
        )

    description = f"""
{opening}

The environment is a {environment} scene set during {time_of_day}.
The weather is {weather}, which contributes to the overall emotional tone.

The visual style is {style}. The composition uses the environment,
lighting and color palette to create a world that visually communicates
the selected mood of {mood}.

The generated scene is designed to feel immersive and visually coherent,
with atmospheric depth, detailed surroundings and cinematic presentation.

Overall Mood:
{mood}

Environment:
{environment}

Time:
{time_of_day}

Weather:
{weather}

Visual Style:
{style}
{custom_part}
"""

    return "\n".join(
        line.strip()
        for line in description.strip().splitlines()
        if line.strip()
    )