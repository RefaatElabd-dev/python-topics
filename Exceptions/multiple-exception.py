 #that working with python version >= 3.11
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()


# calculator problem
class Calculator:
    def power(self, n, p):
        if(n < 0 or p < 0):
            raise ValueError('n and p should be non-negative')
        res = 1
        for _ in range(p):
            res *= n
        return res

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   