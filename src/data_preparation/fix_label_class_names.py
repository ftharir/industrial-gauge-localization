from dotenv import load_dotenv
load_dotenv()  # the paths below come from the .env file (see .env.example)
import os

folder_path = os.path.join(os.environ["GAUGE_DATASET_DIR"], "labels", "val")

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
        with open(filepath, 'w') as file:
            for line in lines:
                file.write(line.replace('meter', '0'))
                print("done")
