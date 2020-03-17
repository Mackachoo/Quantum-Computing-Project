import numpy as np
import quantum_states as qs
import math as m
import operations as op
from random import random as rnd
import sparse as sp


class Register():
    """ Class to represent the System (Register) at any point in time

    Receives a pure state as its input (can only be initialised as a pure state, as in real life)
    Main representation is the list self.signVector where all the coefficients for the modes are stored.

    Parameters
    ----------
    input : type
        Description of parameter `input`.

    Attributes
    ----------
    qR : quantum_states.State
        stores the quantum register dynamically created elsewhere.
    signVector : numpy array
        list of amplitudes and signs of each state.
    qbitVector : numpy array
        list of individual states.
    Methods
    -------
    applyGate(self, gate)
        operates matrix "gate" on the Register
    measure(self)
        collapses register into most probable state
    __str__(self)
        string representation of state: |s> = -0.2|0> + 0.9|1>

    Examples
    --------
    |s> = -0.2|0> + 0.9|1>, has
    self.signVector = [-0.2, 0.9], and
    self.qbitVector = [Register(0,1), Register(1,1)] (i.e. a list of pure "states" [|0>, |1>])
    """

    def __init__(self,input, Sparse=False):
        """
        Parameters
        ----------
        input : quantum_states.State
            quantum state dynamically created elsewhere (grovers in our case).
        """

        self.qR = input     # Stores the input quantum register.

        # This creates the signVector by calling vectorRepresentation().
        self.signVector = self.qR.vec
        # This creates a array of the form [|0>,|1>,|2>,...,|2^(dimension)>].
        self.qbitVector = np.array([qs.State((i,self.qR.values[1])) for i in range(self.qR.d)])


    def applyGate(self, gate, Sparse = False):
        """Operates the matrix "gate" on the register.

        Used for Haddamard, Oracle, and Diffuser gates dynamically.
        Works by simple matrix-vector multiplication.

        Parameters
        ----------
        gate : numpy array
            matrix to be applied to the register's vector representation.
        """
        vec = self.signVector
        if Sparse:
            shape = (len(vec),1)
            vec = sp.Sparse(np.resize(vec, shape), shape)
        self.signVector = op.vecMatProduct(gate, vec).asMatrix()

    def measure(self):
        """Colapses the System into one state depending on amplitudes of
           each state

        Returns
        -------
        f-string
            the string representation of the state with the
            selected amplitude.
        """

        ## "Uncertainty" is simulated using a Monte-Carlo like approach.
        r = rnd() #random number, uniform probability from 0 to 1
        sum = 0
        for i in range(self.qR.d):  # for i in range (number of states)
            amp = self.signVector[i] #get the amplitude of the state
            sum += amp.real**2 + amp.imag**2  #find the probability of it occuring and add it to sum
            if r <= sum: #if r is in the interval (sum, sum+prob(state)) then "colapse" system to state
                return (f"{self.qbitVector[i]}")

    def __str__(self):
        """String representation of full register

        Returns
        -------
        str
            representation of register as superposition of states.

        TODO: allow hadamard class to be printed nicely.
        Representation :
            H = (1/√2ⁿ)*Σ registers[i]
              = fⁿ(signVector ᛫ qbitVector)
                where (1/√2ⁿ) is the normalisation factor fⁿ.
        """
#        power = m.log2(len(self.signVector))
#        sqrt2 = ""
#        if power%2 == 1:
#            sqrt2 = "√2"
#        output = f"1/{int(2**(power//2))}{sqrt2}("
        output = ""
        for i in range(self.qR.d):
            if self.signVector[i] >= 0:
                output += f" +{round(self.signVector[i],5)}{self.qbitVector[i]}"
            else:
                output += f" {round(self.signVector[i],5)}{self.qbitVector[i]}"
        return output

# Testing # --------------------------------------------------------------------

#test = Register(qs.Register((0,2)))
#test.applyGate("HH")
#print()
#print(test)
#print()
