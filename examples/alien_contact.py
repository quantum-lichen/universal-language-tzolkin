#!/usr/bin/env python3
"""
SETI Protocol Example
Demonstrates first contact protocol using perfect numbers
"""

import sys
sys.path.insert(0, '../src')
from tzolkin_crypto import TzolkinCrypto
from perfect_numbers import PERFECT_NUMBERS, MERSENNE_PRIMES, is_prime
import time

def send_beacon():
    """Phase 1: Send prime number beacon"""
    print("=" * 60)
    print("PHASE 1: BEACON")
    print("=" * 60)
    print("Transmitting prime number sequence...")
    print()
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for p in primes:
        print(f"  {p}", end=" ", flush=True)
        time.sleep(0.1)
    print()
    print()
    print("Message: 'We are intelligent. Are you there?'")
    print("Awaiting response...")
    time.sleep(0.5)
    print("✓ Response detected!")
    print()

def handshake():
    """Phase 2: Mathematical handshake"""
    print("=" * 60)
    print("PHASE 2: HANDSHAKE")
    print("=" * 60)
    print("Transmitting perfect numbers...")
    print()
    
    for perfect in PERFECT_NUMBERS[:4]:
        print(f"  {perfect}")
        time.sleep(0.1)
    print()
    print("Message: 'We know perfect numbers. Confirm yours.'")
    print("Awaiting confirmation...")
    time.sleep(0.5)
    print("✓ Aliens confirm same mathematics!")
    print()

def propose_protocol():
    """Phase 3: Propose Tzolk'in protocol"""
    print("=" * 60)
    print("PHASE 3: PROTOCOL PROPOSAL")
    print("=" * 60)
    print("Proposing 260-day cycle as encryption key...")
    print()
    
    print("  260 = 13 × 20")
    print("  Factorization: 2² × 5 × 13")
    print("  Astronomical cycle: Observable from anywhere")
    print()
    print("Message: 'Use 260-day cycle for key synchronization'")
    print("Awaiting agreement...")
    time.sleep(0.5)
    print("✓ Aliens agree to Tzolk'in protocol!")
    print()

def encrypted_communication():
    """Phase 4: Encrypted exchange"""
    print("=" * 60)
    print("PHASE 4: ENCRYPTED COMMUNICATION")
    print("=" * 60)
    print()
    
    # Both parties initialize
    earth = TzolkinCrypto()
    aliens = TzolkinCrypto()  # Using same astronomical references
    
    from datetime import datetime
    comm_date = datetime(2075, 6, 15)  # 50 years in future
    
    # First encrypted message
    message = "Greetings from Earth. We come in peace. 🌍✨"
    print(f"Earth sends: {message}")
    
    encrypted = earth.encrypt_with_date(message, comm_date)
    print(f"Encrypted: {encrypted.hex()[:64]}...")
    print()
    
    # Aliens decrypt
    decrypted = aliens.decrypt_with_date(encrypted, comm_date)
    print(f"Aliens receive: {decrypted}")
    print()
    
    # Aliens respond
    response = "Greetings Earth. Peace acknowledged. 👽🌌"
    print(f"Aliens send: {response}")
    
    encrypted_response = aliens.encrypt_with_date(response, comm_date)
    print(f"Encrypted: {encrypted_response.hex()[:64]}...")
    print()
    
    # Earth decrypts
    decrypted_response = earth.decrypt_with_date(encrypted_response, comm_date)
    print(f"Earth receives: {decrypted_response}")
    print()
    
    print("✓ Secure communication established!")
    print("✓ No pre-shared keys required!")
    print("✓ Works across light-years!")

if __name__ == "__main__":
    print()
    print("🛸" * 30)
    print("FIRST CONTACT PROTOCOL SIMULATION")
    print("🛸" * 30)
    print()
    
    send_beacon()
    time.sleep(1)
    
    handshake()
    time.sleep(1)
    
    propose_protocol()
    time.sleep(1)
    
    encrypted_communication()
    
    print()
    print("=" * 60)
    print("MISSION ACCOMPLISHED")
    print("=" * 60)
    print()
    print("First contact protocol complete.")
    print("Secure interstellar communication channel established.")
    print()
    print("The stars are no longer silent. 🌌")
    print()
