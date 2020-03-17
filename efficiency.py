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
    DtS = []
    T = []
    nq = np.arange(7)+1
    print(nq)

    wr = open("Time_vs_N.txt","w")
    wr.write("N, Time taken for Grover's only, Total time taken (to construct gates and run Grover's)" + '\n')

    for n in nq:
        #Run Grover's algorithm for the given parameters
        print(f"Running Grover's, {int(np.pi/(4*np.arcsin(1/np.sqrt(2**n))))} times:")
        start_time = time.time()
        R, t = f(n,s,False)
        T.append(t)
        Dt.append( time.time() - start_time)

        start_time = time.time()
        R, t = f(n,s,False,True)
        T.append(t)
        DtS.append( time.time() - start_time)
        wr.write("%f %10.10f\n" % (t, time.time() - start_time))

    nq = 2**nq
    wr.close()
    plt.plot(nq, Dt, label="Not Sparse")
    plt.plot(nq, DtS, label="Sparse")
    #plt.plot(nq, T)
    plt.legend()
    plt.yscale('log')
    plt.show()

check_efficiency(gr.Grovers)
