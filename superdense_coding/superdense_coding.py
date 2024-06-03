from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def string_to_bin(mensagem: str) -> list:
    return [format(ord(c), '08b') for c in mensagem]


def bin_to_string(bin: list) -> str:
    return ''.join([chr(int(b, 2)) for b in bin])


def split_into_pairs(bin: list) -> list:
    result = []

    for byte in bin:
        pairs = [byte[i:i+2] for i in range(0, len(byte), 2)]
        result.append(pairs)
    
    return result


def list_from_pairs(pairs: list) -> list:
    byte_list = []

    for pair in pairs:
        byte = ''.join(pair)
        byte_list.append(byte)

    return byte_list


def emaranhar(qubits: int) -> QuantumCircuit:
    qc = QuantumCircuit(qubits)

    qc.h(0)
    qc.cx(0, 1)

    return qc


def sua_parte(qc: QuantumCircuit, bin: list) -> QuantumCircuit:
    if bin[0] == '1':
        qc.z(0)
    if bin[1] == '1':
        qc.x(0)

    return qc


def alice_parte(qc: QuantumCircuit) -> list:
    qc.cx(0, 1)
    qc.h(0)
    qc.measure_all()

    result = AerSimulator().run(qc, shots=1).result()
    stats = result.get_counts()

    return list(stats.keys())


def protocol(bin: list) -> list:
    pairs = split_into_pairs(bin)

    result = []
    for byte in pairs:
        byte_result = []
        for pair in byte:
            qc = emaranhar(2)
            qc = sua_parte(qc, list(pair))
            received = alice_parte(qc)
            adjusted = received[0][::-1]
            
            byte_result.append(adjusted)
        result.append(byte_result)

    return result


def main():
    message = "Hello, world!"
    message_bin = string_to_bin(message)

    received_message = protocol(message_bin)
    decoded_message = bin_to_string(list_from_pairs(received_message))

    print(decoded_message)
