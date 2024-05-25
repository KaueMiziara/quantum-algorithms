# Quantum Solutions

## Qiskit
[Medium post explaining the solution (WIP)](https://medium.com/@kauemiziara)

```python
def eight_trees(trees: list) -> int:
    qc = QuantumCircuit(9, 1)
    [qc.x(i) for i in range(8) if trees[i]]

    qc.cx(0, 8)
    qc.cx(1, 8)
    qc.cx(2, 8)
    qc.cx(3, 8)
    qc.cx(4, 8)
    qc.cx(5, 8)
    qc.cx(6, 8)
    qc.cx(7, 8)
    qc.ccx(0, 1, 8)
    qc.ccx(1, 2, 8)
    qc.ccx(2, 3, 8)
    qc.ccx(3, 4, 8)
    qc.ccx(4, 5, 8)
    qc.ccx(5, 6, 8)
    qc.ccx(6, 7, 8)

    qc.measure(8, 0)

    display(qc.draw())

    backend = AerSimulator()
    result = backend.run(qc, shots = 1).result().get_counts()

    output = list(result.keys())[0]
    return int(output)
```
