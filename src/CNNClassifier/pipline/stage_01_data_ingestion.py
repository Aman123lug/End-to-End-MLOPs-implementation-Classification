from ..config.configration import ConfigurationManager
from ..components.data_ingestion import DataIngestion
from ..loggerr import logger

STAGE_NAME  = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):

        config = ConfigurationManager()
        get_config_data = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(get_config_data)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
if __name__ == "__main__":
    
    try:
        logger.info(f" >>>> stage {STAGE_NAME} <<<< started !")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f" >>>> stage {STAGE_NAME} <<<< Completed ! \n\n x==================x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    