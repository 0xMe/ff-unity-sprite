from pathlib import Path

import pytest

from ff_unity_sprite import extract


FIXTURE = Path(__file__).parent / "fixtures" / "example.bin"


@pytest.mark.skipif(
    not FIXTURE.exists(),
    reason="example.bin fixture is not available",
)
def test_extract():
    sprites = extract(FIXTURE)

    assert sprites
