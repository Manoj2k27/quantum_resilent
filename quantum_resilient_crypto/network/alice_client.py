# network/alice_client.py
import socket
from classical.aes_crypto import aes_encrypt
from hybrid.hybrid_key import generate_hybrid_key

HOST = '127.0.0.1'
PORT = 65432

# Generate hybrid key
hybrid_key = generate_hybrid_key()

# Encrypt message
plaintext = b'Hello Quantum-Resilient World!'
ciphertext = aes_encrypt(plaintext, hybrid_key)

# Send over network
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(ciphertext)
client.shutdown(socket.SHUT_WR)
client.close()
print("Message sent.")
