# Roadmap

The detector is the first stage of a system that reads analog gauges automatically.

| Stage | Goal | Status |
|---|---|---|
| 1. Detection | Find the gauge in the frame | **Done** - YOLOv5s, mAP@0.5 0.995 |
| 2. Rectification | Crop and straighten the dial with the four corners (`annotations/quad_4point_2025`, perspective scripts in `src/classical_cv`) | Annotations ready |
| 3. Needle localisation | Find the needle and its angle (segmentation, Hough lines or keypoints) | Planned; classical thresholding / edge experiments in `results/classical_cv` |
| 4. Reading | Map the needle angle to a pressure value using the scale (for example -1 to 3 bar, 0 to 6 bar) | Planned |
| 5. Robustness | More scenes and gauge types, motion blur, reflections, several gauges per frame | Planned |

## Ideas for the data

* annotate the needle tip and the dial centre (keypoints) and the scale end points;
* record more gauges, distances and lighting conditions, including outdoor scenes;
* add frames with blur and glare on purpose, since the detector loses the gauge in blurred frames;
* label frames with several gauges.

## Ideas for evaluation

* validate on whole recordings that are not in the training set;
* report the error of the final pressure reading, not only the box quality.
