from ensure import ensure_annotations
import yaml
import os
from pathlib import Path
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from box import ConfigBox
from typing import Any
import base64
from src.cnnClassifier.loggerr import logger



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
        
@ensure_annotations
def load_json(json_file: str) -> ConfigBox:
    """ load json file data
    
    Args:
        path of json file
        
    Return:
        ConfigBox 
    """
    with open(json_file) as f:
        content = json.load(f)
        
    logger.info("json file loaded !")
    return ConfigBox(content)
        
        
@ensure_annotations
def create_directories(file_lists: list, verbose=True):
    for path in file_lists:
        
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created ! {path}")
        
        
@ensure_annotations
def save_json(path: Path, data: dict):
  
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
  
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
 
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
   
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())


        