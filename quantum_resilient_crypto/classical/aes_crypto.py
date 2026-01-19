# classical/aes_crypto.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key[:32], AES.MODE_ECB)
    return cipher.encrypt(pad(data, AES.block_size))

def aes_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key[:32], AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)


if __name__ == "__main__":
    from hybrid.hybrid_key import generate_hybrid_key
    from qkd.bb84 import run_bb84
    from pqc.kyber import kyber_alice_key

    # Generate hybrid key
    qkd_key, _, _, _ = run_bb84()
    pqc_key = kyber_alice_key()
    hybrid_key = generate_hybrid_key(qkd_key, pqc_key)

    # Example data
    plaintext = b"Hello Quantum-Resilient World!"
    ciphertext = aes_encrypt(plaintext, hybrid_key)
    decrypted = aes_decrypt(ciphertext, hybrid_key)

    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext.hex())
    print("Decrypted :", decrypted)
