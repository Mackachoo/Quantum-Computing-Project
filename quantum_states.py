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
        self.mathRep = np.zeros(len(values))

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



class Qubit(QubitState):
    """A multi-qubit ket in the computational (z) basis.

    We use the normal binary convention that the least significant qubit is on the
    right, so |00001> has a 1 in the least significant qubit.

    Parameters
    ==========

    values : list, str
        The qubit values as a list of ints ([0,0,0,1,1]) or a string ('011').
    """

    def __init__(self, values, ket=True):

        super().__init__(values, ket)
        for i, val in enumerate(values):
            if int(val) == 1:
                self.strRep += str(val)
                self.mathRep[i] = val
            elif int(val) == 0:
                self.strRep += str(val)
                self.mathRep[i] = val
            else:
                raise InputError("Can only accept sequence of 1s and 0s")

    def flip(self):
        """ TODO: Flip the ket to a bra"""
        self.ket = False

    def dotWith(self, ket):
        """ TODO: Implement dot product with another ket"""
        pass

    def __str__(self):
        """TODO: ensure representation is appropiate"""
        return super().__str__()


class IntQubit(QubitState):

    def __init__(self, value, ket=True):
        super().__init__(value, ket)
        if type(value) == int:
            self.strRep = str(value)
        else:
            raise InputError("Can only accept an integer label for the qubit")

    def flip(self):
        """ TODO: Flip the ket to a bra"""
        super()

    def dotWith(self, ket):
        """ TODO: Implement dot product with another ket"""
        pass

    def __str__(self):
        """TODO: ensure representation is appropiate"""
        return super().__str__()

#-----------------------
#TESTS
#-----------------------
bit = Qubit([0,0,1], ket=False)
bit2 = Qubit("010")
print(bit)
print(bit2)