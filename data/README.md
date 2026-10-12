# Data

Everything here comes from three recordings of an analog pressure gauge (1920x1080, 30 fps).

| Folder / file | Content |
|---|---|
| `images/video_XX/` | 435 labelled frames taken from the recordings (JPEG, 1920x1080). |
| `labels/video_XX/` | YOLO labels (generated from annotation pass 1), one `.txt` per frame: `0 x_center y_center width height` (normalised). One class, `0 = gauge`. |
| `../annotations/` | The LabelMe annotations the author drew by hand (two passes and a four-point version), documented in [`../annotations/README.md`](../annotations/README.md). |
| `frames.csv` | Frame -> video -> source recording. |

## Videos and frames

| Folder | Frames | Source recording | Box covers (mean share of the frame) |
|---|---|---|---|
| `video_07` | 30 | `Pressure Gauge Reader Data.mov` (109 s) | 10 % (gauge seen from far away, among pipes) |
| `video_08` | 75 | `handheld15.mov` (59 s) | 48 % (close-up, hand-held) |
| `video_09` | 260 | `out5.mov` (122 s) | 34 % |
| `video_10` | 70 | `out5.mov` | 34 % (a second part of the same recording) |

`video_09` and `video_10` come from the same recording, so they must not be used as independent test sets for each other.
The recordings themselves (540 MB) are not part of the repository; `src/data_preparation/extract_frames.py` shows how the frames were taken from them.

## Not included

Frames, labels and recordings made by other people are not part of this repository.
