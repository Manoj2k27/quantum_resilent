from pqc.kyber import kyber_alice_key
import hashlib

SHARED_QKD_KEY = [1]*128  # fixed 128-bit QKD key for Alice & Bob

def generate_hybrid_key():
    pqc_key = kyber_alice_key()
    qkd_bytes = int("".join(map(str, SHARED_QKD_KEY)), 2).to_bytes(16, byteorder='big')
    combined = qkd_bytes + pqc_key
    return hashlib.sha256(combined).digest()

if __name__ == "__main__":
    # Example usage
    from qkd.bb84 import run_bb84
    from pqc.kyber import kyber_alice_key

    qkd_key, _, _, _ = run_bb84()
    pqc_key = kyber_alice_key()

    hybrid_key = generate_hybrid_key(qkd_key, pqc_key)

    print("Hybrid Key (hex):", hybrid_key.hex())
    print("Length:", len(hybrid_key), "bytes")
