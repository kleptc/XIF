# Read EXIF metadata from image files

from __future__ import annotations

from pathlib import Path

from PIL import ExifTags, Image


def read_metadata(image_path: str | Path) -> dict[str, object]:
    with Image.open(image_path) as img:
        exif = img.getexif()

    return {ExifTags.TAGS.get(tag_id, tag_id): value for tag_id, value in exif.items()}
