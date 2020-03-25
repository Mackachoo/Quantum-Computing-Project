import grovers as gr

k = 10000

s = int(input('\n' + "Target state: "))
nq = int(input("number of qubits: "))

#Run Grover's algorithm for the given parameters
R, Dt = gr.Grovers(nq, s, True, True)

#Simulate the measurement of the System, AS IF you run Grover's each time
success_rate = gr.Observe_System(R, k, nq)
print(f"success rate = {success_rate}")
