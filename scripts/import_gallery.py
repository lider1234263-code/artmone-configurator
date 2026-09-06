#!/usr/bin/env python3
"""Validate and import one 11-image ArtMone ribbon gallery.

Input files must use the shared naming convention AMCODE_01..AMCODE_11
and may be PNG, JPEG, or WebP. Output is a 1600x1600 WebP gallery plus
320x320 WebP thumbnails.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageOps


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
EXPECTED_SIZE = (1600, 1600)
THUMB_SIZE = (320, 320)


def normalize_code(value: str) -> str:
    code = value.strip().upper().replace("А", "A").replace("М", "M")
    code = re.sub(r"[\s_-]+", "", code)
    if not code.startswith("AM"):
        code = f"AM{code}"
    if not re.fullmatch(r"AM[A-Z0-9]+", code):
        raise ValueError(
            "AM code must contain only Latin letters and digits after normalization"
        )
    return code


def folder_name(code: str) -> str:
    return f"am-{code[2:].lower()}"


def collect_sources(source_dir: Path, code: str) -> list[Path]:
    expected_stems = {f"{code}_{index:02d}" for index in range(1, 12)}
    matches: dict[str, Path] = {}

    for path in source_dir.iterdir():
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        if path.stem not in expected_stems:
            continue
        if path.stem in matches:
            raise ValueError(f"Duplicate image number: {path.stem}")
        matches[path.stem] = path

    missing = sorted(expected_stems - matches.keys())
    if missing:
        raise ValueError("Missing gallery files: " + ", ".join(missing))

    return [matches[f"{code}_{index:02d}"] for index in range(1, 12)]


def convert_image(source: Path, destination: Path, size: tuple[int, int], quality: int) -> None:
    last_error: OSError | None = None
    for _attempt in range(3):
        try:
            with Image.open(source) as opened:
                image = ImageOps.exif_transpose(opened)
                image.load()
                if image.width != image.height:
                    raise ValueError(
                        f"{source.name}: expected a square image, got {image.width}x{image.height}"
                    )
                if image.size != size:
                    image = image.resize(size, Image.Resampling.LANCZOS)
                if image.mode not in {"RGB", "RGBA"}:
                    image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
                image.save(destination, "WEBP", quality=quality, method=4)
            with Image.open(destination) as check:
                check.load()
                if check.format != "WEBP" or check.size != size:
                    raise OSError(f"invalid generated image {destination.name}")
            return
        except OSError as error:
            last_error = error
    raise OSError(f"Failed to convert {source.name} after 3 attempts: {last_error}")


def import_gallery(source_dir: Path, destination_root: Path, code: str) -> Path:
    sources = collect_sources(source_dir, code)
    destination = destination_root / folder_name(code)
    destination.parent.mkdir(parents=True, exist_ok=True)

    staging = Path(tempfile.mkdtemp(prefix=f"{folder_name(code)}-"))
    try:
        full_staging = staging / "full"
        thumb_staging = staging / "thumbs"
        full_staging.mkdir()
        thumb_staging.mkdir()
        for index, source in enumerate(sources, start=1):
            filename = f"{code}_{index:02d}.webp"
            convert_image(source, full_staging / filename, EXPECTED_SIZE, 88)
            convert_image(source, thumb_staging / filename, THUMB_SIZE, 78)

        for output in sorted(full_staging.glob("*.webp")):
            with Image.open(output) as image:
                if image.format != "WEBP" or image.size != EXPECTED_SIZE:
                    raise ValueError(f"Invalid generated file: {output.name}")
        for output in sorted(thumb_staging.glob("*.webp")):
            with Image.open(output) as image:
                if image.format != "WEBP" or image.size != THUMB_SIZE:
                    raise ValueError(f"Invalid generated thumbnail: {output.name}")

        destination.mkdir(parents=True, exist_ok=True)
        thumbs_destination = destination / "thumbs"
        thumbs_destination.mkdir(parents=True, exist_ok=True)
        for output in sorted(full_staging.glob("*.webp")):
            output.replace(destination / output.name)
        for output in sorted(thumb_staging.glob("*.webp")):
            output.replace(thumbs_destination / output.name)
    finally:
        shutil.rmtree(staging, ignore_errors=True)

    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--code", required=True)
    parser.add_argument(
        "--destination-root",
        type=Path,
        default=PROJECT_ROOT / "assets" / "mockups",
    )
    args = parser.parse_args()

    try:
        code = normalize_code(args.code)
        source_dir = args.source.resolve()
        if not source_dir.is_dir():
            raise ValueError(f"Source directory does not exist: {source_dir}")
        destination = import_gallery(source_dir, args.destination_root.resolve(), code)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Imported {code}: 11 full WebP + 11 thumbnails -> {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
