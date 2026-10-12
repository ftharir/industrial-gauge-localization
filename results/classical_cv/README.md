# Classical image-processing results

Outputs of the thresholding / edge-detection experiments, made on the five input frames in `input_frames/`.
**The code that produced each folder is in [`../../src/classical_cv`](../../src/classical_cv).**

| Output folder | Method | Script (in `src/classical_cv/thresholding_edge_experiments/`) |
|---|---|---|
| `global_threshold/` | global threshold (value 128) | `global_thresholding.py` |
| `global_threshold_canny/` | global threshold + Canny | `global_thresholding_and_canny.py` |
| `global_threshold_sobel/` | global threshold + Sobel | `global_thresholding_and_sobel.py` |
| `local_threshold/` | adaptive (local mean) threshold | `local_thresholding.py` |
| `local_threshold_canny/` | local threshold + Canny | `local_thresholding_and_canny.py` |
| `local_threshold_sobel/` | local threshold + Sobel | `local_thresholding_and_sobel.py` |
| `min_error_threshold/` | threshold that maximises the between-class variance | `minimum_error_thresholding.py` |
| `min_error_threshold_canny/` | same + Canny | `minimum_error_thresholding_and_canny.py` |
| `min_error_threshold_sobel/` | same + Sobel | `minimum_error_thresholding_and_sobel.py` |
| `perspective_correction_output/` | perspective rectification of 412 frames | `../perspective_correction.py` |
| `white_balance_input/` | input image of the white-balance function | `../white_balance.py` |

Side-by-side overview: [`../figures/08_classical_cv_overview.png`](../figures/08_classical_cv_overview.png).
