import random
import math
import sys
import statistics

arrsize = int(input('Enter size'))
print(arrsize)
numbers = []

for _ in range(arrsize):
    numbers.append(random.randrange(100))

print(numbers)

def median(array):
    array.sort()
    size = len(array)
    mid = None
    if size % 2 == 1:
      mid = array[size // 2]
    else:
      s = sum(array[size // 2 -1:size //2 + 1])         
      mid = s / 2
    print('Sorted')
    print(array)
    return mid

print(median(numbers))
print(statistics.median(numbers))
