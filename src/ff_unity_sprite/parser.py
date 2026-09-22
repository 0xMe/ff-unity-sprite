from __future__ import annotations

from pathlib import Path
from typing import Iterator

import UnityPy

from .models import UISpriteData
from .reader import BinaryReader, ParseError


HEADER_SIZE = 48
FIELD_COUNT = 14


def parse(data: bytes) -> list[UISpriteData]:
    """
    Parse serialized UISpriteData entries.

    Args:
        data: Raw MonoBehaviour serialized data.

    Returns:
        List of UISpriteData objects.
    """

    if not isinstance(data, bytes):
        raise TypeError(
            f"data must be bytes, got {type(data).__name__}"
        )

    if len(data) <= HEADER_SIZE:
        return []

    reader = BinaryReader(data, HEADER_SIZE)
    sprites: list[UISpriteData] = []

    while reader.remaining > 0:
        start = reader.offset

        try:
            name = reader.read_string()
            values = reader.read_int32s(FIELD_COUNT)
        except ParseError:
            break

        if not name:
            continue

        (
            x,
            y,
            width,
            height,
            cdn_width,
            cdn_height,
            border_left,
            border_right,
            border_top,
            border_bottom,
            padding_left,
            padding_right,
            padding_top,
            padding_bottom,
        ) = values

        sprites.append(
            UISpriteData(
                name=name,
                x=x,
                y=y,
                width=width,
                height=height,
                cdn_width=cdn_width,
                cdn_height=cdn_height,
                border_left=border_left,
                border_right=border_right,
                border_top=border_top,
                border_bottom=border_bottom,
                padding_left=padding_left,
                padding_right=padding_right,
                padding_top=padding_top,
                padding_bottom=padding_bottom,
            )
        )

        if reader.offset <= start:
            raise ParseError(
                f"Parser did not advance at 0x{start:X}"
            )

    return sprites


def extract(
    filename: str | Path,
) -> list[UISpriteData]:
    """
    Load a Unity asset and extract UISpriteData entries
    from its MonoBehaviour objects.
    """

    path = Path(filename)

    if not path.is_file():
        raise FileNotFoundError(path)

    environment = UnityPy.load(str(path))
    sprites: list[UISpriteData] = []

    for obj in environment.objects:
        if obj.type.name != "MonoBehaviour":
            continue

        try:

            raw = obj.get_raw_data()
            sprites.extend(parse(raw))

        except ParseError:
            # This MonoBehaviour isn't a valid UISpriteData payload.
            continue

    return sprites


def iter_extract(
    filename: str | Path,
) -> Iterator[UISpriteData]:
    """
    Generator version of extract().
    """

    path = Path(filename)

    if not path.is_file():
        raise FileNotFoundError(path)

    environment = UnityPy.load(str(path))

    for obj in environment.objects:
        if obj.type.name != "MonoBehaviour":
            continue
            
        try:
            raw = obj.get_raw_data()

            for sprite in parse(raw):
                yield sprite

        except ParseError:
            continue
