import time
from qkd.bb84 import run_bb84
from pqc.kyber import kyber_alice_key
from hybrid.hybrid_key import generate_hybrid_key
from classical.aes_crypto import aes_encrypt, aes_decrypt

# Example plaintext
plaintext = b"Hello Quantum-Resilient World!" * 1000  # make it bigger for measurement

print("=== Performance Evaluation ===")

# 1. BB84 Key Generation
start = time.time()
qkd_key, _, _, _ = run_bb84()
qkd_time = time.time() - start
print(f"BB84 Key Generation Time: {qkd_time*1000:.2f} ms")

# 2. PQC Key Generation
start = time.time()
pqc_key = kyber_alice_key()
pqc_time = time.time() - start
print(f"PQC Key Generation Time: {pqc_time*1000:.2f} ms")

# 3. Hybrid Key Generation
start = time.time()
hybrid_key = generate_hybrid_key()
hybrid_time = time.time() - start
print(f"Hybrid Key Generation Time: {hybrid_time*1000:.2f} ms")

# 4. AES Encryption
start = time.time()
ciphertext = aes_encrypt(plaintext, hybrid_key)
aes_enc_time = time.time() - start
print(f"AES Encryption Time: {aes_enc_time*1000:.2f} ms")

# 5. AES Decryption
start = time.time()
decrypted = aes_decrypt(ciphertext, hybrid_key)
aes_dec_time = time.time() - start
print(f"AES Decryption Time: {aes_dec_time*1000:.2f} ms")

# Verify correctness
print("Decryption Correct:", decrypted == plaintext)
