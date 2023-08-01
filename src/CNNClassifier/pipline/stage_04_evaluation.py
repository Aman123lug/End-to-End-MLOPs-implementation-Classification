from src.cnnClassifier.entity.config_entity import ModelEvaluationConfig
from src.cnnClassifier.config.configration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation import Evaluation
from src.cnnClassifier import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluation:
    def __init__(self) -> None:
        pass
    
    def main(self):
        
        config = ConfigurationManager()
        get_eval = config.get_validation_config()
        evaluations = Evaluation(get_eval)
        evaluations.evaluation()
        evaluations.save_score()
        
if __name__ == "__main__":

    try:
        logger.info(f"<<<< stage {STAGE_NAME} Started >>>>")
        evaluate = ModelEvaluation()
        evaluate.main()
        
        logger.info(f"<<<< Stage {STAGE_NAME} Completed >>>>")
        
    except Exception as e:
        logger.exception(e)
        raise e

        
        