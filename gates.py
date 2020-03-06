import numpy as np
import operations as op
import hadamard as hdm
import quantum_states as qs

""" This will probably all need to be put into the Hadamard class so it can operate on it, or an updater could be added"""



def singleH():
    """TODO: This could be the single hadamard gate.""" 
    pass

def CNOTdepreciated():
    """TODO: This will be the CNOT gate."""
    matrix = np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,0,1],
                        [0,0,1,0]])
    return matrix

def NOT():                                ### This is Pauli X ?
    """TODO: This will be the NOT gate."""
    matrix = np.array([[0,1],
                       [1,0]])

    return matrix

def controlGate(gate, signVector):
    if len(signVector) == 2:
        return signVector
    else:
        return np.append(signVector[:-2],gate(signVector[-2:]))

def CNOT(signVector):
    return controlGate(NOT,signVector)


# Testing # --------------------------------------------------------------------

test = hdm.hadamardInterpretation(qs.Register((0, 2)))
print(test)
print()
print(CNOT(test.signVector))
test.applyGate(CNOT)
print()
print(test)
