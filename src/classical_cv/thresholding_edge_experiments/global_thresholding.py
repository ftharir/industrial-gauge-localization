from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import cv2
import os

input_folder = os.environ["GAUGE_CV_INPUT_DIR"]
output_folder = os.path.join(os.environ["GAUGE_CV_OUTPUT_DIR"], "thresholded_images")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

threshold_value = 128

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        _, thresh_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
        output_path = os.path.join(output_folder, f"thresholded_{filename}")
        cv2.imwrite(output_path, thresh_image)
        print(f"Thresholding applied and saved for: {filename}")

print("Global Thresholding completed for all images.")
