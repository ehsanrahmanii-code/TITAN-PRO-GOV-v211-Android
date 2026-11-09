"""Settings loader for TITAN PRO GOV."""
from __future__ import annotations
from pathlib import Path
import json
from app.config import DATA_DIR

def load_settings():
    p = DATA_DIR / "settings.json"
    if p.is_file():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

def save_settings(data: dict):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "settings.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
