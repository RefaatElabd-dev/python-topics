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
    