import operations as op
import register as re
import quantum_states as qs
import numpy as np
import matplotlib.pyplot as plt
import time

def Oracle(nq, s, Sparse = False):
    """ Function that dynamically creates the oracle gate

    Using deterministic algorithm for mode s, with number of qubits nq,
    function creates a matrix made up from lower-level gates which serves as
    the oracle gate when applied to an entangled quantum register.

    Parameters
    ----------
    nq : int
        Number of qubits per state.
    s : int
        Denary representation of state the gate is applied to.

    Returns
    -------
    numpy array or sp.Sparse
        returns an nq-dimensional numpy array which can be applied as an Oracle
        gate on a quantum register

    """
    #takes binary representation of state and formats it to construct gate
    Tr = bin(s)[2:].zfill(nq)
    Neg = ""        #Stores the code for the Left
                    #and Rightmost layers (i.e. for |0> we get all 'XX')
    for i in Tr:
        if i == '0':
            Neg+="X"
        else:
            Neg+="I"

    #Constructs the matrices representing the leftmost and rightmost operations
    L = op.constructGate(Neg, Sparse)
    #Constructs the nq-dimansional CNOT gate (middle layer)
    Z = op.constructGate(f"{nq}Z", Sparse)
    return op.matrixProduct(op.matrixProduct(L, Z), L)


def Hadamard(nq, Sparse = False):
    """ Constructs the Hadamard gate (that is to be applied to all qubits)

    Parameters
    ----------
    nq : int
        Number of qubits per state.

    Returns
    -------
    numpy array or sp.Sparse
        returns an nq-dimensional numpy array which can be applied as a Hadamard
        gate on a quantum register
    """

    H = op.constructGate('H'*nq, Sparse)
    return H


def Diffuser(nq, Sparse = False):
    """ Returns the Grover's Diffusion operator for # of qubits nq

    Parameters
    ----------
    nq : int
        Number of qubits per state.

    Returns
    -------
    numpy array or sp.Sparse
        returns an nq-dimensional numpy array which can be applied as a Diffuser
        gate on a quantum register
    """
    L = op.constructGate("X"*nq, Sparse)   #Constructs the matrices representing the leftmost and rightmost operations
    Z = op.constructGate(f"{nq}Z", Sparse)  #Constructs the nq-dimansional CNOT gate (middle layer)
    return op.matrixProduct(op.matrixProduct(L, Z), L)


def Grovers(nq, s, cOut, Sparse = False):
    """ Actual function running grover's algorithm.

    Capable of adapting gates dynamically depending on the mode and number of
    qubits selected by user.

    Parameters
    ----------
    nq : type
        Description of parameter `nq`.
    s : type
        Denary representation of state.

    Returns
    -------
    register.Register, int
        The custom register object starts as a uniform superposition of States
        which is then put through Grover's algorithm 'it' times and the heavily
        weighted (towards target state) register is returned at the end.

        Dt is the time interval that it took to run Grovers 'it' times on
        register.
    """
    if cOut:
        print('\n'+"-------Making gates------:")
        print("Making Hadamard")
    H = Hadamard(nq, Sparse)
    if cOut:
        print("Making Oracle")
    Orac = Oracle(nq, s, Sparse)
    if cOut:
        print("Making Diffusion Operator" + '\n')
    Diff = Diffuser(nq, Sparse)

    #Initialising Register in a uniform superposition
    if cOut:
        print("-------Initialising Register-------" + '\n')
    #pass an n-qbit determinate state 0
    R = re.Register(qs.State((0,nq)))
    start_time = time.time()
    #n-dimensional hadamard creates uniform superposition of states up until state(2**nq)
    R.applyGate(H, Sparse)

    #Iterating -it times (most accurate order of iteration, ussually simply quoted as root(n))
    it = int(np.pi/(4*np.arcsin(1/np.sqrt(2**nq))))
    if cOut:
        print('\n'+ f"Running Grover's, {it} times:")
    for i in range(it):
        R.applyGate(Orac, Sparse)
        R.applyGate(H, Sparse)
        R.applyGate(Diff, Sparse)
        R.applyGate(H, Sparse)
    Dt = time.time() - start_time
    return R, Dt


def FrequencyPlot(freq, States):
    """Plots a graph of each state and how many times it was observed.

    Times selected is analogous to probability of being the 'correct' target state.

    Parameters
    ----------
    freq : list of int
        Number of occurances for each state.
    States : list of strings
        List containing each possible state, in dirac notation.
    """

    xaxis = list(range(0,len(States)))
    plt.bar(xaxis,freq, tick_label=States)
    plt.ylabel("occurrences")
    plt.xlabel("states")
    plt.xticks(rotation=90)
    plt.title("Plot of Occurrences of Each State")
    for i in range (0, len(States)):
        plt.annotate(freq[i], xy=(i, freq[i]), ha='center', va='bottom')
    plt.show()


def Observe_System(R, n, nq):
    """ Observe the register R, n times.

    This simulates the "Uncertainty" in the outcome of the observation.

    As the state of the system before observing it, is definite, we don't need
    to run Grover's each time. Just simulate the final measurement using
    the register.measure() method, that implements a Monte-Carlo approach to choose
    which state the system is going to collapse to when measuring it.

    Calls for plot of measurements at the end.


    Parameters
    ----------
    R : register.Register
        Custom register object.
    n : int
        Number of times Grover's was "ran". Grover's doesn't actually have to be ran
        n times, as the final amplitudes are definite.
    nq : int
        Number of quibits used to represent each state.
    """

    Obs = []
    States = [f"|{bin(i)[2:].zfill(nq)}>" for i in range(2**nq)]
    freq = []

    for i in range(n):
        Obs.append(R.measure())

    for s in States:
        freq.append(Obs.count(s))

    print('\n' + f"# of Occurences of each state after measuring the system {n} times:")
    for i in range(len(freq)):
        print(f"{States[i]}: {freq[i]}")
    if nq <= 5:
        FrequencyPlot(freq, States)
    return (max(freq))
