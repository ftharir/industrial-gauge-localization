from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# آدرس فولدرها
base_folder = os.environ["GAUGE_CV_OUTPUT_DIR"]
folders = [
    "Global Thresholding",
    "global_canny_images",
    "global_sobel_images"
]

# لیست تصاویر برای بارگذاری
images = []
titles = []

# بارگذاری تصاویر از فولدرها
for folder in folders:
    folder_path = os.path.join(base_folder, folder)
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            image = cv2.imread(img_path)
            images.append(image)
            titles.append(folder)

# اندازه جدید برای تصاویر
resize_dim = (150, 150)  # تغییر اندازه به 150x150 پیکسل

# ایجاد یک تصویر جامع
num_images = len(images)
grid_size = int(np.ceil(num_images**0.5))  # اندازه گرید برای نمایش
fig, axs = plt.subplots(grid_size, grid_size, figsize=(10, 10))

# نمایش تصاویر و نام فولدرها
for i, ax in enumerate(axs.flat):
    if i < num_images:
        resized_image = cv2.resize(images[i], resize_dim)
        ax.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
        ax.set_title(titles[i], fontsize=10)
    ax.axis('off')  # عدم نمایش محور

plt.tight_layout()
plt.show()
