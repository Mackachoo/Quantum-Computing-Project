import quantum_states as qs
import numpy as np
import grovers as gr
import register as re

##___________________________________Demonstration______________________________##
s = int(input("Which state are you looking for?: "))
nq = int(input("Number of qubits: "))

#Make gates
H = gr.Hadamard(nq)
Orac = gr.Oracle(nq, s)
Diff = gr.Diffuser(nq)

#Show them for the eyes of the world
print("Hadamard: ")
print(H)
print("Oracle: ")
print(Orac)

#Make Register and apply gates
R = re.Register(qs.State((0,nq)))
R.applyGate(H)
print(f"Starting with the Register in the pure state {qs.State((0,nq))} and applying Hadamard's gate to all qubits once we obtain: ")
print(R)

print(f"Then as specified we are looking for state {qs.State((s,nq))}. After applying the Oracle we have: ")
R.applyGate(Orac)
print(R)
