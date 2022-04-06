def func(func, *args, **kwargs):
    return func(*args, **kwargs)

def func3(n):
    return n

def func4(n1, n2):
    return n1, n2



    





print(func(func3, 'oi'))
print(func(func4, 'oi', 'opa'))