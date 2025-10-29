import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os
import sys
from PIL import Image
from matplotlib import pyplot as plt

MODEL_PATH = "models/pawdentify_cnn.h5"
CLASS_INDICES_PATH = "models/class_indices.json"
IMG_SIZE = (224, 224)
BREED_INFO_PATH = "data/breed_info.json"

model = tf.keras.models.load_model(MODEL_PATH)
with open(CLASS_INDICES_PATH, "r") as f:
    class_indices = json.load(f)
inv_class_map = {v: k for k, v in class_indices.items()}

breed_info = {}
if os.path.exists(BREED_INFO_PATH):
    with open(BREED_INFO_PATH, "r") as f:
        breed_info = json.load(f)

def predict_breed(img_path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize(IMG_SIZE)
    x = image.img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    idx = np.argmax(preds, axis=1)[0]
    breed = inv_class_map[idx]
    confidence = np.max(preds) * 100
    return breed, confidence

def get_breed_info(breed):
    return breed_info.get(breed.lower(), {"description": "No info available."})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/classify_and_describe.py <image_path>")
        sys.exit(1)

    img_path = sys.argv[1]
    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        sys.exit(1)

    breed, confidence = predict_breed(img_path)
    print(f"Predicted Breed: {breed}")
    print(f"Confidence: {confidence:.2f}%")

    if breed_info:
        info = get_breed_info(breed)
        for k, v in info.items():
            print(f"{k.capitalize()}: {v}")

    img = Image.open(img_path)
    plt.imshow(img)
    plt.title(f"{breed} ({confidence:.1f}%)")
    plt.axis("off")
    plt.show()
