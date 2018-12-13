def dif_div(x, y, init, n):
    """Computes the divided difference of the 
        Newton Polynomial
    
        f[x0, ..., xn] = f[x1, ..., xn]/f[x0, ..., x(n-1)]
        
        Args:
            x: input values
            y: values of the function in x
            init: if f[x0,...,xn], then init=0 and so on
            n: maximum index
        
        Returns:
            The divided difference from x0 to xn        
    """
    if init != n:
        return (dif_div(x,y,init+1,n)-dif_div(x,y,init,n-1))/(x[n]-x[init])
    else:
        return y[init]

def newton_interpol(x, y, value):
    '''Computes the value of the Newton Polynomial
        that interpolates the function in a given value
        
        Args:
            x: input values
            y: values of the function in x
            value: value to be interpolated
            
        Returns:
            Estimate of the polynomial in the given value
    '''
    n = len(x)
    s = f[0]
    p = 1
    
    for i in range(1,n): #montar o polinômio
        p=1
        for j in range(0,i): #montar um termo do polinômio
            p = p*(value - x[j])
        s = s + dif_div(x, y, 0, i)*p
        
    return s