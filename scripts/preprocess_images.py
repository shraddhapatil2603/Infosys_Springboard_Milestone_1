import os
from PIL import Image
from tqdm import tqdm

def preprocess_images(src_root='data/raw/organized_train', dst_root='data/processed/all', size=(224,224)):
    os.makedirs(dst_root, exist_ok=True)
    print(f"Preprocessing images from {src_root} ...")

    for breed_folder in os.listdir(src_root):
        src_folder = os.path.join(src_root, breed_folder)
        if not os.path.isdir(src_folder):
            continue

        for img_name in tqdm(os.listdir(src_folder), desc=f"{breed_folder}"):
            if not img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            src_path = os.path.join(src_folder, img_name)
            dst_folder = os.path.join(dst_root, breed_folder)
            os.makedirs(dst_folder, exist_ok=True)
            dst_path = os.path.join(dst_folder, img_name)

            try:
                img = Image.open(src_path).convert('RGB')
                img = img.resize(size, Image.Resampling.LANCZOS)
                img.save(dst_path, format='JPEG', quality=95)
            except Exception as e:
                print(f"Error processing {src_path}: {e}")

    print(f"Preprocessing complete! Saved to {dst_root}")

if __name__ == "__main__":
    preprocess_images()
