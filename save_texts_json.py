import json
from generate_text import generate_exoplanet_texts

texts = generate_exoplanet_texts()

with open("data/exoplanet_texts.json", "w") as f:
    json.dump(texts, f, indent=2)