import numpy as np
def repTrapezoid(f, x):
    '''Computes the Trapezoid rule
        for m divisions
        
    Args:
        f: function values for each x
        x: [x0, ..., xm] input values
    
    '''
    m = len(x)-1
    x = np.array(x)
    h = (x[m] - x[0])/m
    f = np.array(f)
    
    return (h/2)*(f[0] + 2*sum(f[:m]) + f[m])