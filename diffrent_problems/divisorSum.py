class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
import math

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n == 0:
            return 0
        divisors = {1, n}
        biggest_divisor = math.ceil(math.sqrt(n))
        for i in range(2, biggest_divisor + 1, 1):
            if n % i == 0:
                divisors.update({i, n/i})
        return int(sum(divisors))
                


n = int(input('enter a number: '))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)