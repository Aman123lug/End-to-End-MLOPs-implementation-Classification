
from ..entity.config_entity import PrepareBaseModelConfig
import tensorflow as tf
from pathlib import Path      
            
class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig) -> None:
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            include_top=self.config.params_include_top,
            weights=self.config.params_weight,
            input_shape=self.config.params_image_size,
            classes=self.config.params_classes,
            
        )
        
        self.save_model(path=self.config.base_model_path, model=self.model)
          
    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainlable = False
                
        elif (freeze_till is not None) and (freeze_till > 0):
            for layers in model.layers[:-freeze_till]:
                model.trainable = False
                
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)
            
            
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )
        
        full_model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                           loss=tf.keras.losses.CategoricalCrossentropy(),
                           metrics=["accuracy"]
                           
                           )
        full_model.summary()
        
        return full_model
        
        
    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        
        self.save_model(path=self.config.updated_base_model, model=self.full_model)
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
            