import numpy as np
def repSimpson(x, f, m):
    
    '''
        x = [x0, xm]
        f: funcao previamente definida
    '''
    
    h = (x[-1] - x[0])/m 
    
    #construção dos x's intermediários
    X = np.array([x[0]])
    for i in range(1, m):
        X = np.append(X, X[i-1]+h)
    X = np.append(X, x[-1])
    
    #construção de vetor de (ci)*(yi)
    y = np.array([])
    for i in range(len(X)):
        if i == 0 or i == m:
            y = np.append(y, 1*f(X[i]))
        elif i%2 == 0: #se i for par
            y = np.append(y, 2*f(X[i]))
        else: #se i for ímpar
            y = np.append(y, 4*f(X[i]))
    
    
    return (h/3)*sum(y)