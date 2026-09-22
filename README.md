# ff-unity-sprite

Decode Unity UI sprite data from Free Fire asset files into clean Python objects. Simple, fast, no drama.

## Install

Install straight from GitHub:

```bash
pip install git+https://github.com/0xMe/ff-unity-sprite.git
```

## Usage

```python
from ff_unity_sprite import extract

sprites = extract("example.bin")

for sprite in sprites:
    print(sprite)
```

## Save as JSON

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

## Example Output

Want to see what the output looks like?

[View the example JSON](https://github.com/0xMe/ff-unity-sprite/blob/main/tests/sprites_output.json)

## Requirements

- Python 3.10+
- UnityPy
