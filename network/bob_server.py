# network/bob_server.py
import socket
from classical.aes_crypto import aes_decrypt
from hybrid.hybrid_key import generate_hybrid_key

HOST = '127.0.0.1'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Server listening on", HOST, PORT)

conn, addr = server.accept()
print("Connected by", addr)

# Receive full message
data = b''
while True:
    packet = conn.recv(1024)
    if not packet:
        break
    data += packet

# Generate hybrid key
hybrid_key = generate_hybrid_key()

# Decrypt
plaintext = aes_decrypt(data, hybrid_key)
print("Decrypted message:", plaintext)
conn.close()
