from src.cnnClassifier import logger
from src.cnnClassifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME  = "Data Ingestion Stage"

try: 
    logger.info(f" <<<< stage {STAGE_NAME} <<<< started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" <<<< stage {STAGE_NAME} >>>> completed !")
    
except Exception as e:
    logger.exception(e)
    raise e