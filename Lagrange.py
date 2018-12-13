import numpy as np
def Lagrange(x, y, value):
    '''Computes the Lagrange Polynomial

        Args: 
            x: input values x0, x1, ..., xn
            y: output values for a given x, i.e., f(x)
            value: value to be interpolated 
                by the Lagrange Polynomial

        Returns:
            Value of the Lagrange Polynomial 
            that interpolates the function 
            in the input value
    '''
    n = len(x) #grau do polinomio
    L = np.ones(n) #cria um vetor com os valores Lk
    for k in range(n):
    	#inicia um vetor com os termos multiplicados
        s1 = np.array([])
        s2 = np.array([])
        #elementos do numerador e do denominador
        for j in range(n):
            if j == k:
                continue
            s1 = np.append(s1, value - x[j])
            s2 = np.append(s2, x[k] - x[j])
        L[k] = np.prod(s1)/np.prod(s2)
    return sum(y*L)

#para grau 1
x1 = np.array([0.1, 0.6])
y1 = np.array([1.221, 3.32])
Lagrange(x1, y1, 0.2)

#para grau 2
x = np.array([0.1, 0.6, 0.8])
y = np.array([1.221, 3.32, 4.953])
Lagrange(x, y, 0.2)