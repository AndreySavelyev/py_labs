import sys

def digitsum(string):
    sum = 0
    for i in string:
        sum += int(i)
    return sum

string = sys.argv[1]

print(digitsum(string))