from ff_unity_sprite import extract
import json
from dataclasses import asdict

sprites = extract("example.bin") # Real name: 7f91bb5fc7618ab4cbd2205b48abb0b8

with open("sprites_output.json", "w", encoding="utf-8") as f:
    json.dump(
        [asdict(sprite) for sprite in sprites],
        f,
        indent=4,
        ensure_ascii=False,
    )
