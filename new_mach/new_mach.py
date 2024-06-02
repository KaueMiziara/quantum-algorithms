import numpy as np
from qiskit.circuit import QuantumCircuit, Qubit, Clbit
from qiskit.quantum_info import Operator
from qiskit_aer import AerSimulator


def beam_splitter(r: float) -> np.array:
    """
    Returns the beam splitter matrix.

    Args:
        - r (float): The reflection coefficient of the beam splitter.
    Returns:
        - (np.array): 2 x 2 matrix that represents the beam
        splitter matrix.    
    """
    t = np.sqrt(1 - r**2)
    return np.array([[r, t], [t, -r]])


def mz_interferometer(r: float) -> np.array:
    """
    This quantum circuit returns the probability that either A or C
    detect a photon, and the probability that D detects a photon.
    
    Args:
        - r (float): The reflection coefficient of the beam splitters.
    Returns: 
        - np.array(float): An array of shape (2,), where the first 
        element is the probability of detection at A or C,
        and the second element is the probability of detection at D.
    """
    
    bits = [Qubit(), Clbit(), Clbit(), Clbit()]
    qc = QuantumCircuit(bits)

    splitter_op = Operator(beam_splitter(r))
    qc.unitary(splitter_op, 0, label="Beam Splitter")
    qc.measure(0, 0)

    with qc.if_test((bits[1], 0)) as else_:
        pass
    with else_:
        qc.unitary(splitter_op, 0, label="Beam Splitter")
        qc.measure(0, 1)
        qc.measure(0, 2)

    backend = AerSimulator()
    
    shots = 2**20
    job = backend.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()

    det_a = counts['000']
    det_c = counts['001']
    det_d = counts['111']

    p_ac = (det_a + det_c)/shots
    p_d = det_d/shots
    
    return np.array([p_ac, p_d])
