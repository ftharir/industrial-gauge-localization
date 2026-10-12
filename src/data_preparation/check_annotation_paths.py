from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import os

main_dir = os.environ["GAUGE_FRAMES_DIR"]
folders = ["7", "8", "9", "10"]

for folder in folders:
    json_folder = os.path.join(main_dir, folder, "annotation")
    if not os.path.exists(json_folder):
        print(f"Path does not exist: {json_folder}")
    else:
        print(f"Path exists: {json_folder}")
