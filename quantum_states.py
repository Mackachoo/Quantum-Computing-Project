#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Qubits interface for quantum computing.

Todo:
* Finish interface implementation.
* Finish method implementation.
* Design tests for custom qubit data type.
* Update docstrings.
"""

from abc import ABC, abstractmethod

import numpy as np
from errors import InputError


class QubitState(ABC):
    """Base class for Qubit and IntQubit"""

    @abstractmethod
    def __init__(self, values, ket=True):
        """ TODO: override me in either binary or denary representation """

        self.vals = values
        self.ket = ket

        self.strRep = ""

    @property
    def nQubits(self):
        """ TODO: override me to show bit number (decide alternative for denary)"""

        return len(self.vals)

    @property
    def qubitVals(self):
        """ TODO: return the values of the qubits as a tuple."""

        return (self.vals)

    @abstractmethod
    def flip(self):
        """ TODO: Flip the ket to a bra"""

        self.ket = False

    @abstractmethod
    def dotWith(self, ket):
        """ TODO: Implement dot product with another ket"""

        pass

    @abstractmethod
    def __str__(self):
        """TODO: ensure representation is appropiate"""

        if self.ket == True:
            return("|" + self.strRep + ">")
        else:
            return("<" + self.strRep + "|")



class Register(QubitState):
    """A multi-qubit ket in the computational (z) basis.

    We use the normal binary convention that the least significant qubit is on the
    right, so |00001> has a 1 in the least significant qubit.

    Parameters
    ==========

    values : list, str

        The qubit values as a list of ints: ([0,0,0,1,1]), a string: ('011'),
        or a tuple: (3,3) = [0, 1, 1].

        First tuple element is the representation of the state in denary
        second element is the dimensionality of our state space (i.e. # of elements in the vector).
        e.g.
        (1, 4) = [0,0,0,1]
        (0, 4) = [0,0,0,0]
        (9, 4) = [1,0,0,1]
    """

    def __init__(self, values, ket=True):

        super().__init__(values, ket)
        self.d = 2**values[1]

        if values[0]>self.d-1:
            raise InputError("State can't be represented with given number of qubits")

        #Implement Vector Representation (<0| = [1,0], <3| = [0,0,0,1])
        vr = np.zeros(self.d)
        vr[values[0]] = 1
        self.vec = vr

        bi = bin(values[0])
        binary = [int(n) for n in bi[2:].zfill(values[1])]
        self.bin = np.array(binary)


        for val in self.bin:
            self.strRep += str(val)

    def flip(self):
        """ TODO: Flip the ket to a bra"""
        self.ket = False

    def dotWith(self, ket):
        """ TODO: Implement dot product with another ket"""
        pass

    def __str__(self):
        """TODO: ensure representation is appropiate"""
        return super().__str__()


#class State():
#    """ Superposition of registers """
#    def __init__():



#-----------------------
#TESTS
#-----------------------
#bit = Register((0,2), ket=True)
#print(bit.strRep)
