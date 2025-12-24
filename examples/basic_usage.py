"""Basic usage example for Tzolk'in Cryptography"""

import sys
sys.path.insert(0, '../src')

from tzolkin_crypto import TzolkinCrypto
from datetime import datetime

# Initialize
crypto = TzolkinCrypto()

# Example 1: Simple encryption/decryption
print("Example 1: Basic Usage")
print("-" * 40)
message = "Hello Universe!"
encrypted = crypto.encrypt_with_date(message)
decrypted = crypto.decrypt_with_date(encrypted)
print(f"Original:  {message}")
print(f"Encrypted: {encrypted.hex()[:40]}...")
print(f"Decrypted: {decrypted}")
print()

# Example 2: Specific date
print("Example 2: Using Specific Date")
print("-" * 40)
date = datetime(2025, 12, 24)
pos = crypto.calculate_tzolkin_position(date)
print(f"Date: {date.strftime('%Y-%m-%d')}")
print(f"Tzolk'in Position: Day {pos[0]}, {pos[1]}-{pos[2]}")
encrypted = crypto.encrypt_with_date("Secret message", date)
print(f"Encrypted: {encrypted.hex()}")
print()

# Example 3: Key generation
print("Example 3: Direct Key Generation")
print("-" * 40)
key = crypto.generate_key(157, 1, 17)
print(f"Key for position (157, 1, 17): {key.hex()}")
