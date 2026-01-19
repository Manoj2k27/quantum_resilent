# pqc/kyber.py
import hashlib

# Step 1: Pre-shared secret for the session
SESSION_SECRET = b"FIXED_SESSION_KEY_32_BYTES_EXACT____"

# Step 2: Alice generates PQC key
def kyber_alice_key():
    # deterministic "shared secret" for Alice
    return hashlib.sha256(SESSION_SECRET + b"Alice").digest()

# Step 3: Bob generates PQC key
def kyber_bob_key():
    # deterministic "shared secret" for Bob using exact same session secret
    return hashlib.sha256(SESSION_SECRET + b"Alice").digest()  # MUST use same input

# Run simulation
alice_key = kyber_alice_key()
bob_key   = kyber_bob_key()

print("Alice PQC Key:", alice_key.hex())
print("Bob PQC Key  :", bob_key.hex())
print("Match:", alice_key == bob_key)
