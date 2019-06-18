import sys

import logging
# To output apache logs
logging.basicConfig(stream = sys.stderr)

sys.path.insert(0, '/var/html/LLMusicCloud')

from app import application as application