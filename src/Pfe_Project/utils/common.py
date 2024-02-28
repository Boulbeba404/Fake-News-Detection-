import os
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
from box import BoxError, ConfigBox
from pathlib import Path
from typing import Any
from src.log_config import get_logger
import pandas as pd 



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
 
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger=get_logger()
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def save_yaml(data: ConfigBox, path_to_yaml: Path) -> None:
    
    try:
        with open(path_to_yaml) as yaml_file:
            yaml.dump(data.to_dict(), yaml_file)
        logger = get_logger()
        logger.info(f"YAML file: {path_to_yaml} saved successfully")
    except BoxError as e:
        logger.error(f"Failed to save YAML file: {path_to_yaml}, error: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred while saving YAML file: {path_to_yaml}, error: {e}")
        raise e

    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
   
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger=get_logger()
            logger.info(f"created directory at: {path}")

@ensure_annotations
def load_data(file_path: str, file_type: str = 'csv') -> pd.DataFrame:
    
    if file_type == 'csv':
        return pd.read_csv(file_path)

@ensure_annotations
def save_data(df: pd.DataFrame, file_path: str, file_type: str = 'csv') -> None:
    
    if file_type == 'csv':
        df.to_csv(file_path, index=False)



    