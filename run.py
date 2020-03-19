import grovers as gr

n = 50000

s = int(input('\n' + "which state are you looking for?: "))
nq = int(input("number of qubits: "))

#Run Grover's algorithm for the given parameters
R, Dt = gr.Grovers(nq, s, True, True)

#Simulate the measurement of the System, AS IF you run Grover's each time
success_rate = gr.Observe_System(R, n, nq)/n
print(f"success rate = {success_rate}")
