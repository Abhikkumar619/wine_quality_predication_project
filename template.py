import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="ml_project"

list_of_file=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    "config/config.yaml", 
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_file:
    filepath=Path(filepath)

    file_dir, filename=os.path.split(filepath)

    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Crating directory: {file_dir} for the file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath, "w") as f:
                pass 
            logging.info(f"Creating empty file : {filepath}")


        else: 
            logging.info(f"{filename} is already exists")