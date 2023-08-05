import os
import urllib.request as request
import zipfile
from ..loggerr import logger
from ..utils.common import get_size
from pathlib import Path
from ..entity.config_entity import DataIngestionConfig
import sys
from os.path import dirname, abspath

class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config
    
    def download_file(self):
        try:
            logger.info("Fetching zip file...")
            if not os.path.exists(self.config.local_data_file):
                filename, dirname = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"File Download Successfully {filename} with : {dirname}")
                
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") 
                
        except Exception as e:
            logger.exception(e)
            raise e
            
        
    def extract_zip_file(self):
        
        unzip_dir = self.config.local_data_file

        with zipfile.ZipFile(unzip_dir, "r") as unzip:
            logger.info("zipefile read successfully")
            unzip.extractall("data")
            logger.info("zipfile extracted successfully")
              
              

