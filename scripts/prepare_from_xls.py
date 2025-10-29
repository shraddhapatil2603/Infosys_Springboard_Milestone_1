import os
import shutil
import pandas as pd
from tqdm import tqdm

RAW_DIR = "data/raw"
TRAIN_DIR = os.path.join(RAW_DIR, "train")
LABELS_CSV = os.path.join(RAW_DIR, "labels.csv")
OUTPUT_DIR = os.path.join("data", "raw", "organized_train")

def organize_images():
    df = pd.read_csv(LABELS_CSV)
    print("Total labeled images:", len(df))
    print("Columns:", df.columns.tolist())

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for _, row in tqdm(df.iterrows(), total=len(df)):
        img_id = row['id']
        breed = row['breed']
        src = os.path.join(TRAIN_DIR, f"{img_id}.jpg")
        dst_folder = os.path.join(OUTPUT_DIR, breed)
        os.makedirs(dst_folder, exist_ok=True)
        dst = os.path.join(dst_folder, f"{img_id}.jpg")

        if os.path.exists(src):
            shutil.copy(src, dst)
        else:
            print(f" Missing: {src}")

    print("Organization complete.")
    print(f"Images organized under: {OUTPUT_DIR}")

if __name__ == "__main__":
    organize_images()
