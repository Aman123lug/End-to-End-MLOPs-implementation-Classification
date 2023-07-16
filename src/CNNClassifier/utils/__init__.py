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



@ensure_annotations
def load_yaml(yaml_file:str):
    
    try:
        with open(yaml_file, "r") as f:
            yaml_content = yaml.safe_load(f)
            # logging.info
        return ConfigBox(yaml_content)  #d = ConfigBox({"key":"val", "key2":"val2"}) --> d.key2

    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        print(e)
        
@ensure_annotations
def load_json(json_file: str):
    pass
        
        
        
@ensure_annotations
def create_directories(file_lists: list, verbose=True):
    for path in file_lists:
        
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info("Directory created !")
        
        
@ensure_annotations
def save_json(path: Path, data: dict):
  
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
  
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
 
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
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


        