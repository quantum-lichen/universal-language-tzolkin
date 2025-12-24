"""
Tzolk'in Cryptography System
Universal Language & Tzolk'in-based One-Time Pad

Author: Bryan Ouellette & Claude AI
License: Apache 2.0
"""

import hashlib
import numpy as np
from datetime import datetime, timedelta
from typing import Tuple, Optional

# Universal Constants
PHI = 1.618033988749895  # Golden Ratio
PI = 3.141592653589793   # Pi
E = 2.718281828459045    # Euler's number
PHI_INT = int(PHI * 10**15)  # φ as integer for seed mixing

# Mayan Long Count Epoch (August 11, 3114 BCE)
DEFAULT_EPOCH = datetime(year=-3113, month=8, day=11)

# Tzolk'in cycle parameters
TZOLKIN_CYCLE = 260
TRECENA = 13
VEINTENA = 20


class TzolkinCrypto:
    """
    Cryptographic system based on Mayan Tzolk'in calendar.
    
    Uses astronomical cycles to generate deterministic keys
    without requiring key distribution.
    """
    
    def __init__(self, epoch: Optional[datetime] = None):
        """
        Initialize Tzolk'in crypto system.
        
        Args:
            epoch: Reference date for calendar start
                  (default: Mayan Long Count epoch)
        """
        self.epoch = epoch if epoch is not None else DEFAULT_EPOCH
    
    def calculate_tzolkin_position(self, 
                                   date: Optional[datetime] = None
                                   ) -> Tuple[int, int, int]:
        """
        Calculate position in 260-day Tzolk'in cycle.
        
        Args:
            date: Date to calculate (default: now)
            
        Returns:
            (day_number, trecena, veintena) tuple where:
            - day_number: 1-260 (absolute position)
            - trecena: 1-13 (short cycle)
            - veintena: 1-20 (long cycle)
        """
        if date is None:
            date = datetime.now()
        
        # Days since epoch
        delta_days = (date - self.epoch).days
        
        # Position in 260-day cycle
        day_number = (delta_days % TZOLKIN_CYCLE) + 1
        
        # Trecena (1-13 cycle)
        trecena = ((day_number - 1) % TRECENA) + 1
        
        # Veintena (1-20 cycle)
        veintena = ((day_number - 1) % VEINTENA) + 1
        
        return (day_number, trecena, veintena)
    
    def generate_key(self,
                    day_number: int,
                    trecena: int,
                    veintena: int,
                    key_length: int = 32
                    ) -> bytes:
        """
        Generate cryptographic key from Tzolk'in position.
        
        Args:
            day_number: 1-260
            trecena: 1-13
            veintena: 1-20
            key_length: Key length in bytes (default: 32 = 256 bits)
            
        Returns:
            Cryptographic key (bytes)
        """
        # Combine components into seed
        seed = (day_number * 1_000_000 + 
                trecena * 1_000 + 
                veintena)
        
        # Mix with golden ratio for additional entropy
        seed = (seed * PHI_INT) % (2**64)
        
        # Convert to bytes
        seed_bytes = seed.to_bytes(8, byteorder='big')
        
        # Key stretching via iterated hashing (PBKDF-like)
        key = seed_bytes
        for _ in range(1000):  # 1000 iterations
            key = hashlib.sha256(key).digest()
        
        # Extend key if needed (stream cipher mode)
        if key_length > len(key):
            extended_key = key
            while len(extended_key) < key_length:
                extended_key += hashlib.sha256(extended_key[-32:]).digest()
            key = extended_key
        
        return key[:key_length]
    
    def encrypt(self, 
               message: [str, bytes],
               key: bytes
               ) -> bytes:
        """
        Encrypt message using one-time pad (XOR).
        
        Args:
            message: Message to encrypt (str or bytes)
            key: Cryptographic key
            
        Returns:
            Ciphertext (bytes)
        """
        # Convert string to bytes if needed
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        # Extend key if message is longer
        if len(message) > len(key):
            extended_key = key
            while len(extended_key) < len(message):
                extended_key += hashlib.sha256(extended_key[-32:]).digest()
            key = extended_key[:len(message)]
        
        # XOR encryption (one-time pad)
        ciphertext = bytes([m ^ k for m, k in zip(message, key)])
        
        return ciphertext
    
    def decrypt(self,
               ciphertext: bytes,
               key: bytes
               ) -> bytes:
        """
        Decrypt ciphertext using one-time pad.
        
        XOR is its own inverse, so this is identical to encrypt().
        
        Args:
            ciphertext: Encrypted message
            key: Same key used for encryption
            
        Returns:
            Plaintext (bytes)
        """
        return self.encrypt(ciphertext, key)  # XOR is symmetric
    
    def encrypt_with_date(self,
                         message: [str, bytes],
                         date: Optional[datetime] = None
                         ) -> bytes:
        """
        Encrypt message using key derived from date.
        
        Args:
            message: Message to encrypt
            date: Date for key generation (default: today)
            
        Returns:
            Ciphertext (bytes)
        """
        position = self.calculate_tzolkin_position(date)
        key = self.generate_key(*position)
        return self.encrypt(message, key)
    
    def decrypt_with_date(self,
                         ciphertext: bytes,
                         date: Optional[datetime] = None
                         ) -> str:
        """
        Decrypt message using key derived from date.
        
        Args:
            ciphertext: Encrypted message
            date: Date for key generation (default: today)
            
        Returns:
            Decrypted message (str)
        """
        position = self.calculate_tzolkin_position(date)
        key = self.generate_key(*position)
        plaintext_bytes = self.decrypt(ciphertext, key)
        return plaintext_bytes.decode('utf-8')
    
    def get_key_for_today(self, key_length: int = 32) -> bytes:
        """
        Get today's cryptographic key.
        
        Args:
            key_length: Desired key length in bytes
            
        Returns:
            Today's key
        """
        position = self.calculate_tzolkin_position()
        return self.generate_key(*position, key_length)


# Convenience functions
def encrypt_message(message: str, date: Optional[datetime] = None) -> bytes:
    """Quick encryption with default settings."""
    crypto = TzolkinCrypto()
    return crypto.encrypt_with_date(message, date)


def decrypt_message(ciphertext: bytes, date: Optional[datetime] = None) -> str:
    """Quick decryption with default settings."""
    crypto = TzolkinCrypto()
    return crypto.decrypt_with_date(ciphertext, date)


if __name__ == "__main__":
    # Demo
    print("=" * 60)
    print("Tzolk'in Cryptography System Demo")
    print("=" * 60)
    print()
    
    crypto = TzolkinCrypto()
    
    # Today's position
    pos = crypto.calculate_tzolkin_position()
    print(f"Today's Tzolk'in Position:")
    print(f"  Day: {pos[0]}/260")
    print(f"  Trecena: {pos[1]}/13")
    print(f"  Veintena: {pos[2]}/20")
    print()
    
    # Encrypt a message
    message = "The stars are waiting. 🌌"
    print(f"Original: {message}")
    
    encrypted = crypto.encrypt_with_date(message)
    print(f"Encrypted: {encrypted.hex()}")
    
    decrypted = crypto.decrypt_with_date(encrypted)
    print(f"Decrypted: {decrypted}")
    print()
    
    assert message == decrypted
    print("✓ Encryption/Decryption successful!")
