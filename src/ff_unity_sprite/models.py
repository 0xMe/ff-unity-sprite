from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class UISpriteData:
    name: str

    x: int
    y: int
    width: int
    height: int

    cdn_width: int
    cdn_height: int

    border_left: int
    border_right: int
    border_top: int
    border_bottom: int

    padding_left: int
    padding_right: int
    padding_top: int
    padding_bottom: int

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    @property
    def cdn_size(self) -> tuple[int, int]:
        return self.cdn_width, self.cdn_height

    @property
    def borders(self) -> tuple[int, int, int, int]:
        return (
            self.border_left,
            self.border_right,
            self.border_top,
            self.border_bottom,
        )

    @property
    def padding(self) -> tuple[int, int, int, int]:
        return (
            self.padding_left,
            self.padding_right,
            self.padding_top,
            self.padding_bottom,
        )
