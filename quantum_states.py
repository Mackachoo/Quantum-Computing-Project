
""" Basis State interface for quantum computing.
"""

from abc import ABC, abstractmethod

import numpy as np
from errors import InputError


class QubitState(ABC):
    """ Base class for State serving as an interface.
    Methods are all abstract and overriden in child classes

    Parameters
    ----------
    values : tuple
        Contains the (state, no. qubits used to represent it).
    ket : Bool=True
        sets wether to treat state in bra or ket representation,
        used to set vector and string representations

    Attributes
    ----------
    vals : tuple
        tuple of (state, no. of qubits) .
    strRep : str
        string representation of superposition of states.
    ket: Bool
        property dictating vector and string representation

    Methods (Abstract)
    ------------------
    flip(self)
        override: flip ket to bra and viceversa
    __str__
        override: appropiate string representation of state

    """

    @abstractmethod
    def __init__(self, values, ket=True):
        """ Override me in either binary or denary representation """

        self.vals = values
        self.ket = ket

        self.strRep = ""

    @abstractmethod
    def flip(self):
        """ Flip the ket to a bra and viceversa"""
        pass
    @abstractmethod
    def __str__(self):
        """ Ensure representation is appropiate"""
        pass


class State(QubitState):
    """Class representing a multi-qubit ket (basis state) in the computational (z) basis.

    -Note: We use the normal binary convention that the least significant
     qubit is on the right, so |00001> has a 1 in the least significant qubit.

    Parameters
    ----------
    values : tuple
        Contains the (state, no. qubits used to represent it).
    ket : Bool=True
        sets wether to treat state in bra or ket representation,
        used to set vector and string representations

    Attributes
    ----------
    values : tuple
        tuple of (state, no. of qubits)
            First element is the representation of the state in denary,
            second element is the number of qubits.
            e.g: (1, 4) = |0001>
    strRep : str
        string representation of state.
    ket: Bool
        property dictating vector and string representation
    d : int
        qubits used to represent the state
    den : int
        denary representation of state, e.g. |011> has den = 3.
    vec : numpy array
        list of qubits representing the state vector, e.g. |01> = [0,1,0,0]
    bin : str
        binary representation of state as 0b___ e.g. |3> has bin = "0b11"
    strRep : str
        string representaiton of the state in dirac notation: |state>.

    Methods
    -------
    flip(self)
        flip ket to a bra and viceversa
    dotWith(self, ket)
        dot operation between state's vector representation and another object
    __str__(self)
        represent state in string representation
    """

    def __init__(self, values, ket=True):

        super().__init__(values, ket)
        self.values = values
        self.d = 2**values[1]    #number of qubits
        self.den = values[0]     #Integer representation of State

        if self.den>self.d-1:
            raise InputError("State can't be represented with given number of qubits")

        #Implement Vector Representation (|0> = [1,0], |3> = [0,0,0,1])
        vr = np.zeros(self.d)
        vr[self.den] = 1
        self.vec = np.array(vr)

        bi = bin(self.den)
        self.bin = np.array([int(n) for n in bi[2:].zfill(values[1])])


        for val in self.bin:
            self.strRep += str(val)

    def flip(self):
        """ Flip the ket to a bra and viceversa"""
        self.ket = not self.ket

    def __str__(self):
        """ Appropiate string representation of state. Dirac notation"""
        if self.ket == True:
            return(f"|{self.strRep}>")
        else:
            return(f"<{self.strRep}|")
