class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass
# A class in an except clause is compatible with an exception if it is the same class or a base class thereof
#  (but not the other way around)
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")




for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")
    
def ret_bool():
    try:
        return True
    finally:
        return False
    
print(ret_bool()) # false

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
# result is 2
# executing finally clause


divide(2, 0)
# division by zero!
# executing finally clause

divide("2", "1")
# executing finally clause
# exception raised

# cleanup "with" keyword
# for line in open("myfile.txt"):
#     print(line, end="")
# that will leave the file opend for an indeterminate amount of time
# Do This
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
