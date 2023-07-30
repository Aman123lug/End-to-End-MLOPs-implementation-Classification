from src.cnnClassifier import logger
from src.cnnClassifier.config.configration import ConfigurationManager
from src.cnnClassifier.components.prepare_callbacks import PrepareCallback
from src.cnnClassifier.components.training import Training

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    
    def main(self):
        
        config = ConfigurationManager()
        prepare_callbacks = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallback(prepare_callbacks)
        callback_list = prepare_callbacks._get_tb_ckpt_callbacks()
    
        training_config = config.get_training_config()
        training = Training(configfile=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callbacks_list=callback_list
        )
        
try:
    logger.info(f"<<<< Stage {STAGE_NAME} Started >>>>")
    model = ModelTrainingPipeline()
    model.main()
    
    logger.info(f"<<<< Stage {STAGE_NAME} Completed >>>>")
    
except Exception as e:
    logger.exception(e)
    raise e

    