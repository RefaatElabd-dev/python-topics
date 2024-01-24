def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value)

x = simpleGeneratorFun()
print(next(x)) 
print(next(x)) 
print(next(x))