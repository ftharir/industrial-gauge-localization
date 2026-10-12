# Pipeline

```
recordings (.mov)
   |  extract_frames.py / notebook cells 1-10        evenly spaced frames, 1920x1080
   v
frames (435 used here)
   |  LabelMe, rectangle around the gauge            annotation pass 1 (2024), pass 2 (2025)
   v
LabelMe json
   |  json_to_yolo.py, fix_label_class_names.py      YOLO text labels, class 0 = gauge
   v
YOLO labels  --->  create_train_val_split.py (random 80/20 per video)
   |  notebook cells 26-28  (YOLOv5s, 100 epochs, batch 16, 640 px)
   v
best.pt  --->  results/yolo_training (curves, matrices, predictions), results/demo
```

Parallel experiments on the same frames (not used by the detector): thresholding and edge detection (`results/classical_cv`), perspective correction, white balance, and a four-point version of the annotation (`annotations/quad_4point_2025`) intended for perspective rectification of the gauge face.

The long-term goal is to read the needle angle and translate it into a pressure value; this repository covers the first stage, finding the gauge in the frame.
