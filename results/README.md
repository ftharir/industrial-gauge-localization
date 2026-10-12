# Results

| Folder | Content |
|---|---|
| `demo/` | `yolo_detection_result.mp4` (20 s) and a GIF of its first 9 s: the detector running on a video. `demo/unseen_videos/` has the detector on three never-annotated videos (clips, gallery image, confidence over time, detection rates). |
| `yolo_training/` | Output of the notebook's YOLOv5s training: `results.csv` and `results.png` (curves), confusion matrices, PR/F1/P/R curves, label statistics, validation predictions and (the trained weights are in `../models/best.pt`). |
| `figures/` | Plots of the data analysis (frames, box position and size, annotation agreement, sample frames, overlap of the old train/val folders, classical-CV overview). |
| `tables/` | CSV tables behind those plots (per-frame box statistics, per-video summary). |
| `classical_cv/` | Outputs of the thresholding / Canny / Sobel experiments, the perspective-correction output and the white-balance input. The code that made them is in [`../src/classical_cv`](../src/classical_cv); a table in `classical_cv/README.md` maps each folder to its script. |
