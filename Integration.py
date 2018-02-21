def anonymous(x):
    return x**2 + 1

def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        """ your work here """
        area += step * fun(integrate)
    return area

print(round(integrate(anonymous, 0, 10)))