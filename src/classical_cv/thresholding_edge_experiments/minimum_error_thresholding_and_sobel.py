from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import cv2
import numpy as np
import os

input_folder = os.environ["GAUGE_CV_INPUT_DIR"]
output_folder = os.path.join(os.environ["GAUGE_CV_OUTPUT_DIR"], "minimum_error_sobel_images")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        total_pixels = image.size
        current_max = 0
        threshold_value = 0

        for t in range(1, 256):
            weight_background = np.sum(hist[:t]) / total_pixels
            weight_foreground = np.sum(hist[t:]) / total_pixels

            if weight_background == 0 or weight_foreground == 0:
                continue

            mean_background = np.sum(np.arange(0, t) * hist[:t]) / np.sum(hist[:t])
            mean_foreground = np.sum(np.arange(t, 256) * hist[t:]) / np.sum(hist[t:])

            variance_between = weight_background * weight_foreground * (mean_background - mean_foreground) ** 2
            
            if variance_between > current_max:
                current_max = variance_between
                threshold_value = t

        _, thresh_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
        
        sobel_x = cv2.Sobel(thresh_image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(thresh_image, cv2.CV_64F, 0, 1, ksize=3)
        
        sobel_edges = cv2.magnitude(sobel_x, sobel_y)
        sobel_edges = np.uint8(sobel_edges)

        output_path = os.path.join(output_folder, f"minimum_error_sobel_{filename}")
        cv2.imwrite(output_path, sobel_edges)
        print(f"Minimum Error Thresholding and Sobel Edge Detection applied and saved for: {filename}")

print("Minimum Error Thresholding and Sobel Edge Detection completed for all images.")
