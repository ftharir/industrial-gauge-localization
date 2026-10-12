from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import os
import json
from tkinter import filedialog, Tk

# مسیر فولدر ورودی و خروجی
input_folder = os.environ["GAUGE_QUAD_INPUT_DIR"]
output_folder = os.environ["GAUGE_QUAD_OUTPUT_DIR"]

# تابعی برای پردازش هر فایل JSON
def process_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    # استخراج مختصات دو نقطه
    points = data['shapes'][0]['points']

    # دو نقطه موجود
    x1, y1 = points[0]
    x2, y2 = points[1]

    # محاسبه مختصات ۴ نقطه مربع (مستطیل)
    top_left = (min(x1, x2), min(y1, y2))
    bottom_left = (min(x1, x2), max(y1, y2))
    top_right = (max(x1, x2), min(y1, y2))
    bottom_right = (max(x1, x2), max(y1, y2))

    # به روزرسانی مختصات با ۴ نقطه
    data['shapes'][0]['points'] = [top_left, bottom_left, bottom_right, top_right]

    # ذخیره فایل جدید
    return data

# ایجاد پوشه خروجی اگر وجود نداشته باشد
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# پردازش همه فایل‌های JSON در پوشه ورودی و ذخیره در پوشه خروجی
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        # پردازش فایل JSON و ذخیره آن
        updated_data = process_json(input_file_path)
        with open(output_file_path, 'w') as f:
            json.dump(updated_data, f, indent=4)

        print(f"Processed {filename} and saved to {output_file_path}")
