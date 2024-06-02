from qiskit.circuit import QuantumCircuit
from qiskit_aer import AerSimulator

def eight_trees(trees: list) -> int:
    n = len(trees)
    qc = QuantumCircuit(n + 1, 1)
    [qc.x(i) for i in range(n) if trees[i]]

    [qc.cx(i, n) for i in range(n)]
    
    [qc.ccx(i, i+1, n) for i in range(n - 1)]

    qc.measure(n, 0)

    backend = AerSimulator()
    result = backend.run(qc, shots = 1).result().get_counts()

    output = list(result.keys())[0]
    return int(output)
