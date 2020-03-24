import grovers as gr
import time
import numpy as np
import matplotlib.pyplot as plt

#Run for different sizes of registers and see how time scales for each algorithm f

def writeData(n, f, file):
    s = 1
    Dt = []
    DtS = []
    nq = np.arange(n)+1

    store = open(file, 'a')
    store.write(str(nq))
    store.close()

    for n in nq:
        #Run Grover's algorithm for the given parameters
        print(f"Running Grover's, {int(np.pi/(4*np.arcsin(1/np.sqrt(2**n))))} times:")
        start_time = time.time()
        R, t = f(n,s,False)
        Dt.append( time.time() - start_time)
        store = open(file, 'a')
        store.write(f"\n\n{Dt}")
        store.close()

        start_time = time.time()
        R, t = f(n,s,False,True)
        DtS.append( time.time() - start_time)
        store = open(file, 'a')
        store.write(f"\n{DtS}")
        store.close()


def getData(file):
    f = open(file, 'r')
    d = f.read()
    f.close()
    data = d.split('\n')

    nq = np.array([float(a) for a in (data[0])[1:-1].split(' ')])
    Dt = np.array([float(a) for a in (data[1])[1:-1].split(', ')])
    DtS = np.array([float(a) for a in (data[2])[1:-1].split(', ')])
    print(f"{nq}\n{Dt}\n{DtS}")
    return nq, Dt, DtS


def check_efficiency(data):
    """Short summary.


    Parameters
    ----------
    f : str
        String for filename with data.

    Returns
    -------
    type
        Description of returned object.

    """
    
    nq, Dt, DtS = data
    fig = plt.figure()
    dd = fig.add_subplot(111)
    #f1 = fig.add_subplot(311)
    #f2 = fig.add_subplot(323)
    #f3 = fig.add_subplot(324)
    #f4 = fig.add_subplot(325)
    #f5 = fig.add_subplot(326)

    #nq = 2**np.array(nq)

    dd.set_title("Log of Time vs qbits per state for Sparse and Non Sparse Method")
    dd.plot(nq, Dt*1000, label="Non-Sparse Method")
    dd.plot(nq, DtS*1000, label="Sparse Method")
    dd.legend()
    dd.set_yscale('log')
    dd.set_xlabel("Qbits in Register")
    dd.set_ylabel("Log of Time")
    dd.set_ylim((0,max(abs(Dt*1000))))


    plt.show()

    
    """
    f1.set_title("Time Difference")
    f1.plot(nq, abs(np.array(Dt)-np.array(DtS))*1000, label="Not Sparse")
    f1.set_yscale('log')
    f1.set_xlabel("qbits per state")
    f1.set_ylabel("Time (ms)")
    f1.set_ylim((0,max(abs(np.array(Dt)-np.array(DtS))*1000)))

    f2.set_title("Non Sparse Log Time")
    f2.plot(nq, Dt*1000, label="Not Sparse")
    f2.set_yscale('log')
    f2.set_xlabel("qbits per state")
    f2.set_ylabel("Time (ms)")
    f2.set_ylim((0,max(abs(Dt*1000))))

    f3.set_title("Sparse Log Time")
    f3.plot(nq, DtS*1000, label="Sparse")
    f3.set_yscale('log')
    f3.set_xlabel("qbits per state")
    f3.set_ylabel("Time (ms)")
    f3.set_ylim((0,max(DtS*1000)))

    f4.set_title("Non Sparse Time")
    f4.plot(nq, Dt*1000, label="Not Sparse")
    f4.set_xlabel("qbits per state")
    f4.set_ylabel("Time (ms)")
    f4.set_ylim((0,max(abs(Dt*1000))))

    f5.set_title("Sparse Time")
    f5.plot(nq, DtS*1000, label="Sparse")
    f5.set_xlabel("qbits per state")
    f5.set_ylabel("Time (ms)")
    f1.set_ylim((0,max(DtS*1000)))

    """

file = "data1.txt"

#writeData(50, gr.Grovers, file)
check_efficiency(getData(file))

