import os
import logging
import sys

logging_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logs = "log"
logging_path = os.path.join(logs, "running_log.log")

os.makedirs(logging_path, exist_ok=True)

logging.basicConfig(level=logging.INFO, format=logging_format,

    handlers = [
        logging.FileHandler(logging_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("CnnClassifier")