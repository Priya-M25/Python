''' Recursive factorial where return type is list
Output -
n=5
120
'''
from typing import List

def factorialNumbers(n: int) -> List[int]:
    if n == 0:
        return [1]
    last = factorialNumbers(n - 1)
    factorial = last[-1] * n
    return [factorial]
n = int(input('n='))
result = factorialNumbers(n)
print(*result)

#----------------------------------------------------------
''' Recursive factorial where return type is int
Output -
n=7
5040
'''
from typing import List

def factorialNumbers(n: int) -> int:
    if n == 0:
        return 1
    return factorialNumbers(n-1) * n
n = int(input('n='))
result = factorialNumbers(n)
print(result)
