def func(x):
    return 1/x

#utilizando a regra 1/3
round(simpson([1, 7], func), 4)

#utilizando a regra 3/8
round(simpson([1, 7], func, n=3), 4)