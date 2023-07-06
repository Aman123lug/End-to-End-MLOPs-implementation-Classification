from ensure import ensure_annotations
import yaml
import os
from pathlib import Path
from box.exceptions import BoxValueError
import yaml
from src.logger import logging
# import logging
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
            logging.info
        return ConfigBox(yaml_content)  #d = ConfigBox({"key":"val", "key2":"val2"}) --> d.key2

    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        print(e)
        
        
# @ensure_annotations
# def 

        
        
        

        