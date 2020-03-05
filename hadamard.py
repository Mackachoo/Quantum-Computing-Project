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
        self.qR = qRegister

        self.signVector = self.vectorRepresenation(self.qR.bin, np.array([1]))
        self.qbitVector = np.array([qs.Register((i,self.qR.values[1])) for i in range(self.qR.d)])


    def vectorRepresenation(self,qBinary,vRep):
        """This is for and only for the initilizing function to create the signVector."""
        if len(qBinary) == 0:
            return vRep
        else:
            if qBinary[-1:] == 0:
                vR = np.concatenate((vRep,vRep))
            else:
                vR = np.concatenate((vRep,-vRep))
            return self.vectorRepresenation(qBinary[:-1],vR)

    
    def applyGate(self,gate):
        self.signVector = gate(self.signVector)


    def __str__(self):
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

test = hadamardInterpretation(qs.Register((1, 9)))
print()
print(test)
print()
