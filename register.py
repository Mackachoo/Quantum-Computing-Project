import numpy as np
import quantum_states as qs
import math as m
import operations as op
from random import random as rnd

"""
-Class to represent the System (Register) at any point in time
-Receives a pure state as its input (can only be initialised as a pure state, as in real life)
-Main representation is the list self.signVector where all the coefficients for the modes are stored.
e.g
|s> = -0.2|0> + 0.9|1>, has
self.signVector = [-0.2, 0.9], and
self.qbitVector = [Register(0,1), Register(1,1)] (i.e. a list of pure "states" [|0>, |1>])

"""


class Register():

    def __init__(self,input):

        self.qR = input                                                                                 # Stores the input quantum register.

        self.signVector = self.qR.vec                                                                   # This creates the signVector by calling vectorRepresentation().
        self.qbitVector = np.array([qs.State((i,self.qR.values[1])) for i in range(self.qR.d)])      # This creates a array of the form [|0>,|1>,|2>,...,|2^(dimension)>].


    def applyGate(self, gate):
        """ Operates the matrix "gate" on the Register, (simple matrix-vector multiplication)"""
        self.signVector = np.dot(gate, self.signVector)

    def measure(self):
        """
        Randomly colapses the System into one state depending on amplitudes
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
        """TODO: allows hadamard class to be printed nicely.
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
