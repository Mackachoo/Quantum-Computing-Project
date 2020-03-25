import numpy as np
import quantum_states as qs
import math as m
import operations as op
from random import random as rnd
import sparse as sp


class Register():
    """ Class to represent the System (Register) at any point in time

    Receives a basis state as its input (can only be initialised as a non-superposed state)
    Main representation is the list self.stateVector where all the coefficients for each basis state are stored.

    Parameters
    ----------
    input : type
        Description of parameter `input`.

    Attributes
    ----------
    qR : quantum_states.State
        stores the quantum register dynamically created elsewhere.
    stateVector : numpy array
        list of amplitudes and signs for each basis state.
    qbitVector : numpy array
        list of individual basis states.
    Methods
    -------
    applyGate(self, gate)
        operates matrix "gate" on the Register's stateVector
    measure(self)
        returns a basis state of the register randonly, depending on the amplitude of the basis states (does not change the stateVector)
        i.e. the measurement is not realistic
    measure_collapse(self)
        same as measure(self), but actually collapses the register to a basis state (which it returns)
        After the measurement the register is not in a superposition .
    __str__(self)
        string representation of state

    Examples
    --------
    |s> = -0.2|0> + 0.9|1>, has
    self.stateVector = [-0.2, 0.9], and
    self.qbitVector = [Register(0,1), Register(1,1)] (i.e. a list of pure "states" [|0>, |1>])
    __str__ prints: '-0.2|0> + 0.9|1>'
    """

    def __init__(self,input, Sparse=False):
        """
        Parameters
        ----------
        input : quantum_states.State
            quantum basis state dynamically created elsewhere (grovers in our case).
        """

        self.qR = input     # Stores the input quantum register.

        # This creates the stateVector by calling vectorRepresentation().
        self.stateVector = self.qR.vec
        # This creates a array of the form [|0>,|1>,|2>,...,|2^(dimension)>].
        self.qbitVector = np.array([qs.State((i,self.qR.values[1])) for i in range(self.qR.d)])


    def applyGate(self, gate, Sparse = False):
        """Operates the matrix "gate" on the register.

        Works by simple matrix-vector multiplication.

        Parameters
        ----------
        gate : numpy array
            matrix to be applied to the register's vector representation.
        """
        self.stateVector = op.vecMatProduct(gate, self.stateVector)

    def measure(self):
        """Uses Monte-Carlo approach, to choose and return a basis state of the register randomly,
        depending on amplitudes in stateVector

        Returns
        -------
        f-string
            the string representation of the selected basis state.
        """

        ## "Uncertainty" is simulated using a Monte-Carlo like approach.
        r = rnd() #random number, uniform probability from 0 to 1
        sum = 0
        for i in range(self.qR.d):  # for i in range (number of states)
            amp = self.stateVector[i] #get the amplitude of the state
            sum += amp.real**2 + amp.imag**2  #find the probability of it occuring and add it to sum
            if r <= sum: #if r is in the interval (sum, sum+prob(state)) then "colapse" system to state
                return (f"{self.qbitVector[i]}")

    def measure_collapse(self):
        """Colapses the System into one basis state depending on amplitudes in stateVector
        Works exactly the same as measure(self), but doesn't leave the register intact.
        Built for added realism

        Returns
        -------
        f-string
            the string representation of the selected basis state.
        """
        ## "Uncertainty" is simulated using a Monte-Carlo like approach.
        r = rnd() #random number, uniform probability from 0 to 1
        sum = 0
        for i in range(self.qR.d):  # for i in range (number of states)
            amp = self.stateVector[i] #get the amplitude of the state
            sum += amp.real**2 + amp.imag**2  #find the probability of it occuring and add it to sum
            if r <= sum: #if r is in the interval (sum, sum+prob(state)) then "colapse" system to state
                self.stateVector = np.zeros(self.qR.d)
                self.stateVector[i] = 1
                return (f"{self.qbitVector[i]}")


    def __str__(self):
        """String representation of full register

        Returns
        -------
        str
            representation of register as superposition of states.
        """
        output = ""
        for i in range(self.qR.d):
            if self.stateVector[i] >= 0:
                output += f" +{round(self.stateVector[i],5)}{self.qbitVector[i]}"
            else:
                output += f" {round(self.stateVector[i],5)}{self.qbitVector[i]}"
        return output
