from pathlib import Path
import argparse
from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser(
        description="Run YOLOv8 drone detection on an image or video."
    )

    parser.add_argument(
        "--model",
        required=True,
        help="Path to trained YOLOv8 model (.pt)"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to input image or video"
    )

    parser.add_argument(
        "--output",
        default="results/detection",
        help="Directory for detection results"
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

    model = YOLO(args.model)

    Path(args.output).mkdir(parents=True, exist_ok=True)

    model.predict(
        source=args.source,
        imgsz=args.imgsz,
        conf=args.conf,
        save=True,
        project=args.output,
        name="prediction",
        exist_ok=True
    )

    print("Detection completed successfully.")


if __name__ == "__main__":
    main()