
def func2():
    return '1'

def func(func):
    return func()


executando =  func(func2)
print(executando)