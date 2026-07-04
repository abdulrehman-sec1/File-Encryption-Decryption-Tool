import unittest
import os
from core.encryption import FileEncryptor
from core.decryption import FileDecryptor

class TestDecryptionEngine(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_decrypt_target.txt"
        self.secret_text = "Highly confidential data package contents framework."
        with open(self.test_file, "w") as f:
            f.write(self.secret_text)
            
    def tearDown(self):
        for path in [self.test_file, self.test_file + ".enc", "test_decrypt_target_decrypted.txt"]:
            if os.path.exists(path):
                os.remove(path)

    def test_successful_decryption_loop(self):
        password = "ValidSuperSecretPass!1"
        enc_path = FileEncryptor.encrypt_file(self.test_file, password)
        dec_path = FileDecryptor.decrypt_file(enc_path, password)
        
        self.assertTrue(os.path.exists(dec_path))
        with open(dec_path, "r") as f:
            recovered = f.read()
        self.assertEqual(recovered, self.secret_text)

    def test_wrong_password_throws_exception(self):
        enc_path = FileEncryptor.encrypt_file(self.test_file, "CorrectPassword123")
        with self.assertRaises(PermissionError):
            FileDecryptor.decrypt_file(enc_path, "WrongPasswordChoice")