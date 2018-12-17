from math import log

def func2(x):
    return (x**3)*log(x)

round(repSimpson([1, 3], func2, m=4), 3)