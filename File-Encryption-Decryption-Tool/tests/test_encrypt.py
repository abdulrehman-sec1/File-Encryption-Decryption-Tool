import unittest
import os
from core.encryption import FileEncryptor
from core.key_manager import KeyManager

class TestEncryptionEngine(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_target_payload.txt"
        with open(self.test_file, "w") as f:
            f.write("System testing payload data strings for core integration validation.")
            
    def tearDown(self):
        for path in [self.test_file, self.test_file + ".enc"]:
            if os.path.exists(path):
                os.remove(path)

    def test_encryption_output_generation(self):
        out_path = FileEncryptor.encrypt_file(self.test_file, "SecurePassphrase123!")
        self.assertTrue(os.path.exists(out_path))
        self.assertTrue(out_path.endswith(".enc"))