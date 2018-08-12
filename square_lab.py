import sys
import math 

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

def discriminant(a,b,c):
    return b * b - 4 * a * c

def solution(a,b,c):
    d = discriminant(a,b,c)
    x1 = (-b + math.sqrt(d)) / 2 * a
    x2 = (-b - math.sqrt(d)) / 2 * a
    return [x1, x2]

def print_solution(roots):
    for root in roots:
        print(int(root))

print_solution(solution(a,b,c))