import sys

def stair_on_level(total, level_number):
    return " " * (total - level_number)  + "#" * level_number 

levels_count = int(sys.argv[1])

for i in range(levels_count):
    print(stair_on_level(levels_count, i+1))
