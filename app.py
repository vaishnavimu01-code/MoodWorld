# app.py

import os
import uuid

from flask import (
    Flask,
    render_template,
    request
)

from mood_engine import build_world_prompt
from generate_world import generate_world
from world_description import generate_description


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GENERATED_FOLDER = os.path.join(
    BASE_DIR,
    "static",
    "generated"
)

os.makedirs(GENERATED_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/generator")
def generator():
    return render_template("generator.html")


@app.route("/generate", methods=["POST"])
def generate():

    try:
        mood = request.form.get(
            "mood",
            "Peaceful"
        )

        environment = request.form.get(
            "environment",
            "Forest"
        )

        time_of_day = request.form.get(
            "time_of_day",
            "Sunset"
        )

        weather = request.form.get(
            "weather",
            "Foggy"
        )

        style = request.form.get(
            "style",
            "Fantasy"
        )

        custom_description = request.form.get(
            "custom_description",
            ""
        )

        # --------------------------------
        # STEP 1: Build AI Prompt
        # --------------------------------

        prompt = build_world_prompt(
            mood=mood,
            environment=environment,
            time_of_day=time_of_day,
            weather=weather,
            style=style,
            custom_description=custom_description
        )

        print("\nGenerated Prompt:")
        print(prompt)

        # --------------------------------
        # STEP 2: Generate Image
        # --------------------------------

        filename = (
            f"world_{uuid.uuid4().hex}.png"
        )

        output_path = os.path.join(
            GENERATED_FOLDER,
            filename
        )

        generate_world(
            prompt=prompt,
            output_path=output_path,
            steps=15
        )

        # --------------------------------
        # STEP 3: Generate Description
        # --------------------------------

        description = generate_description(
            mood=mood,
            environment=environment,
            time_of_day=time_of_day,
            weather=weather,
            style=style,
            custom_description=custom_description
        )

        # --------------------------------
        # STEP 4: Show Result
        # --------------------------------

        image_url = (
            f"/static/generated/{filename}"
        )

        return render_template(
            "result.html",
            image_url=image_url,
            description=description,
            mood=mood,
            environment=environment,
            time_of_day=time_of_day,
            weather=weather,
            style=style,
            custom_description=custom_description
        )

    except Exception as e:

        print("ERROR:", str(e))

        return render_template(
            "generator.html",
            error=(
                "Something went wrong while generating "
                "your world. Please try again."
            )
        )


if __name__ == "__main__":

    print("=" * 60)
    print("MOOD WORLD GENERATOR")
    print("=" * 60)

    print("Open:")
    print("http://127.0.0.1:5000")

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )