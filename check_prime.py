num = int(input("a number: "))

def is_prime(num):
    result = 0
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            result = 1
    if result == 0:
        print("Prime")

is_prime(num)