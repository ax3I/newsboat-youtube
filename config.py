""" Main config """
import sys
from pathlib import Path

DEFAULT_CONFIG = {
    "CHANNEL_URL":  sys.argv[1],
    "NEWSBOAT_URLS_FILE": str(Path.home()) + "/.newsboat/urls",
}
