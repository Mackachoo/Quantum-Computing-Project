import grovers as gr

n = 1000

s = int(input('\n' + "which state are you looking for?: "))
nq = int(input("number of qubits: "))

#Run Grover's algorithm for the given parameters
R = gr.Grovers(nq, s)
#Simulate the measurement of the System, AS IF you run Grover's each time
gr.Observe_System(R, n, nq)
