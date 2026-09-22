from __future__ import annotations

import struct


class ParseError(ValueError):
    """Raised when serialized Unity data cannot be parsed."""


class BinaryReader:
    __slots__ = ("_data", "_offset")

    def __init__(self, data: bytes, offset: int = 0) -> None:
        self._data = data
        self._offset = offset

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def remaining(self) -> int:
        return len(self._data) - self._offset

    def require(self, size: int) -> None:
        if size < 0 or self._offset + size > len(self._data):
            raise ParseError(
                f"Unexpected end of buffer at "
                f"0x{self._offset:X}"
            )

    def read_uint32(self) -> int:
        self.require(4)

        value = struct.unpack_from(
            "<I",
            self._data,
            self._offset,
        )[0]

        self._offset += 4
        return value

    def read_int32s(self, count: int) -> tuple[int, ...]:
        size = count * 4
        self.require(size)

        values = struct.unpack_from(
            f"<{count}i",
            self._data,
            self._offset,
        )

        self._offset += size
        return values

    def read_string(self) -> str:
        length = self.read_uint32()

        self.require(length)

        raw = self._data[
            self._offset:
            self._offset + length
        ]

        self._offset += length

        try:
            value = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ParseError(
                f"Invalid UTF-8 at 0x{self._offset - length:X}"
            ) from exc

        # 4-byte alignment.
        self._offset = (self._offset + 3) & ~3

        return value
