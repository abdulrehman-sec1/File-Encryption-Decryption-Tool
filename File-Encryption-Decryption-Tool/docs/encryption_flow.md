# Cryptographic Framework Layout Specification

### File Structural Layout Format
When GuardVault outputs an encrypted asset (`.enc`), it maps binary parameters sequentially using this structured frame layout layout:

+----------------------+--------------------+----------------------------------+
| Salt Header Offset   | IV Initialization  | Ciphertext Payload Container     |
| (16 Bytes)           | (12 Bytes)         | (Arbitrary Variable Length)      |
+----------------------+--------------------+----------------------------------+

### Cryptographic Lifecycle Flow
1. Generates 16 random unique salt bytes via OS entropy (`os.urandom`).
2. Generates a 12-byte initialization vector (`IV`) for AES-GCM.
3. Derives a 256-bit symmetric key through PBKDF2HMAC using SHA256 processing over 120,000 algorithmic cycles.
4. Encrypts the payload, returning the processed cipher details alongside an integrated internal GCM validation tag.