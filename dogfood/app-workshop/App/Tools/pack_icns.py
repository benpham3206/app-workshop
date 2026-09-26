#!/usr/bin/env python3
"""Package already-rendered PNGs into a Mac .icns for the local dogfood build."""

import argparse
import struct
from pathlib import Path


SIZES = (
    ("icp4", 16, "icon_16x16.png"),
    ("icp5", 32, "icon_32x32.png"),
    ("icp6", 64, "icon_32x32@2x.png"),
    ("ic07", 128, "icon_128x128.png"),
    ("ic08", 256, "icon_256x256.png"),
    ("ic09", 512, "icon_512x512.png"),
    ("ic10", 1024, "icon_512x512@2x.png"),
)


def png_size(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("Expected a PNG with an IHDR chunk")
    return struct.unpack(">II", data[16:24])


def build_icon(iconset, output):
    chunks = []
    for code, size, filename in SIZES:
        data = (iconset / filename).read_bytes()
        if png_size(data) != (size, size):
            raise ValueError(f"{filename} must be {size} by {size} pixels")
        chunks.append(code.encode("ascii") + struct.pack(">I", len(data) + 8) + data)
    body = b"".join(chunks)
    output.write_bytes(b"icns" + struct.pack(">I", len(body) + 8) + body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iconset", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build_icon(args.iconset, args.output)
