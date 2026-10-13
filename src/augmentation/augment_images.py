from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import cv2
import albumentations as A
import os

augmentation = A.Compose([
    A.Rotate(limit=20, p=0.5),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.GaussNoise(p=0.2)
])


input_folder = os.environ["GAUGE_AUG_INPUT_DIR"]
output_folder = os.environ["GAUGE_AUG_OUTPUT_DIR"]
os.makedirs(output_folder, exist_ok = True)


for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        img = cv2.imread(os.path.join(input_folder, filename))
        augmented = augmentation(image = img)["image"]
        cv2.imwrite(os.path.join(output_folder, filename), augmented)


