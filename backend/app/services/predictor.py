import json
from pathlib import Path
import random

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "tanks.json"

def load_tanks():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def predict_dummy():
    tanks = load_tanks()
    tank = random.choice(tanks)

    return {
        "tank_id": tank["id"],
        "name": tank["label"],
        "confidence": round(random.uniform(0.75, 0.98), 2),
        "description": tank.get("description_ar", tank.get("description_en", "")),
        "facts": [
            {"label": "Country", "value": tank.get("country", "")},
            {"label": "Year", "value": tank.get("year", "")},
            {"label": "Role", "value": tank.get("role", "")},
        ],
        "wiki_url": tank.get("wiki_url")
    }
