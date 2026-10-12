from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import cv2
import numpy as np
import os

input_folder = os.environ["GAUGE_CV_INPUT_DIR"]
output_folder = os.path.join(os.environ["GAUGE_CV_OUTPUT_DIR"], "local_sobel_images")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

block_size = 11
constant_c = 2

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        thresh_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant_c)
        
        sobel_x = cv2.Sobel(thresh_image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(thresh_image, cv2.CV_64F, 0, 1, ksize=3)
        
        sobel_edges = cv2.magnitude(sobel_x, sobel_y)
        sobel_edges = np.uint8(sobel_edges)
        
        output_path = os.path.join(output_folder, f"local_sobel_{filename}")
        cv2.imwrite(output_path, sobel_edges)
        print(f"Local Thresholding and Sobel Edge Detection applied and saved for: {filename}")

print("Local Thresholding and Sobel Edge Detection completed for all images.")
