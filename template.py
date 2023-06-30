import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "CNN-Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
    "test.py",
    "templates/index.html"
    
]

for file in list_of_files:
    filepath = Path(file)  #src\CNN-Classifier\utils
    dirname, filename = os.path.split(filepath)
    

    if dirname != "":
        os.makedirs(dirname, exist_ok=True)
        logging.info(f"Directory Created ! {dirname} -- for file = {filename}")
        
    if (not os.path.exists(filename)) or (os.path.getsize(filepath))==0:
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already created !!")
        
        

    
    
    
    

    
    
    
        