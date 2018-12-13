def bisec(f, a, b, epsilon, maxIter = 100):
    #toma os valores de f(a) e f(b)
    Fa = f(a); Fb = f(b)

    if round(Fa, 2) == 0:
        return (False, a)
    elif round(Fb, 2) == 0:
        return (False, b)
    
    #testing the signal
    if Fa*Fb > 0:
        print('Erro: não há mudança de sinal no intervalo dado!')
        return (True, None)
    
    #initializes the initial range
    deltaX = abs(b - a)/2
    
    for i in range(1, maxIter+1):
        #takes x on the half of the interval or its value at the given point
        x = (a + b)/2; Fx = f(x)
        
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(i, a, Fa, b, Fb, x, Fx, deltaX))
        
        #criteria for stopping the algorithm
        if (deltaX <= epsilon) or (abs(Fx) <= epsilon):
            break
        
        #update the values of a or b by testing the signals
        if Fa*Fx > 0: #se f(a) e f(x) tiverem o mesmo sinal
            a = x; Fa = Fx
        else:
            b = x
        
        #update the range
        deltaX = deltaX/2
    
    #convergence test
    if deltaX <= epsilon or abs(Fx) <= epsilon:
        error = False
    else:
        error = True
    
    return (error, x)

def false_pos(f, a, b, epsilon, maxIter=100):
    Fa = f(a); Fb = f(b)
    
    #if a or b are roots
    if Fa == 0:
        return (False, a)
    elif Fb == 0:
        return (False, b)
    
    #testing the signal
    if Fa*Fb > 0:
        print('Erro: não há mudança de sinal no intervalo dado!')
        return (True, None)
    
    #making sure f(a) is the negative value
    if Fa > 0:
        aux = a; a = b; b = aux
        aux = Fa; Fa = Fb; Fb = aux
    
    for i in range(1, maxIter+1):
        x = (a*Fb - b*Fa)/(Fb - Fa); Fx = f(x)
        
        deltaX = abs(b - a)
        
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(i, a, Fa, b, Fb, x, Fx, deltaX))
        
        #criteria for stopping the algorithm
        if (deltaX <= epsilon) or (abs(Fx) <= epsilon):
            break
        
        #update the values of a, b, f(b) and f(a) based on the value of f(x)
        if Fx < 0:
            a = x; Fa = Fx
        else:
            b = x; Fb = Fx
    
    #convergence test
    if deltaX <= epsilon or abs(Fx) <= epsilon:
        error = False
    else:
        error = True
    
    return (error, x)

def mpf(f, iter_func, x0, epsilon, maxIter):
    
    #check if the criteria for stopping has been already achieved
    if abs(f(x0)) < epsilon:
        x = x0
        return (False, x)
    
    for k in range(1, maxIter+1):
        x = iter_func(x0)
        
        print('Iter        x                f(x)')
        print("%d\t%e\t%e"%(k, x, f(x)))
        print('-------------------------------------')
        
        if abs(f(x)) < epsilon:
            return (False, x)
        x0 = x
    
    return (True, None)

def newton_raphson(f, df, x0, epsilon, maxIter):
    
    #check if the criteria for stopping has been achieved
    if abs(f(x0)) < epsilon:
        x = x0
        return (False, x)
    
    for k in range(1, maxIter+1):
        x = x0 - (f(x0)/df(x0))
        
        print('Iter        x                f(x)')
        print("%d\t%e\t%e"%(k, x, f(x)))
        print('-------------------------------------')
        
        if abs(f(x)) < epsilon:
            return (False, x)
        x0 = x
    
    return (True, None)

def inc_search(f, a, b, dx):
    x1 = a
    f1 = f(a)
    x2 = a + dx
    f2 = f(x2)

    while f1*f2 >= 0:
        if x1 >= b:
            return (None,None)
        x1 = x2
        f1 = f2
        x2 = x1 + dx
        f2 = f(x2)
    else:
        return x1,x2

