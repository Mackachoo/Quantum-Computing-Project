import grovers as gr
import time
import numpy as np
import matplotlib.pyplot as plt

#Run for different sizes of registers and see how time scales for each algorithm f
def check_efficiency(f):
    """Short summary.

    Parameters
    ----------
    f : type
        Description of parameter `f`.

    Returns
    -------
    type
        Description of returned object.

    """
    s = 1
    Dt = []
    T = []
    nq = np.arange(9)+1
    print(nq)

    wr = open("Time_vs_N.txt","w")
    wr.write("N, Time taken for Grover's only, Total time taken (to construct gates and run Grover's)" + '\n')

    for n in nq:
        #Run Grover's algorithm for the given parameters
        start_time = time.time()
        R, t = f(n,s)
        T.append(t)
        Dt.append( time.time() - start_time)
        wr.write("%f %10.10f\n" % (t, time.time() - start_time))

    nq = 2**nq
    wr.close()
    plt.plot(nq, Dt)
    plt.plot(nq, T)
    plt.yscale('log')
    plt.show()

check_efficiency(gr.Grovers)
