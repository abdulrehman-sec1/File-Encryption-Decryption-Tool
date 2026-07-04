# 🔒 GuardVault - File Encryption & Decryption Tool

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Security Mode](https://img.shields.io/badge/Crypto-AES--256--GCM-green.svg)]()

GuardVault is a desktop file encryption utility built with Python, using modern `customtkinter` interfaces and robust `cryptography` libraries. It implements high-security industry-standard parameters to keep your files secure against local and remote threats.

---

## ✨ Features

- **Authenticated Encryption**: Uses AES-256-GCM authenticated symmetric data structures.
- **Secure Key Derivation**: Derives keys using PBKDF2HMAC (SHA256) running across 120,000+ computational tuning cycles.
- **Dynamic Live Feedback**: Password strength metrics dynamically change and update color parameters via active structural evaluations.
- **Responsive Architecture**: Multi-threaded operational execution loops keep UI frames responsive during file asset transformations.
- **Enterprise Error Controls**: Handles incorrect passphrases and modified payloads without revealing sensitive state details.

---

## 📂 Project Structure

```text
File-Encryption-Decryption-Tool/
│
├── app.py                  # Main initialization launcher entry point
├── requirements.txt         # Project runtime library dependencies
├── README.md               # Product manuals documentation
├── LICENSE                 # Legal licensing conditions map
├── .gitignore              # Repository source target tracking filter rules
├── config.py               # Global system parameter presets
│
├── assets/                 # App icon & graphic resources
│   └── screenshots/
│
├── core/                   # Underlying pure logic computations
│   ├── encryption.py
│   ├── decryption.py
│   ├── key_manager.py
│   ├── validator.py
│   ├── logger.py
│   └── utils.py
│
├── gui/                    # Presentation visualization UI layer
│   ├── main_window.py
│   ├── dialogs.py
│   ├── theme.py
│   └── widgets.py
│
├── tests/                  # Integrity test suites
│   ├── test_encrypt.py
│   ├── test_decrypt.py
│   └── test_utils.py
│
└── docs/                   # Engineering design specs
    ├── architecture.md
    ├── encryption_flow.md
    └── screenshots.md

   ```
# Installation & Setup 
Prerequisites Python 3.12 or newer installed locally.
```
```
# Execution Steps
Clone the repository resources:
```
Bash
git clone [https://github.com/abdulrehman-sec1/File-Encryption-Decryption-Tool.git]
cd File-Encryption-Decryption-Tool
```
# Configure Virtual Environment:
```
Bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```
# Install Dependencies:
```
Bash
pip install -r requirements.txt
```
# Launch the Engine Interface:
```
Bash
python app.py
```
# 🛠️ Operational Guide

File Encryption
1 Launch GuardVault and click Select Target File.
2 Type a secure passphrase into the Master Security Passphrase field.
3 Retype the same key in the Confirm Master Passphrase field.
4 Click Encrypt File. The app creates a secure .enc copy of your file in the same directory.
File Decryption
1 Select any .enc encrypted target file.
2 Input the original passphrase.
3 Click Decrypt File. The tool automatically verifies data integrity and writes the decrypted payload to disk.


# 🧪Running Automated Tests
Run the following command from the root directory to execute all unit tests:
```
Bash
python -m unittest discover -s tests
```