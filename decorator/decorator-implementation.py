
# decleration
import time


def myDecorator(func):
    def myWrapper():
        print('before Implementation')
        func()
        print('after Implementation')
    
    return myWrapper


@myDecorator
def doSomeThing():
    print('I am in Process Now')
    time.sleep(2)
    print('huh! I am finished')

# excusion
    
doSomeThing()