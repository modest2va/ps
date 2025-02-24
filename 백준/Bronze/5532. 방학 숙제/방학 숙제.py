L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

import math

print(L-max(int(math.ceil(A/C)),int(math.ceil(B/D))))