# Dataset card

| | |
|---|---|
| **Name** | Industrial gauge frames with hand-made boxes |
| **Content** | 435 video frames (1920x1080, JPEG) of analog pressure gauges, plus 435 augmented frames |
| **Task** | Gauge detection (one box per frame, one class) |
| **Source** | Three recordings (30 fps, 59 s to 122 s); frames were extracted at even intervals |
| **Annotation** | By hand with LabelMe 5.5.0, twice (2024 and 2025); a four-corner version and annotations of the augmented frames are included |
| **Formats** | LabelMe JSON (`annotations/`), YOLO text labels (`data/labels/`) |
| **Period** | August 2024 - April 2025 |
| **Licence** | Annotations, documentation and code: MIT. Please credit the repository when using the data. |

## Composition

| Video | Frames | Source recording | Gauge share of the frame | Scene |
|---|---|---|---|---|
| `video_07` | 30 | `Pressure Gauge Reader Data.mov` | 10 % | gauge seen from far away among pipes |
| `video_08` | 75 | `handheld15.mov` | 48 % | hand-held close-up of a gauge with a 6 bar scale |
| `video_09` | 260 | `out5.mov` | 34 % | fixed view of a gauge in front of a wall |
| `video_10` | 70 | `out5.mov` | 34 % | second part of the same recording |

## Annotation quality

* Two independent passes over the same frames: mean IoU 0.845 between them (see [`annotations/README.md`](../annotations/README.md)).
* Box size is the same in both passes; they differ mostly by a shift of about 60 px.

## Augmented frames

`data/augmented/images` holds one augmented version of each frame (81 are mirrored, 77 are unchanged and 277 carry another change such as brightness or a small geometric change). The augmented annotations (`annotations/labelme_augmented_2025`) repeat the boxes of the original frames, so they are exact for unchanged and brightness-changed frames and approximate for mirrored or geometrically changed ones.

## Known issues

* Frames of one video are consecutive samples of the same recording and look alike; a random split puts near-duplicates on both sides.
* Only three recordings: limited variety of gauges, backgrounds and lighting.
* The source recordings (540 MB) are not in the repository.
* A second, older train/val folder had 128 of its 151 validation frames also in training; it is not used (see [`data_audit.md`](data_audit.md)).
