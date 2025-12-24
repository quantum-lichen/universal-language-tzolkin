#!/usr/bin/env python3
"""
Interplanetary Communication Example
Simulates Earth-Mars encrypted communication
"""

import sys
sys.path.insert(0, '../src')
from tzolkin_crypto import TzolkinCrypto
from datetime import datetime, timedelta
import time

print("=" * 60)
print("Interplanetary Communication Simulation")
print("=" * 60)
print()

# Initialize systems
earth = TzolkinCrypto()
mars = TzolkinCrypto()

# Communication date
comm_date = datetime(2025, 12, 24, 14, 30)  # 2:30 PM UTC

print(f"Communication Date: {comm_date.strftime('%Y-%m-%d %H:%M UTC')}")
print()

# Earth calculates position
earth_pos = earth.calculate_tzolkin_position(comm_date)
print(f"Earth observes Tzolk'in position: {earth_pos}")

# Mars calculates position (independently!)
mars_pos = mars.calculate_tzolkin_position(comm_date)
print(f"Mars observes Tzolk'in position: {mars_pos}")
print()

# Verify synchronization
if earth_pos == mars_pos:
    print("✓ Positions synchronized! Communication can begin.")
else:
    print("✗ Sync error! (This should never happen)")
print()

# Earth sends encrypted message
print("-" * 60)
print("EARTH → MARS")
print("-" * 60)
message_to_mars = "Rover deployment successful. All systems nominal."
print(f"Original: {message_to_mars}")

encrypted = earth.encrypt_with_date(message_to_mars, comm_date)
print(f"Encrypted: {encrypted.hex()[:64]}...")
print(f"Transmitting... (20 minute delay)")
print()

# Simulate transmission delay
time.sleep(0.5)  # Simulate in demo

# Mars receives and decrypts
print("-" * 60)
print("MARS RECEIVES")
print("-" * 60)
decrypted = mars.decrypt_with_date(encrypted, comm_date)
print(f"Decrypted: {decrypted}")
print()

if message_to_mars == decrypted:
    print("✓ Message received successfully!")
else:
    print("✗ Decryption failed!")
print()

# Mars responds
print("-" * 60)
print("MARS → EARTH")
print("-" * 60)
response = "Message received. Proceeding with mission plan."
print(f"Original: {response}")

encrypted_response = mars.encrypt_with_date(response, comm_date)
print(f"Encrypted: {encrypted_response.hex()[:64]}...")
print(f"Transmitting... (20 minute delay)")
print()

time.sleep(0.5)  # Simulate

# Earth receives
print("-" * 60)
print("EARTH RECEIVES")
print("-" * 60)
decrypted_response = earth.decrypt_with_date(encrypted_response, comm_date)
print(f"Decrypted: {decrypted_response}")
print()

if response == decrypted_response:
    print("✓ Response received successfully!")
print()
print("=" * 60)
print("Secure interplanetary communication established!")
print("No pre-shared keys required. Zero key distribution.")
print("=" * 60)
