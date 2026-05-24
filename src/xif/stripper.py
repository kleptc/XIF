from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageOps


def strip_metadata(src_path: str | Path, dst_path: str | Path) -> None:
    with Image.open(src_path) as img:
        img = ImageOps.exif_transpose(img)
        clean = Image.new(img.mode, img.size)
        clean.putdata(list(img.getdata()))
        clean.save(dst_path)
