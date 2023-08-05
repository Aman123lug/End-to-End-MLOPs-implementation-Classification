from ..constant import *
from ..utils.common import load_bin, read_yaml, create_directories
from ..entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig, ModelEvaluationConfig 
import os

class ConfigurationManager:
    def __init__(self, configfile_path = CONFIG_FILE_PATH, paramsfile_path = PARAMS_FILE_PATH) -> None:
        
        self.config  = read_yaml(configfile_path)
        self.params = read_yaml(paramsfile_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
    
    
        data_ingestion_config = DataIngestionConfig(
            
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
            
        )
        return data_ingestion_config
    
    
    def get_base_model_config(self) -> PrepareBaseModelConfig:
        
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_config,
            updated_base_model=config.updated_base_model_config,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weight=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
            
        )
        
        return prepare_base_model_config
    
    
    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        
        config = self.config.prepare_callbacks
        
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])
        
        prepare_callbacks_config = PrepareCallbacksConfig(
            
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
            
        )
        
        return prepare_callbacks_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.root_dir, "Chicken-fecal-images")
        
        create_directories([
            Path(training.root_dir) #data
        ])
        
        training_config = TrainingConfig(
            
            root_dir=Path(training.root_dir), #data
            train_model_path=Path(training.train_model_path), # artifacts/training/model.h5
            updated_model_base_path=Path(prepare_base_model.updated_base_model_config), 
            training_data=Path(training_data),
            params_epochs=params.EPOCH,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            param_image_size=params.IMAGE_SIZE,
            
        )
        
        return training_config
    
    
    def get_validation_config(self) -> ModelEvaluationConfig:
        
        model_eval = ModelEvaluationConfig(
            path_of_model = "artifacts/training/model.h5",
            training_data = "data/Chicken-fecal-images",
            all_params = self.params,
            params_image_size = self.params.IMAGE_SIZE,
            params_batch_size = self.params.BATCH_SIZE
        )
        
        return model_eval
    