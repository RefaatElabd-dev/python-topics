def decoratorWithReturn(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    
    return wrapper

@decoratorWithReturn
def nonReturnedFunc():
    print('some implementation')

@decoratorWithReturn
def returnedFunc():
    print('some implementation')
    return 'I am your Response'

# excution
print(nonReturnedFunc())

print(returnedFunc())