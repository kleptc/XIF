from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageOps


def strip_metadata(src_path: str | Path, dst_path: str | Path) -> None:
    with Image.open(src_path) as img:
        img = ImageOps.exif_transpose(img)
        icc_profile = img.info.get("icc_profile")
        clean = Image.new(img.mode, img.size)
        clean.putdata(list(img.getdata()))
        clean.save(dst_path, icc_profile=icc_profile)
