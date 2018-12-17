def simpson(x, f, n = 2):
    
    '''x = [x_inferior, x_superior] vetor 
       com os limites inferior e superior da integral
       f: a função previamente definida
       n: grau do polinômio usado para interpolar f(x), 
       definido, por padrão, como 2,
       isto é, usando a regra 1/3;
       para a regra 3/8, usa-se n = 3
    '''
    if n == 3:
        h = (x[-1] - x[0])/3
        
        x1 = x[0] + h 
        x2 = x1 + h
        
        return (3*h/8)*(f(x[0]) + 3*f(x1) + 3*f(x2) + f(x[-1]))
    
    else:
        h = (x[-1] - x[0])/2
        x1 = x[0] + h

        return (h/3)*(f(x[0]) + 4*f(x1) + f(x[-1]))