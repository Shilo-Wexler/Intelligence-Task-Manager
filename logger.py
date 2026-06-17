import logging 
import os 
from logging import Logger 


OUTPUT_FILE = "logs/app.log" 
 

def get_logger(name: str, log_file: str = OUTPUT_FILE) -> Logger: 
    logger = logging.getLogger(name) 
 
    if logger.handlers: 
        return logger 
     
    logger.setLevel(logging.DEBUG) 
     
    log_dir = os.path.dirname(log_file) 
    if log_dir: 
        os.makedirs(log_dir, exist_ok=True) 
     
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S') 
     
    file_handler = logging.FileHandler(filename=log_file, encoding='utf-8') 
    stream_handler = logging.StreamHandler() 
     
    file_handler.setFormatter(formatter) 
    stream_handler.setFormatter(formatter) 
 
    logger.addHandler(file_handler) 
    logger.addHandler(stream_handler) 
 
    return logger



