"""
Handles core encryption operations.
"""
import os
from typing import Callable
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import config
from core.key_manager import KeyManager
from core.logger import app_logger

class FileEncryptor:

    @staticmethod
    def encrypt_file(input_file_path: str, password: str, progress_callback: Callable[[float], None] = None) -> str:
        """
        Encrypts a target file using AES-256-GCM.
        Saves file as <original_filename>.enc and updates processing updates via callback.
        """
        app_logger.info(f"Starting encryption on file: {input_file_path}")
        
        if progress_callback: progress_callback(0.1)
        
        salt = os.urandom(config.SALT_SIZE_BYTES)
        iv = os.urandom(config.IV_SIZE_BYTES)
        
        derived_key = KeyManager.derive_key(password, salt)
        if progress_callback: progress_callback(0.4)
        
        with open(input_file_path, "rb") as f:
            plaintext = f.read()
        if progress_callback: progress_callback(0.6)
            
        aesgcm = AESGCM(derived_key)
        # Encrypt and construct standard payload authentication tag implicitly
        ciphertext = aesgcm.encrypt(iv, plaintext, None)
        if progress_callback: progress_callback(0.8)
        
        output_file_path = input_file_path + config.ENCRYPTED_FILE_EXTENSION
        
        with open(output_file_path, "wb") as f:
            f.write(salt)
            f.write(iv)
            f.write(ciphertext)
            
        if progress_callback: progress_callback(1.0)
        app_logger.info(f"Encryption successful. Encrypted payload saved to: {output_file_path}")
        return output_file_path