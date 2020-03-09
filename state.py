import numpy as np
import quantum_states as qs
import math as m
import operations as op
from random import random as rnd

"""
This runs a quantum register through a hadamard gate and then keeps it in the representation.
Representation :
    H = (1/√2ⁿ)*Σ registers[i]
      = fⁿ(signVector ᛫ qbitVector)
        where (1/√2ⁿ) is the normalisation factor fⁿ.
"""


class state():

    def __init__(self,input):
        self.qR = input                                                                                 # Stores the input quantum register.

        self.signVector = self.qR.vec                                                                   # This creates the signVector by calling vectorRepresentation().
        self.qbitVector = np.array([qs.Register((i,self.qR.values[1])) for i in range(self.qR.d)])      # This creates a array of the form [|0>,|1>,|2>,...,|2^(dimension)>].


    def applyGate(self, gate):
        self.signVector = op.vecMatProduct(gate, self.signVector)

    def observe(self):
        """
        Randomly colapses the state into one outcome depending on amplitudes
        """
        r = rnd() #random number, uniform probability from 0 to 1
        sum = 0
        for i in range(self.qR.d):
            amp = self.signVector[i]
            sum += amp.real**2 + amp.imag**2
            if r <= sum:
                return (f"{self.qbitVector[i]}")

    def __str__(self):
        """TODO: allows hadamard class to be printed nicely."""
#        power = m.log2(len(self.signVector))
#        sqrt2 = ""
#        if power%2 == 1:
#            sqrt2 = "√2"
#        output = f"1/{int(2**(power//2))}{sqrt2}("
        output = ""
        for i in range(self.qR.d):
            if self.signVector[i] >= 0:
                output += f" +{round(self.signVector[i],3)}{self.qbitVector[i]}"
            else:
                output += f" {round(self.signVector[i],2)}{self.qbitVector[i]}"
        return output


# Testing # --------------------------------------------------------------------

#test = state(qs.Register((0,2)))
#test.applyGate("HH")
#print()
#print(test)
#print()
