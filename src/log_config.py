import os
import sys
import logging
from logging.handlers import RotatingFileHandler

def get_logger(logger_name="Pfe_ProjectLogger"):
    logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
    log_dir = "logs"
    log_filepath = os.path.join(log_dir, "running_logs.log")
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)  

    
    file_handler = RotatingFileHandler(log_filepath, maxBytes=1024*1024*5) 
    console_handler = logging.StreamHandler(sys.stdout)

    
    formatter = logging.Formatter(logging_str)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
