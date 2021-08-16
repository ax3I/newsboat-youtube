""" Main config """
import sys
from pathlib import Path

DEFAULT_CONFIG = {
    "NEWSBOAT_URLS_FILE": str(Path.home()) + "/.newsboat/urls",
}
