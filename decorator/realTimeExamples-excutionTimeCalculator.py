import time

def calcExcutionTime(func):
    def wrapper():
        before = time.time()
        func()
        print(str(time.time() - before) + "seconds")
        
    return wrapper


@calcExcutionTime
def doSomeThing():
    print('I am in Process Now')
    time.sleep(2)
    print('huh! I am finished')

# excusion
    
doSomeThing()