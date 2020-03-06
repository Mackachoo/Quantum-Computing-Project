import numpy as np
import quantum_states as qs
import math as m
import operations as op 


"""
This runs a quantum register through a hadamard gate and then keeps it in the representation.

Representation :
    H = (1/√2ⁿ)*Σ registers[i]
      = fⁿ(signVector ᛫ qbitVector)
      
        where (1/√2ⁿ) is the normalisation factor fⁿ.


"""

gates = {

    'H' : 1/m.sqrt(2)*np.array([[1,1],
                               [1,-1]]),
    'I' : np.identity(2),
    'X' : np.array([[0,1],
                   [1,0]]),
    'Y' : np.array([[0,-1j],
                   [1j,0]]),
    'Z' : np.array([[1,0],
                   [0,-1]])

}


class state():

    def __init__(self,input):
        self.qR = input                                                                                 # Stores the input quantum register.

        self.signVector = self.qR.vec                                                                   # This creates the signVector by calling vectorRepresentation().
        self.qbitVector = np.array([qs.Register((i,self.qR.values[1])) for i in range(self.qR.d)])      # This creates a array of the form [|0>,|1>,|2>,...,|2^(dimension)>].

    
    def constructGate(self,code):
        matrix = np.array([[1]])
        TofN = 0
        for char in code:
            if char.isdigit():
                TofN = int(char)
            elif TofN != 0:
                Tof = np.identity(2**TofN)
                gate = gates[char]
                for x in range(len(gates)):
                    for y in range(len(gates)):
                        Tof[len(Tof)-len(gate)+x%len(gate)][len(Tof)-len(gate)+y%len(gate)] = gate[x%len(gate)][y%len(gate)]
                matrix = op.kroneckerProduct(matrix,Tof)
                TofN = 0
            else:
                matrix = op.kroneckerProduct(matrix,gates[char])
        return matrix


    def applyGate(self,code):
        self.signVector = op.vecMatProduct(self.constructGate(code),self.signVector)


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

test = state(qs.Register((0,6)))
test.applyGate("HHHHHH")
print()
print(test)
print()
