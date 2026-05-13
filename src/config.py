from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = BASE_DIR/ "data" / "input.txt"
LOG_FILE = BASE_DIR/ "logs" / "log.txt"

API_URL = "https://httpbin.org/post"
TIMEOUT = 5

RETRY_TIMES = 3