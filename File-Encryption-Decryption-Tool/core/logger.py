"""
Centralized logging system for the application.
"""
import logging
from config import LOG_FILE_PATH

def setup_logger() -> logging.Logger:
    """Configures and returns a production-ready logger instance."""
    logger = logging.getLogger("GuardVault")
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        
        file_handler = logging.FileHandler(LOG_FILE_PATH, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger

app_logger = setup_logger()