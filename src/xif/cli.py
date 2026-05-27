from __future__ import annotations
import argparse
from pathlib import Path
from xif import __version__
from xif.reader import print_metadata
from xif.stripper import strip_metadata


def main() -> None:
    parser = argparse.ArgumentParser(prog="xif", description="Strip EXIF metadata from images.")
    parser.add_argument("input", type=Path, help="Path to input image")
    parser.add_argument("-o", "--output", type=Path, help="Output path (default: <name>_clean<ext>)")
    parser.add_argument("--preview", action="store_true", help="Show metadata without stripping")
    parser.add_argument("--version", action="version", version=f"xif {__version__}")
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error(f"input not found: {args.input}")

    if args.preview:
        print_metadata(args.input)
        return

    output = args.output or args.input.with_stem(args.input.stem + "_clean")
    strip_metadata(args.input, output)
    print(f"Wrote {output}")

if __name__ == "__main__":
    main()
