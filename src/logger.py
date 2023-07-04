import os
import logging
import sys
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
log_file= os.path.join(os.getcwd(), "LOGS", LOG_FILE)

os.makedirs(log_file, exist_ok=True)
print(LOG_FILE)

LOG_FILE_PATH = os.path.join(log_file, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
    
    
)

if __name__ == "__main__":
    logging.info("first log writed !!")
    




