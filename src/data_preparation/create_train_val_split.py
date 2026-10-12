from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import os
import shutil
import random

main_dir = os.environ["GAUGE_FRAMES_DIR"]
output_dir = "dataset/"

os.makedirs(os.path.join(output_dir, "images/train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images/val"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels/train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels/val"), exist_ok=True)

folders = ["7", "8", "9", "10"]

split_ratio = 0.8

def copy_files(image_files, label_files, split):
    for i, file in enumerate(image_files):
        if i < split:
            shutil.copy(file, os.path.join(output_dir, "images/train"))
            shutil.copy(label_files[i], os.path.join(output_dir, "labels/train"))
        else:
            shutil.copy(file, os.path.join(output_dir, "images/val"))
            shutil.copy(label_files[i], os.path.join(output_dir, "labels/val"))

for folder in folders:
    image_dir = os.path.join(main_dir, folder)
    label_dir = os.path.join(main_dir, folder, "labels")
    
    images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]
    labels = [os.path.join(label_dir, f.replace('.jpg', '.txt')) for f in os.listdir(image_dir) if f.endswith('.jpg')]
    
    labels = [f for f in labels if os.path.exists(f)]
    
    print(f"Folder: {folder}, Images found: {len(images)}, Labels found: {len(labels)}")
    
    if len(images) == 0 or len(labels) == 0:
        print(f"No valid images or labels found in folder: {folder}")
        continue
    
    combined = list(zip(images, labels))
    random.shuffle(combined)
    
    if len(combined) == 0:
        print(f"No pairs of images and labels found in folder: {folder}")
        continue
    
    images[:], labels[:] = zip(*combined)
    
    split = int(len(images) * split_ratio)
    
    copy_files(images, labels, split)
    print("Done")