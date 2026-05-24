from __future__ import annotations
from pathlib import Path
from PIL import ExifTags, Image


def read_metadata(image_path: str | Path) -> dict[str, object]:
    with Image.open(image_path) as img:
        exif = img.getexif()

    return {ExifTags.TAGS.get(tag_id, tag_id): value for tag_id, value in exif.items()}

def print_metadata(image_path: str | Path) -> None:
    metadata = read_metadata(image_path)
    if not metadata:
        print("No EXIF metadata found.")
        return
    for tag, value in metadata.items():
        print(f"  {tag:30s}: {value}")
