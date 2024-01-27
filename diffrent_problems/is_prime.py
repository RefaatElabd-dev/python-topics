# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, ceil

def is_peime(n):
    if(n in set([2, 3, 5, 7])): # start looping after root(n) > 3 
        return True
    if n < 2 or n % 2 == 0: # remove looping on even numbers
        return False
    for i in range(3, ceil(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
    
number_of_lines = int(input())
for i in range(number_of_lines):
    number_to_check = int(input())
    print('Prime' if is_peime(number_to_check) else 'Not prime')
