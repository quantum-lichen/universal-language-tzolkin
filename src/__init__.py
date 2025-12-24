"""
Universal Language & Tzolk'in Cryptography
==========================================

A mathematical framework for interstellar communication and 
quantum-resistant encryption.

Main components:
- TzolkinCrypto: Cryptographic system
- Perfect number utilities
- Astronomical calculations
- Universal language encoding

Example:
    >>> from tzolkin_crypto import TzolkinCrypto
    >>> crypto = TzolkinCrypto()
    >>> encrypted = crypto.encrypt_with_date("Hello Universe!")
    >>> decrypted = crypto.decrypt_with_date(encrypted)
"""

__version__ = "1.0.0"
__author__ = "Bryan Ouellette, Claude AI"
__license__ = "Apache 2.0"

from .tzolkin_crypto import (
    TzolkinCrypto,
    quick_encrypt,
    quick_decrypt,
    PHI,
    PI,
    E,
    TZOLKIN_CYCLE,
    TRECENA,
    VEINTENA
)

__all__ = [
    'TzolkinCrypto',
    'quick_encrypt',
    'quick_decrypt',
    'PHI',
    'PI',
    'E',
    'TZOLKIN_CYCLE',
    'TRECENA',
    'VEINTENA'
]
