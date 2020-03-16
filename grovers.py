"""
Contains all functions used to implement grover's algorithm
"""

import operations as op
import register as re
import quantum_states as qs
import numpy as np
import matplotlib.pyplot as plt
import time

def Oracle(nq, s):
    """ Returns the oracle gate when looking for mode s, with # of qubits nq """
    Tr = bin(s)[2:].zfill(nq)
    Neg = ""       #Stores the code for the Left and Rightmost layers (i.e. for |0> we get all 'XX')
    for i in Tr:
        if i == '0':
            Neg+="X"
        else:
            Neg+="I"
    L = op.constructGate(Neg)   #Constructs the matrices representing the leftmost and rightmost operations
    Z = op.constructGate(f"{nq}Z")  #Constructs the nq-dimansional CNOT gate (middle layer)
    return np.dot(np.dot(L, Z), L)


def Hadamard(nq):
    """Constructs the Hadamard gate (that is to be applied to all qubits)"""
    H = op.constructGate('H'*nq)
    return H


def Diffuser(nq):
    """ Returns the Grover's Diffusion operator for # of qubits nq """
    L = op.constructGate("X"*nq)   #Constructs the matrices representing the leftmost and rightmost operations
    Z = op.constructGate(f"{nq}Z")  #Constructs the nq-dimansional CNOT gate (middle layer)
    return np.dot(np.dot(L, Z), L)

def Grovers(nq, s, print):
    if print:
        print('\n'+"-------Making gates------:")
        print("Making Hadamard")
    H = Hadamard(nq)
    if print:
        print("Making Oracle")
    Orac = Oracle(nq, s)
    if print:
        print("Making Diffusion Operator" + '\n')
    Diff = Diffuser(nq)

    #Initialising Register in a uniform superposition
    if print:
        print("-------Initialising Register-------" + '\n')
    R = re.Register(qs.State((0,nq)))
    start_time = time.time()
    R.applyGate(H)

    #Iterating it times
    it = int(np.pi/(4*np.arcsin(1/np.sqrt(2**nq))))
    if print:
        print('\n'+ f"Running Grover's, {it} times:")
    for i in range(it):
        R.applyGate(Orac)
        R.applyGate(H)
        R.applyGate(Diff)
        R.applyGate(H)
    Dt = time.time() - start_time
    return R, Dt


def FrequencyPlot(freq, States):
    xaxis = list(range(0,len(States)))
    plt.bar(xaxis,freq, tick_label=States)
    plt.ylabel("occurrences")
    plt.xlabel("states")
    plt.xticks(rotation=90)
    plt.title("Plot of Occurrences of Each State")
    for i in range (0, len(States)):
        plt.annotate(freq[i], xy=(i, freq[i]), ha='center', va='bottom')
    plt.show()

"""
Observe the system S, n times. This simulates the "Uncertainty" in the outcome of the observation.
Parameters: Register (R), number of times you want to "run" Grover's (n), number of qubits(nq).

As the state of the system before observing it, is definite, we don't need to run Grover's each time.
Just simulate the final measurement using the register.measure() method, that implements a Monte-Carlo approach
for counting how many times each state was observed in a given number of trials.
"""
def Observe_System(R, n, nq):

    Obs = []
    States = [f"|{bin(i)[2:].zfill(nq)}>" for i in range(2**nq)]
    freq = []

    for i in range(n):
        Obs.append(R.measure())

    for s in States:
        freq.append(Obs.count(s))

    print('\n' + f"# of Occurances of each state after measuring the system {n} times:")
    for i in range(len(freq)):
        print(f"{States[i]}: {freq[i]}")

    FrequencyPlot(freq, States)
