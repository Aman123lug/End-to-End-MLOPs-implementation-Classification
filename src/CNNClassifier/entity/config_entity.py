from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    

@dataclass
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weight: str
    params_classes: int
    
    


@dataclass
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path
    
    
    
    
@dataclass
class TrainingConfig:
   
   root_dir: Path
   train_model_path: Path
   updated_model_base_path: Path
   training_data: Path
   params_epochs: int
   params_batch_size: int
   params_is_augmentation: bool
   param_image_size: list   



@dataclass(frozen=True)
class ModelEvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int
    