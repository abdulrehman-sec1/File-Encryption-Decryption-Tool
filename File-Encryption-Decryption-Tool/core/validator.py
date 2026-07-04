"""
Validates files and credentials before running operations.
"""
import os
import re
from typing import Tuple, Optional
from core.logger import app_logger

class Validator:
    
    @staticmethod
    def validate_file_for_encryption(file_path: str) -> Tuple[bool, Optional[str]]:
        """Validates if a file exists, is readable, and is ready for encryption."""
        if not file_path or not os.path.exists(file_path):
            app_logger.warning(f"Validation failed: File does not exist: '{file_path}'")
            return False, "Selected file does not exist."
            
        if not os.path.isfile(file_path):
            app_logger.warning(f"Validation failed: Path is not a file: '{file_path}'")
            return False, "Selected path is not a valid file."
            
        if os.path.getsize(file_path) == 0:
            app_logger.warning(f"Validation failed: File is empty: '{file_path}'")
            return False, "Selected file is completely empty."
            
        if not os.access(file_path, os.R_OK):
            app_logger.warning(f"Validation failed: Missing read permissions: '{file_path}'")
            return False, "Permission denied. Cannot read the input file."
            
        return True, None

    @staticmethod
    def validate_file_for_decryption(file_path: str, system_extension: str) -> Tuple[bool, Optional[str]]:
        """Validates if a file is safe and correctly formatted for decryption."""
        success, error = Validator.validate_file_for_encryption(file_path)
        if not success:
            return False, error
            
        if not file_path.endswith(system_extension):
            app_logger.warning(f"Validation warning: External extension parsed: '{file_path}'")
            
        return True, None

    @staticmethod
    def check_password_strength(password: str) -> Tuple[int, str]:
        """
        Evaluates password strength.
        Returns a tuple: (score out of 4, description string).
        """
        if len(password) < 8:
            return 0, "Too Short (Min 8 chars required)"
            
        score = 0
        if re.search(r"[A-Z]", password): score += 1
        if re.search(r"[a-z]", password): score += 1
        if re.search(r"[0-9]", password): score += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
        
        if score <= 1:
            return 1, "Weak"
        elif score == 2:
            return 2, "Fair"
        elif score == 3:
            return 3, "Good"
        return 4, "Strong / Secure"