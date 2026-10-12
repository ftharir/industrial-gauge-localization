# Classical computer vision

Thresholding, edge detection, perspective correction and white balance, tried before using a neural network.
**The images these scripts produced are in [`../../results/classical_cv`](../../results/classical_cv)** (a table there maps every output folder to its script).

| Script | Output folder in `results/classical_cv` |
|---|---|
| `thresholding_edge_experiments/global_thresholding*.py` (3 scripts) | `global_threshold`, `global_threshold_canny`, `global_threshold_sobel` |
| `thresholding_edge_experiments/local_thresholding*.py` (3 scripts) | `local_threshold`, `local_threshold_canny`, `local_threshold_sobel` |
| `thresholding_edge_experiments/minimum_error_thresholding*.py` (3 scripts) | `min_error_threshold`, `min_error_threshold_canny`, `min_error_threshold_sobel` |
| `thresholding_edge_experiments/results.py` | side-by-side figure ([`08_classical_cv_overview.png`](../../results/figures/08_classical_cv_overview.png)) |
| `perspective_correction.py` | `perspective_correction_output` |
| `white_balance.py` | `white_balance_input` (input only; the call is commented out in the script) |

The input and output folders are read from the `.env` file (`GAUGE_CV_INPUT_DIR`, `GAUGE_CV_OUTPUT_DIR`, `GAUGE_DATASET_DIR`); see [`../../.env.example`](../../.env.example).
