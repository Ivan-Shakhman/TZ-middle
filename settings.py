import os
from dotenv import load_dotenv


load_dotenv()

SETTINGS = {
    "web3_url": os.getenv("WEB3_URL"),
    "proxy_type": "residential",
    "log_enabled": True,
    "max_threads": 10,
    "transaction_delay": (0, 3600),
}

MAX_THREADS = 100

MIN_THREADS = 1