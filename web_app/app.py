from flask import Flask, render_template, request, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os
from PIL import Image

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "pawdentify_cnn.h5")
CLASS_INDICES_PATH = os.path.join(BASE_DIR, "..", "models", "class_indices.json")
BREED_INFO_PATH = os.path.join(BASE_DIR, "..", "data", "breed_info.json")
IMG_SIZE = (224, 224)

model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_INDICES_PATH, "r") as f:
    class_indices = json.load(f)
inv_class_map = {v: k for k, v in class_indices.items()}

with open(BREED_INFO_PATH, "r", encoding="utf-8") as f:
    breed_info = json.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            upload_dir = os.path.join(BASE_DIR, "static", "uploads")
            os.makedirs(upload_dir, exist_ok=True)
            img_path = os.path.join(upload_dir, file.filename)
            file.save(img_path)

            # Web URL for displaying in the frontend
            img_url = url_for("static", filename=f"uploads/{file.filename}")

            # Prepare image for prediction
            img = Image.open(img_path).convert("RGB").resize(IMG_SIZE)
            x = np.expand_dims(np.array(img) / 255.0, axis=0)
            preds = model.predict(x)
            idx = np.argmax(preds, axis=1)[0]
            breed = inv_class_map[idx]
            confidence = round(float(np.max(preds)) * 100, 2)

            normalized_key = (
                breed.strip()
                .lower()
                .replace(" ", "_")
                .replace("-", "_")
                .replace("/", "_")
            )

            info = breed_info.get(normalized_key)
            if not info:
                info = {
                    "breed_name": breed.title(),
                    "group": "Unknown",
                    "origin": "Unknown",
                    "size": "Unknown",
                    "lifespan": "Unknown",
                    "temperament": "Unknown",
                    "description": "No description available.",
                    "nature": "Information not added yet.",
                    "health_issues": "Information not added yet.",
                    "health_care": "Information not added yet.",
                    "food_diet": "Information not added yet."
                }

            return render_template(
                "result.html",
                breed=breed,
                confidence=confidence,
                img_path=img_url,
                info=info
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
