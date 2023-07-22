
from src.cnnClassifier.constant import *
from src.cnnClassifier.utils.common import load_bin, read_yaml, create_directories
from src.cnnClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, configfile_path = CONFIG_FILE_PATH, paramsfile_path = PARAMS_FILE_PATH) -> None:
        
        self.config  = read_yaml(configfile_path)
        self.params = read_yaml(paramsfile_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
    
    
        data_ingestion_config = DataIngestionConfig(
            
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
            
        )
        return data_ingestion_config