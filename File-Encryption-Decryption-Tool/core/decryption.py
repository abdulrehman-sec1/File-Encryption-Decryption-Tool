"""
Handles core decryption operations.
"""
import os
from typing import Callable
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
import config
from core.key_manager import KeyManager
from core.logger import app_logger

class FileDecryptor:

    @staticmethod
    def decrypt_file(input_file_path: str, password: str, progress_callback: Callable[[float], None] = None) -> str:
        """
        Decrypts an AES-256-GCM encrypted payload file.
        Detects tampering or invalid passwords securely via GCM authentication verification.
        """
        app_logger.info(f"Starting decryption execution layout on: {input_file_path}")
        if progress_callback: progress_callback(0.1)
        
        file_size = os.path.getsize(input_file_path)
        header_offset = config.SALT_SIZE_BYTES + config.IV_SIZE_BYTES
        
        if file_size < header_offset + config.TAG_SIZE_BYTES:
            app_logger.error("Decryption failed: Target payload is corrupted or structurally invalid.")
            raise ValueError("The selected file framework is structurally invalid or corrupted.")
            
        with open(input_file_path, "rb") as f:
            salt = f.read(config.SALT_SIZE_BYTES)
            iv = f.read(config.IV_SIZE_BYTES)
            ciphertext = f.read()
            
        if progress_callback: progress_callback(0.4)
        derived_key = KeyManager.derive_key(password, salt)
        
        if progress_callback: progress_callback(0.6)
        aesgcm = AESGCM(derived_key)
        
        try:
            plaintext = aesgcm.decrypt(iv, ciphertext, None)
        except InvalidTag:
            app_logger.error("Authentication check failed: Wrong password choice or corrupted payload data.")
            raise PermissionError("Incorrect password choice or corrupted target structure data.")
            
        if progress_callback: progress_callback(0.8)
        
        if input_file_path.endswith(config.ENCRYPTED_FILE_EXTENSION):
            output_file_path = input_file_path[:-len(config.ENCRYPTED_FILE_EXTENSION)]
            if os.path.exists(output_file_path):
                name, ext = os.path.splitext(output_file_path)
                output_file_path = f"{name}_decrypted{ext}"
        else:
            output_file_path = input_file_path + ".decrypted"
            
        with open(output_file_path, "wb") as f:
            f.write(plaintext)
            
        if progress_callback: progress_callback(1.0)
        app_logger.info(f"Decryption execution successfully written to path: {output_file_path}")
        return output_file_path