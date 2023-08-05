from ..config.configration import ConfigurationManager
from ..components.prepare_base_model import PrepareBaseModel
from ..loggerr import logger

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
            config = ConfigurationManager()
            get_base_model_config = config.get_base_model_config()
            prepare_model = PrepareBaseModel(get_base_model_config)
            prepare_model.get_base_model()
            prepare_model.update_base_model()
               
    
if __name__ == "__main__":
    try:
        logger.info(f" >>>> Started {STAGE_NAME} Stage<<<<")
        obj2 = PrepareBaseModelTrainingPipeline()
        obj2.main()
        logger.info(f" >>>> stage {STAGE_NAME} <<<< Completed ! \n\n x==================x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    

        