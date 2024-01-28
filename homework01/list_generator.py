import random

integers = [random.randint(1,100) for _ in range(10)]

print("Current list of integers: ", integers)

for num in integers:
    if num % 2 == 0:
        print(num, "even")
    else:
        print(num, "odd")

