import quantum_states as qs
import numpy as np
import hadamard as hdm


def CNOT(hadamard):
    pass

qbit = qs.Register((1, 3), ket=True)
hadamard = hdm.hadamardInterpretation(qbit)
print(hadamard)