import tensorflow as tf
from ..entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from ..utils.common import save_json


model = tf.keras.models.load_model("artifacts/training/model.h5")

class Evaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config
        
        
    def _train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )
        
        dataflow_kwargs = dict(
            
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
    
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs,
        )
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._train_valid_generator()
        self.score = model.evaluate(self.valid_generator)
        
    def save_score(self):
        score = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("score.json"), data=score)
        
            
    