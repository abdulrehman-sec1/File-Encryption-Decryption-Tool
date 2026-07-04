"""
Handles derive-key operations securely using PBKDF2.
"""
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import config

class KeyManager:

    @staticmethod
    def derive_key(password: str, salt: bytes) -> bytes:
        """Derives a strong 256-bit symmetric key from a plaintext user password."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=config.KEY_LENGTH_BYTES,
            salt=salt,
            iterations=config.PBKDF2_ITERATIONS
        )
        return kdf.derive(password.encode('utf-8'))