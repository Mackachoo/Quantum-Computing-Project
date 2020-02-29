from operations import kroneckerProduct, tensorProduct
from quantum_states import Qubit

R1 = Qubit((1,2))
R2 = Qubit((0,2))

print(R1)
print(R2)

T = tensorProduct(R1.vec, R2.vec)
print(T)
