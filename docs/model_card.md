# Model card - gauge detector

| | |
|---|---|
| **Task** | Object detection: find the dial of an analog pressure gauge in an image or video frame (one class, `gauge`) |
| **Model** | YOLOv5s (ultralytics 8.2.85), fine-tuned from the pre-trained `yolov5s` weights |
| **Training** | 100 epochs, batch 16, image size 640, default ultralytics augmentation; code: notebook cells 26-28 |
| **Training data** | 348 frames (80 %) of the 435 hand-annotated frames, from three recordings |
| **Validation data** | 87 frames (20 %), random split, no frame in both sets |
| **Files** | `models/best.pt` (PyTorch, 18.5 MB) and `models/best.onnx` (ONNX, 36.7 MB; gives the same box as the `.pt` file on the test image) |

## Results

| Validation (87 frames) | |
|---|---|
| Precision | 0.999 |
| Recall | 1.000 |
| mAP@0.5 | 0.995 |
| mAP@0.5:0.95 | 0.977 - 0.978 |

On three videos that were never annotated (every second frame, threshold 0.25): `handheld13` 100 % of frames detected, `handheld8` 100 %, `Pressure Gauge Reader` 27 % (see the README and `results/demo/unseen_videos`).

## Speed

Measured with `yolo val`, batch size 1, 640 px, on the author's laptop (Intel Core i9-13900H, NVIDIA RTX 3050 6 GB Laptop GPU):

| Device | Pre-process | Inference | Post-process | Total per image | Approx. FPS |
|---|---|---|---|---|---|
| GPU (CUDA) | 1.6 ms | 55.5 ms | 10.6 ms | 67.7 ms | 15 |
| CPU | 2.9 ms | 599.6 ms | 2.7 ms | 605.2 ms | 2 |

## Intended use

* Locating a gauge so that its dial can be cropped for the next stage (reading the needle).
* A starting point or baseline for gauge detection in similar indoor industrial scenes.

## Limits

* **Few scenes:** training frames come from three recordings (three gauges, indoor, similar lighting). Other gauge types, outdoor light or strong reflections are untested.
* **Blur and fast motion:** on the unlabelled video with fast hand-held motion, the gauge was found in only about a quarter of the frames (mostly when sharp and in view).
* **One gauge per frame:** the labels contain exactly one box per frame; frames with several gauges (a second gauge is visible in some frames) were annotated for the main one only.
* **Validation caveat:** the validation frames come from the same recordings as the training frames, so the validation scores describe familiar scenes; the unseen-video results are the better guide to new scenes.
* **Not a reading model:** the detector only draws a box; it does not read the pressure value.
* **Not for safety-critical use.**
