import numpy as np
import quantum_states as qs
import math as m


"""
This runs a quantum register through a hadamard gate and then keeps it in the representation.

Representation :
    H = (1/√2ⁿ)*Σ registers[i]
      = fⁿ(signVector ᛫ qbitVector)
      
        where (1/√2ⁿ) is the normalisation factor fⁿ.


"""


class hadamardInterpretation():

    def __init__(self,qRegister):
        self.qR = qRegister                                                                             # Stores the input quantum register.

        self.signVector = self.vectorRepresenation(self.qR.bin, np.array([1]))                          # This creates the signVector by calling vectorRepresentation().
        self.qbitVector = np.array([qs.Register((i,self.qR.values[1])) for i in range(self.qR.d)])      # This creates a array of the form [|0>,|1>,|2>,...,|2^(dimension)>].


    def vectorRepresenation(self,qBinary,vRep):
        """
        This is for and only for the initilizing function to create the signVector.
            - It is a recursive function that why it may look wierd.
            - It creates the vector by looking through the binary representation of the quantum register from right to left.
            - This creates the vector that you dot with qbitVector to form the non normalised hadamard representation.
            - Watch vRep/vR this is what it's building to signVector
        """
        if len(qBinary) == 0:                                       # Recusive exit condition, ie when list is done it returns what it has made.
            return vRep
        else:
            if qBinary[-1:] == 0:                                   # Checks whether the last number of the binary representation is 0 or 1.
                vR = np.concatenate((vRep,vRep))                    # For 0, it adds the next vector duplication as according to hadamard. ie |0> -> +|0>+|1>
            else:
                vR = np.concatenate((vRep,-vRep))                   # For 1, it adds the next inverse vector duplication as according to hadamard. ie |1> -> +|0>-|1>
            return self.vectorRepresenation(qBinary[:-1],vR)        # Returns it recursively with the last digit removed and the updated vRep/vR.

    
    def applyGate(self,gate):
        self.signVector = gate(self.signVector)                                                         # This applies a gate to the hadamard representation.


    def __str__(self):
        """TODO: allows hadamard class to be printed nicely."""
        power = m.log2(len(self.signVector))
        sqrt2 = ""
        if power%2 == 1:
            sqrt2 = "√2"
        output = f"1/{int(2**(power//2))}{sqrt2}("
        for i in range(self.qR.d):
            if self.signVector[i] < 0:
                output += f"-{self.qbitVector[i]}"
            else:
                output += f"+{self.qbitVector[i]}"
        return output+")"




# Testing # --------------------------------------------------------------------

#test = hadamardInterpretation(qs.Register((1, 9)))
#print()
#print(test)
#print()
