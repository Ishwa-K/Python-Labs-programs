#Generate the Fibonacci series using a recursive function, as specified in the Unit II laboratory practice.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")