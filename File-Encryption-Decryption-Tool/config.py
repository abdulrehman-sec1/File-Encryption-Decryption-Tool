"""
Configuration settings for the File Encryption & Decryption Tool.
"""
import os

# Cryptographic Constants
SALT_SIZE_BYTES: int = 16
IV_SIZE_BYTES: int = 12  # 12 bytes standard for AES-GCM
TAG_SIZE_BYTES: int = 16
PBKDF2_ITERATIONS: int = 120_000
KEY_LENGTH_BYTES: int = 32  # 256 bits

# File Extensions
ENCRYPTED_FILE_EXTENSION: str = ".enc"

# UI Configurations
WINDOW_TITLE: str = "GuardVault - File Encryption Tool"
WINDOW_WIDTH: int = 600
WINDOW_HEIGHT: int = 550
THEME_MODE: str = "dark"
COLOR_THEME: str = "blue"

# Logging Config
LOG_FILE_PATH: str = os.path.join(os.path.dirname(__file__), "logs.log")