import numpy as np
import quantum_states as qs

"""
This runs a quantum register through a hadamard gate and then keeps it in the representation.

#TODO Could just make this a sub class of register in quantum states.

"""



class hadamardInterpretation():

    def __init__(self,qRegister):
        self.qR = qRegister

        self.signVector = self.vectorRepresenation(self.qR.bin, np.array([1],dtype=qs.Register))
        self.qbitVector = np.array([])

    def vectorRepresenation(self,qBinary,vRep):
        if len(qBinary) == 0:
            return vRep
        else:
            if qBinary[-1:] == 0:
                vR = np.concatenate((vRep,vRep))
            else:
                vR = np.concatenate((vRep,-vRep))
            return self.vectorRepresenation(qBinary[:-1],vR)


    def __str__(self):
        output = f"1/√{self.qR.d}(|0>"
        for i in range(1,self.qR.d):
            if self.signVector[i] < 0:
                output += f"-|{i}>"
            else:
                output += f"+|{i}>"
        return output+")"


# Testing #

test = hadamardInterpretation(qs.Register((1, 3)))
print(test)