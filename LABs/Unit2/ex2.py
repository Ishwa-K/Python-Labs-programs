def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


num = int(input("Enter a number: "))

if check_prime(num):
    print("The number is Prime")
else:
    print("The number is Not Prime")

print("Factorial =", factorial(num))