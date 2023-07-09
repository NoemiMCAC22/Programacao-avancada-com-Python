import math
import random

N = 25
e = 0.000001
r= random.uniform(1, N)

while(not( N-e <= r*r <= N+e)):
    r = (r+N/r)/2

print("A raiz quadrada de", N, " é: ", r)