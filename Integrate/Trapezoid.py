def trapezoid(f, x):
    '''Computes the value of the 
    Trapezoid Area as an aproximation 
    of an integral of a function
        
    Args:
         f: function to be integrated
         x: [x0, x1] lower and upper limits
    
    Returns:
        The area of a trapezoid between x0 and x1
    '''
    return ((x[1] - x[0])*(f(x[1]) + f(x[0])))/2

