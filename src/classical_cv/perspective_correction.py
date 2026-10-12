from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import cv2
import numpy as np
import os

# تابع برای انجام پرسپکتیو کرکشن
def correct_perspective(image_path, output_path, points_src, points_dst, output_size):
    # خواندن تصویر ورودی
    image = cv2.imread(image_path)
    
    # محاسبه ماتریس تغییر پرسپکتیو
    matrix = cv2.getPerspectiveTransform(points_src, points_dst)
    
    # اعمال ماتریس بر روی تصویر
    corrected_image = cv2.warpPerspective(image, matrix, output_size)
    
    # ذخیره تصویر تصحیح شده
    cv2.imwrite(output_path, corrected_image)

# پوشه حاوی تصاویر ورودی
input_folder = os.path.join(os.environ["GAUGE_DATASET_DIR"], "images", "train")
output_folder = 'output_images'

# اطمینان از وجود پوشه خروجی
os.makedirs(output_folder, exist_ok=True)

# نقاط مرجع از تصویر اصلی (به ترتیب بالا-چپ، بالا-راست، پایین-راست، پایین-چپ)
points_src = np.float32([[100, 150], [400, 150], [400, 400], [100, 400]])

# نقاط مقصد برای تصویر تصحیح شده (به عنوان یک مستطیل مستقیم)
points_dst = np.float32([[0, 0], [300, 0], [300, 300], [0, 300]])

# اندازه تصویر خروجی
output_size = (300, 300)

# پردازش تمامی تصاویر در پوشه ورودی
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # انجام پرسپکتیو کرکشن
        correct_perspective(input_path, output_path, points_src, points_dst, output_size)
        
        print(f'Processed {filename}')

print("All images have been processed and saved in the output folder.")
