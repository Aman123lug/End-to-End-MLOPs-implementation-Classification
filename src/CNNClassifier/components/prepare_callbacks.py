import time
import tensorflow as tf
from ..loggerr import logger
from ..entity.config_entity import PrepareCallbacksConfig
import os



class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig) -> None:
        self.config = config
    
    @property
    def _create_tb_callbacks(self):
        timeStamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_log_at_{timeStamp}",
            
        ) 
        
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def _create_ckpt_callbacks(self):
        
        return tf.keras.callbacks.ModelCheckpoint(
            self.config.checkpoint_model_filepath,
            save_best_only=True
        )
        
        
    def _get_tb_ckpt_callbacks(self):
        
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
        
    