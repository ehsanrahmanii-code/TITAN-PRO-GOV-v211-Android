"""TITAN PRO GOV — configuration. All persistent data lives ONLY under XXX/."""
from __future__ import annotations
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_NAME = "XXX"
LEGACY_DATA_NAMES = ("YYY", "WWW", "LLL", "JJJ")
DATA_DIR = Path(os.environ.get("TITAN_DATA") or (ROOT / DATA_NAME)).expanduser()
SECRET_DIR = Path(os.environ.get("TITAN_SECRET") or (DATA_DIR / "secret"))
HOST = "127.0.0.1"
PORT = int(os.environ.get("TITAN_PORT", "8080"))
VERSION = "2.1.1-NEON-STUDIO"
