from pathlib import Path
import argparse
from ultralytics import YOLO


TRACKER_CONFIG = """
tracker_type: bytetrack
track_high_thresh: 0.20
track_low_thresh: 0.05
new_track_thresh: 0.20
track_buffer: 120
match_thresh: 0.95
fuse_score: True
"""


def main():
    parser = argparse.ArgumentParser(
        description="Run YOLOv8 + ByteTrack drone tracking."
    )

    parser.add_argument(
        "--model",
        required=True,
        help="Path to trained YOLOv8 model (.pt)"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to input video"
    )

    parser.add_argument(
        "--output",
        default="results/tracking",
        help="Directory for tracking results"
    )

    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Detection confidence threshold"
    )

    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Inference image size"
    )

    args = parser.parse_args()

    tracker_path = Path("bytetrack_custom.yaml")
    tracker_path.write_text(TRACKER_CONFIG)

    model = YOLO(args.model)

    Path(args.output).mkdir(parents=True, exist_ok=True)

    model.track(
        source=args.source,
        imgsz=args.imgsz,
        conf=args.conf,
        tracker=str(tracker_path),
        persist=True,
        save=True,
        project=args.output,
        name="tracking",
        exist_ok=True
    )

    print("Tracking completed successfully.")


if __name__ == "__main__":
    main()