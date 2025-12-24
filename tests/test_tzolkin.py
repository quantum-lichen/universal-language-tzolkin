"""
Unit tests for Tzolk'in Cryptography System
"""

import pytest
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '../src')
from tzolkin_crypto import TzolkinCrypto


class TestTzolkinPosition:
    def test_position_calculation(self):
        """Test Tzolk'in position calculation"""
        crypto = TzolkinCrypto()
        pos = crypto.calculate_tzolkin_position(datetime(2025, 1, 1))
        
        # Position should be tuple of 3 integers
        assert isinstance(pos, tuple)
        assert len(pos) == 3
        
        # Check ranges
        day_number, trecena, veintena = pos
        assert 1 <= day_number <= 260
        assert 1 <= trecena <= 13
        assert 1 <= veintena <= 20
    
    def test_cycle_completion(self):
        """Test that position cycles every 260 days"""
        crypto = TzolkinCrypto()
        date1 = datetime(2025, 1, 1)
        date2 = date1 + timedelta(days=260)
        
        pos1 = crypto.calculate_tzolkin_position(date1)
        pos2 = crypto.calculate_tzolkin_position(date2)
        
        # After 260 days, should return to same position
        assert pos1[1] == pos2[1]  # trecena
        assert pos1[2] == pos2[2]  # veintena


class TestKeyGeneration:
    def test_key_generation(self):
        """Test cryptographic key generation"""
        crypto = TzolkinCrypto()
        key = crypto.generate_key(157, 1, 17)
        
        # Key should be 32 bytes by default
        assert len(key) == 32
        assert isinstance(key, bytes)
    
    def test_key_uniqueness(self):
        """Test that different positions generate different keys"""
        crypto = TzolkinCrypto()
        key1 = crypto.generate_key(1, 1, 1)
        key2 = crypto.generate_key(2, 2, 2)
        
        assert key1 != key2
    
    def test_all_260_keys_unique(self):
        """Test that all 260 days have unique keys"""
        crypto = TzolkinCrypto()
        keys = set()
        
        for day in range(1, 261):
            pos = crypto.calculate_tzolkin_position(
                crypto.epoch + timedelta(days=day)
            )
            key = crypto.generate_key(*pos)
            keys.add(key)
        
        # All 260 keys should be unique
        assert len(keys) == 260


class TestEncryption:
    def test_basic_encryption(self):
        """Test basic encrypt/decrypt cycle"""
        crypto = TzolkinCrypto()
        message = "Hello Universe!"
        
        encrypted = crypto.encrypt_with_date(message)
        decrypted = crypto.decrypt_with_date(encrypted)
        
        assert message == decrypted
    
    def test_long_message(self):
        """Test encryption of long messages"""
        crypto = TzolkinCrypto()
        message = "A" * 10000  # 10KB message
        
        encrypted = crypto.encrypt_with_date(message)
        decrypted = crypto.decrypt_with_date(encrypted)
        
        assert message == decrypted
    
    def test_unicode_message(self):
        """Test encryption of Unicode text"""
        crypto = TzolkinCrypto()
        message = "Héllö Wörld! 你好世界 🌍"
        
        encrypted = crypto.encrypt_with_date(message)
        decrypted = crypto.decrypt_with_date(encrypted)
        
        assert message == decrypted
    
    def test_wrong_date_fails(self):
        """Test that wrong date produces gibberish"""
        crypto = TzolkinCrypto()
        message = "Secret message"
        date1 = datetime(2025, 1, 1)
        date2 = datetime(2025, 1, 2)
        
        encrypted = crypto.encrypt_with_date(message, date1)
        
        # Decrypting with wrong date should fail
        with pytest.raises(UnicodeDecodeError):
            decrypted = crypto.decrypt_with_date(encrypted, date2)


class TestSynchronization:
    def test_independent_instances_sync(self):
        """Test that two independent instances generate same keys"""
        crypto1 = TzolkinCrypto()
        crypto2 = TzolkinCrypto()
        
        date = datetime(2025, 12, 24)
        
        key1 = crypto1.get_key_for_date(date)
        key2 = crypto2.get_key_for_date(date)
        
        assert key1 == key2
    
    def test_earth_mars_scenario(self):
        """Test Earth-Mars communication scenario"""
        earth = TzolkinCrypto()
        mars = TzolkinCrypto()
        
        date = datetime(2025, 12, 24)
        message = "Launch sequence initiated"
        
        # Earth encrypts
        encrypted = earth.encrypt_with_date(message, date)
        
        # Mars decrypts (20 min later, same date)
        decrypted = mars.decrypt_with_date(encrypted, date)
        
        assert message == decrypted


class TestPerformance:
    def test_encryption_speed(self):
        """Test encryption performance"""
        import time
        crypto = TzolkinCrypto()
        message = "X" * 1000  # 1KB message
        
        start = time.time()
        for _ in range(100):
            crypto.encrypt_with_date(message)
        end = time.time()
        
        avg_time = (end - start) / 100
        # Should be under 1ms per operation
        assert avg_time < 0.001


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
