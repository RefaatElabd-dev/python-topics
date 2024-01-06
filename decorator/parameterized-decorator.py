#declaration

def parameterizedDecorator(func):
    def parameterizedWrapper(*args, **kwargs):
        print('before implementation')
        func(*args, **kwargs)
        print('after Implementation')
    
    return parameterizedWrapper

@parameterizedDecorator
def generateTextNTimes(text, n):
    for i in range(n):
        print(text)

# implementation
        
generateTextNTimes('I will be great one day', 5)