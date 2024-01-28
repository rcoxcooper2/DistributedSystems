def prime_num(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

for num in range(3, 101):
    if prime_num(num):
        print(num)