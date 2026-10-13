# Source code (the author's scripts)

The scripts written during the project (August 2024 - April 2025), **unchanged** except for their file names, which were made descriptive.
The folders the scripts read and write are **not hard-coded**: they come from environment variables that are read from a `.env` file (loaded with `python-dotenv`). Copy [`../.env.example`](../.env.example) to `.env` in the repository root, set the folders to your own, and run the scripts.

| Variable | Used by |
|---|---|
| `GAUGE_FRAMES_DIR` | `json_to_yolo.py`, `create_train_val_split.py`, `check_annotation_paths.py` (folder with one sub-folder per video) |
| `GAUGE_DATASET_DIR` | `fix_label_class_names.py`, `perspective_correction.py` (YOLO dataset folder) |
| `GAUGE_QUAD_INPUT_DIR`, `GAUGE_QUAD_OUTPUT_DIR` | `annotation/rectangle_to_four_points.py` |
| `GAUGE_CV_INPUT_DIR`, `GAUGE_CV_OUTPUT_DIR` | the thresholding / edge experiments |
| `GAUGE_AUG_INPUT_DIR`, `GAUGE_AUG_OUTPUT_DIR` | `augmentation/augment_images.py` |

The scripts are otherwise the author's originals; the only change is that each path line now reads its value from the environment.

| Folder | Script | What it does |
|---|---|---|
| `data_preparation/` | `extract_frames.py` | Takes 260 evenly spaced frames from a recording with OpenCV. |
| | `json_to_yolo.py` | Converts LabelMe rectangles (and circles) to YOLO text labels. |
| | `fix_label_class_names.py` | Replaces the label name `meter` by the class id `0` in YOLO files. |
| | `create_train_val_split.py` | Copies a random 80/20 split of every video folder into `dataset/images|labels/train|val`. |
| | `check_annotation_paths.py` | Checks that the annotation folders exist. |
| | `check_pytorch_cuda.py` | Prints the PyTorch version and whether CUDA is available. |
| `augmentation/` | `augment_images.py` | Makes one augmented copy of every frame with `albumentations`: rotation up to 20 degrees (p 0.5), horizontal flip (p 0.5), brightness / contrast (p 0.2) and Gaussian noise (p 0.2). It changes the images only, not the annotations. |
| `annotation/` | `rectangle_to_four_points.py` | Turns the two-point rectangles of LabelMe into four corner points. |
| `classical_cv/` | `perspective_correction.py` | Rectifies images with `cv2.getPerspectiveTransform`. |
| | `white_balance.py` | LAB-based white balance function (the call is left in a comment). |
| `classical_cv/thresholding_edge_experiments/` | nine scripts + `results.py` | Global, local and minimum-error (Otsu-type) thresholding, each alone, with Canny and with Sobel, and a script that lays the results side by side. |

The Colab notebook that ties the pipeline together is in [`../notebooks`](../notebooks). The images produced by the classical-CV scripts are in [`../results/classical_cv`](../results/classical_cv) (see [`classical_cv/README.md`](classical_cv/README.md)).
