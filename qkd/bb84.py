import random

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]  # + = rectilinear, x = diagonal

def encode_qubits(bits, bases):
    return list(zip(bits, bases))  # (bit, basis)

# without eve 
# def measure_qubits(qubits, bases):
 #   measured = []
  #  for (bit, sender_basis), receiver_basis in zip(qubits, bases):
   #     if sender_basis == receiver_basis:
    #        measured.append(bit)
     #   else:
      #      measured.append(random.randint(0, 1))  # wrong basis → random result
    #return measured

#with eve
def measure_qubits(qubits, bases, eve=False):
    measured = []
    for (bit, sender_basis), receiver_basis in zip(qubits, bases):
        if eve:
            eve_basis = random.choice(['+', 'x'])
            if eve_basis != sender_basis:
                bit = random.randint(0, 1)

        if sender_basis == receiver_basis:
            measured.append(bit)
        else:
            measured.append(random.randint(0, 1))
    return measured

def sift_key(sender_bases, receiver_bases, bits):
    key = []
    for sb, rb, bit in zip(sender_bases, receiver_bases, bits):
        if sb == rb:
            key.append(bit)
    return key

def detect_eavesdropper(alice_key, bob_key, threshold=0.2):
    errors = sum(a != b for a, b in zip(alice_key, bob_key))
    error_rate = errors / len(alice_key)
    return error_rate > threshold, error_rate

def run_bb84(n=128):
    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)

    qubits = encode_qubits(alice_bits, alice_bases)

    bob_bases = generate_bases(n)
    #with out eve 
    # bob_measurements = measure_qubits(qubits, bob_bases)
    bob_measurements = measure_qubits(qubits, bob_bases, eve=True)


    alice_key = sift_key(alice_bases, bob_bases, alice_bits)
    bob_key = sift_key(alice_bases, bob_bases, bob_measurements)

    eavesdrop, error_rate = detect_eavesdropper(alice_key, bob_key)

    return alice_key, bob_key, eavesdrop, error_rate

if __name__ == "__main__":
    ak, bk, eve, err = run_bb84()
    print("Alice Key:", ak[:20])
    print("Bob Key  :", bk[:20])
    print("Eavesdrop Detected:", eve)
    print("Error Rate:", err)
