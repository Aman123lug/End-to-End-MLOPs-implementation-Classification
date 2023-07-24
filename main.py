from src.cnnClassifier import logger
from src.cnnClassifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
STAGE_NAME  = "Prepare base model"

# try: 
#     logger.info(f" <<<< stage {STAGE_NAME} <<<< started")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f" <<<< stage {STAGE_NAME} >>>> completed !")
    
# except Exception as e:
#     logger.exception(e)
#     raise e

try: 
    logger.info(f" <<<< stage {STAGE_NAME} <<<< started")
    base_model = PrepareBaseModelTrainingPipeline()
    base_model.main()
    logger.info(f" <<<< stage {STAGE_NAME} >>>> completed !")
    
except Exception as e:
    logger.exception(e)
    raise e