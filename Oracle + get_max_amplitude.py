"""
This file is for the Oracle of the Grover's algorithm and for extracting 
the maximum amplitude and its corresponding state using the amplitudes list,
a list of all the amplitudes whose index corresponds to it's state.
Latest version 06/03/20
"""

def oracle(amplitudes, target):
    """
    This function takes the whole amplitudes list composed of potentially 
    several registers. The other input is the target, the state we want to find.
    
    The function flips the sign of the amplitude of the target state, 
    whilst preserving all others. 
    Finally, it returns the updated ampltidues after applying the oracle.
    """
    for i in range(len(amplitudes)):
        if i == target:
    
            # Recall numpy counts from 0 so correct this by 1.
            # Do this only if we call our first state 1 and not 0.
            amplitudes[i-1] = -amplitudes[i-1]
   
    return amplitudes
            

def get_max_amplitude(amplitudes):
    """
    This function takes in a list of amplitudes.
    It returns the maximum amplitude and its corresponding index (state).
    """
    state, max_amplitude = max(enumerate(amplitudes), key=(lambda x: x[1]))
    
    # Assuming that we start counting the first state as being 1. If not just return state 
    # without + 1 and take away - 1 in the previous function (oracle).
    return state + 1, max_amplitude
              

"""
Testing oracle function
"""      
  
target = 4   # Therefore should flip amplitude of state 4
states = [1, 2, 3, 4, 5]
amplitudes = [0.1, -0.4, 0, 0.3, 0.2]
k = oracle(amplitudes, target)

"""
Testing the maximum amplitude function
"""

m = get_max_amplitude(amplitudes, states)   
# Therefore should give (4, 0.3) if we did not test oracle first, if not (5, 0.2) 

