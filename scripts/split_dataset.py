import os
import random
import shutil
from tqdm import tqdm

def split_dataset(src_root='data/processed/all', dst_root='data/processed', train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, seed=42):
    random.seed(seed)
    print(f"Splitting dataset from {src_root} ...")

    for breed in os.listdir(src_root):
        breed_folder = os.path.join(src_root, breed)
        if not os.path.isdir(breed_folder):
            continue

        images = [f for f in os.listdir(breed_folder) if f.lower().endswith('.jpg')]
        random.shuffle(images)
        total = len(images)
        train_end = int(total * train_ratio)
        val_end = int(total * (train_ratio + val_ratio))

        splits = {
            'train': images[:train_end],
            'val': images[train_end:val_end],
            'test': images[val_end:]
        }

        for split_name, split_files in splits.items():
            dst_folder = os.path.join(dst_root, split_name, breed)
            os.makedirs(dst_folder, exist_ok=True)
            for img in tqdm(split_files, desc=f"{breed} → {split_name}", leave=False):
                src = os.path.join(breed_folder, img)
                dst = os.path.join(dst_folder, img)
                shutil.copy(src, dst)

    print("Split complete!")
    print(f"Data saved to {dst_root}")

if __name__ == "__main__":
    split_dataset()
