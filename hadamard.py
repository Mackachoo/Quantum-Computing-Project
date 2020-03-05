import numpy as np
import quantum_states as qs

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
        if len(qBinary) == 0:
            return vRep
        else:
            if qBinary[-1:] == 0:
                vR = np.concatenate((vRep,vRep))
            else:
                vR = np.concatenate((vRep,-vRep))
            return self.vectorRepresenation(qBinary[:-1],vR)
            

    def __str__(self):
        output = f"1/√{self.qR.d}(|{self.qbitVector[0]}>"
        for i in range(1,self.qR.d):
            if self.signVector[i] < 0:
                output += f"-{self.qbitVector[i]}"
            else:
                output += f"+{self.qbitVector[i]}"
        return output+")"


# Testing #

#test = hadamardInterpretation(qs.Register((1, 3)))
#print()
#print(test)
#print()
