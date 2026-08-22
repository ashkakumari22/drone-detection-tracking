# Model Information

## Model

YOLOv8n trained for single-class drone detection.

- Architecture: YOLOv8n
- Task: Object Detection
- Number of classes: 1
- Class: `drone`
- Input image size: 640 × 640
- Training epochs: 30
- Batch size: 16
- Dataset format: YOLOv8
- Dataset: UAVs
- Base model: `yolov8n.pt`

## Final Evaluation

| Metric | Score |
|---|---:|
| Precision | 95.11% |
| Recall | 94.01% |
| mAP@50 | 97.09% |
| mAP@50–95 | 71.39% |

## Tracking

The trained YOLOv8n model is used with ByteTrack for multi-drone tracking.

The final tracking configuration uses:

- `track_high_thresh`: 0.20
- `track_low_thresh`: 0.05
- `new_track_thresh`: 0.20
- `track_buffer`: 120
- `match_thresh`: 0.95
- `fuse_score`: True

The increased track buffer and association threshold were used to improve identity persistence during temporary drone overlap/occlusion.

## Model Weights

The trained `.pt` weights are not included directly in this repository.

The original trained model is:

`drone_yolov8n_best.pt`

The repository contains the training notebook, evaluation results, and inference/tracking scripts needed to reproduce the workflow.