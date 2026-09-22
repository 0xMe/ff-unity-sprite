# ff_sprite_decoder

Decode Unity UI sprite data from Free Fire asset files into structured Python objects.

## Installation

```bash
pip install ff-unity-sprite
```

## Usage

```python
from ff_unity_sprite import extract

sprites = extract("example.bin")

for sprite in sprites:
    print(sprite)
```

You can also save the extracted sprites as JSON:

```python
import json
from dataclasses import asdict

from ff_unity_sprite import extract

sprites = extract("example.bin")

with open("sprites_output.json", "w", encoding="utf-8") as f:
    json.dump(
        [asdict(sprite) for sprite in sprites],
        f,
        indent=4,
        ensure_ascii=False,
    )
```

## Requirements

- Python 3.10+
- UnityPy
