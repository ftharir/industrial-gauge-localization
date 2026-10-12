import cv2
import os

# نام فایل ویدئو را وارد کنید
video_path = 'out5.mov'  
output_folder = 'extracted_frames_out5'  # دایرکتوری خروجی برای فریم‌ها

# ایجاد دایرکتوری خروجی در صورت عدم وجود
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)

# بررسی اینکه آیا ویدئو به درستی باز شده است یا خیر
if not cap.isOpened():
    print("خطا در باز کردن ویدئو")
    exit()

# تعداد کل فریم‌ها
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# محاسبه فریم‌هایی که باید استخراج شوند
frame_indices = [int(i * total_frames / 260) for i in range(260)]

for i in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break

    # اگر فریم جاری در لیست فریم‌های مورد نظر باشد، آن را ذخیره کن
    if i in frame_indices:
        cv2.imwrite(os.path.join(output_folder, f'frame_{i}.jpg'), frame)

cap.release()
print(f"{len(frame_indices)} فریم استخراج شد و در پوشه '{output_folder}' ذخیره شد.")
