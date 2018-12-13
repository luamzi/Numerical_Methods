def linear_interpol(x, y, value):
    '''Computes the Linear Interpolation 
        of a function in a given value
        
        Args:
            x: input array
            y: value of the function in x, i.e., f(x)
            value: value to be interpolated
        
        Returns: 
            The Linear Interpolation of the function
            in the given value
    '''
    return ((y[1]-y[0])/(x[1]-x[0]))*(value-x[0]) + y[0]   