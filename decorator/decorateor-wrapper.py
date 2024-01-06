def decorator(func):
    def wrapper():
        print('before')
        func()
        print('after')
        
    return wrapper

def f2():
    print('Hello')

# that's how decorator works
decorator(f2)()





