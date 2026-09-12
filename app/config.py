# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests.
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = Path(os.getenv("ARP_DB_PATH", str(DATA_DIR / "netshield.db")))
APP_NAME = "NetShield ARP Guardian"
VERSION = "2.0.0"
DEFAULT_GATEWAY = os.getenv("ARP_GATEWAY_IP", "192.168.1.1")
RISK_THRESHOLD = int(os.getenv("ARP_RISK_THRESHOLD", "35"))
BASELINE_WINDOW = int(os.getenv("ARP_BASELINE_WINDOW", "300"))
MAX_EVENTS_PER_QUERY = 500
