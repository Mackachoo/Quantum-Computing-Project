"""
Contains all functions used to implement grover's algorithm
"""

import operations as op
import hadamard as ha
import quantum_states as qs

def Oracle(nq, s):
    """ Returns the oracle gate for mode s, with # of qubits nq """
    Tr = bin(s)[2:]
    Tr = Tr.zfill(nq)
    Neg = ""       #Stores the code for the Left and Rightmost layers (i.e. for |0> we get all 'XX')
    for i in Tr:
        if i == '0':
            Neg+="X"
        else:
            Neg+="I"
    L = op.constructGate(Neg)   #Constructs the matrices representing the leftmost and rightmost operations
    Z = op.constructGate(f"{nq}Z")  #Constructs the nq-dimansional CNOT gate (middle layer)
    Orac = op.matrixProduct(L, Z)
    Orac = op.matrixProduct(Orac, L)
    return Orac

def Hadamard(nq):
    """Constructs the Hadamard gate (that is to be applied to all qubits)"""
#    H_code = ''
#    for i in range (nq):
#        H_code += 'H'
    H = op.constructGate('H'*nq)
    return H


##___________________________________Demonstration______________________________##
s = int(input("which state are you looking for?: "))
nq = int(input("number of qubits: "))

#Make gates
H = Hadamard(nq)
Orac = Oracle(nq, s)

#Show them for the eyes of the world
print(H)
print(Orac)

#Make state and apply gates
S = ha.state(qs.Register((0,nq)))
S.applyGate(H)
print(f"Starting with state {qs.Register((0,nq))} and applying Hadamard's gate to all qubits once we obtain: ")
print(S)

print(f"Then as specified we are looking for state {qs.Register((s,nq))}. After applying the Oracle we have: ")
S.applyGate(Orac)
print(S)
