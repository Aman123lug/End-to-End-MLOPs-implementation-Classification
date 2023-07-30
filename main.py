from src.cnnClassifier import logger
from src.cnnClassifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipline.stage_03_training import ModelTrainingPipeline


STAGE_NAME  = "Data Ingestion"
try: 
    logger.info(f" <<<< stage {STAGE_NAME} <<<< started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" <<<< stage {STAGE_NAME} >>>> completed !")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME  = "Prepare Base Model"
try: 
    logger.info(f" <<<< stage {STAGE_NAME} <<<< started")
    base_model = PrepareBaseModelTrainingPipeline()
    base_model.main()
    logger.info(f" <<<< stage {STAGE_NAME} >>>> completed !")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME  = "Training"
try:
    logger.info(f"<<<< stage {STAGE_NAME} started >>>>")
    train = ModelTrainingPipeline()
    train.main()
    logger.info(f"<<<< stage {STAGE_NAME} completed >>>>")
    
except Exception as e:
    logger.exception(e)
    raise e
