import random

def randcatch():
    num_set = set()
    while True:
        num = random.randint(1,10)
        print("generated number = {}".format(num))
        if num in num_set:
            break
        else:
            num_set.add(num)
    return len(num_set) + 1

print(randcatch())