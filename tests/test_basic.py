"""Basic tests for Tzolk'in Cryptography"""

import sys
sys.path.insert(0, '../src')

from tzolkin_crypto import TzolkinCrypto
from datetime import datetime, timedelta

def test_position_calculation():
    """Test Tzolk'in position calculation"""
    crypto = TzolkinCrypto()
    pos = crypto.calculate_tzolkin_position(datetime(2025, 1, 1))
    assert 1 <= pos[0] <= 260
    assert 1 <= pos[1] <= 13
    assert 1 <= pos[2] <= 20

def test_encryption_decryption():
    """Test basic encryption/decryption"""
    crypto = TzolkinCrypto()
    message = "Test message"
    date = datetime(2025, 12, 24)
    encrypted = crypto.encrypt_with_date(message, date)
    decrypted = crypto.decrypt_with_date(encrypted, date)
    assert message == decrypted

def test_key_uniqueness():
    """Test that different days generate different keys"""
    crypto = TzolkinCrypto()
    key1 = crypto.generate_key(1, 1, 1)
    key2 = crypto.generate_key(2, 2, 2)
    assert key1 != key2

if __name__ == "__main__":
    test_position_calculation()
    test_encryption_decryption()
    test_key_uniqueness()
    print("✓ All tests passed!")
