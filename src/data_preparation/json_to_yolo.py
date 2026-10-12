from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import os
import json

main_dir = os.environ["GAUGE_FRAMES_DIR"]

folders = ["7", "8", "9", "10"]

def convert_json_to_yolo(json_file, output_path):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    image_width = data['imageWidth']
    image_height = data['imageHeight']
    
    with open(output_path, 'w') as out_file:
        for shape in data['shapes']:
            label = shape['label']
            points = shape['points']

            if shape['shape_type'] == 'circle':
                cx, cy = points[0]
                radius = points[1][0] - cx
                x_min = cx - radius
                x_max = cx + radius
                y_min = cy - radius
                y_max = cy + radius
            else:
                x_min = min(points[0][0], points[1][0])
                x_max = max(points[0][0], points[1][0])
                y_min = min(points[0][1], points[1][1])
                y_max = max(points[0][1], points[1][1])
            
            x_center = (x_min + x_max) / 2.0 / image_width
            y_center = (y_min + y_max) / 2.0 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height
            
            out_file.write(f"{label} {x_center} {y_center} {width} {height}\n")


for folder in folders:
    json_folder = os.path.join(main_dir, folder, "annotation")
    txt_folder = os.path.join(main_dir, folder, "labels")
    os.makedirs(txt_folder, exist_ok=True)

    for json_file in os.listdir(json_folder):
        if json_file.endswith(".json"):
            json_path = os.path.join(json_folder, json_file)
            txt_filename = os.path.splitext(json_file)[0] + ".txt"
            txt_path = os.path.join(txt_folder, txt_filename)
            convert_json_to_yolo(json_path, txt_path)