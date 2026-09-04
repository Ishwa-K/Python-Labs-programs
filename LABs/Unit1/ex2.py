#Read two numbers and demonstrate arithmetic, relational, logical, and assignment operators.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operators
print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Relational Operators
print("\nRelational Operators")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)

# Logical Operators
print("\nLogical Operators")
print("(a > 0 and b > 0):", a > 0 and b > 0)
print("(a > 0 or b > 0):", a > 0 or b > 0)
print("not(a > 0):", not(a > 0))

# Assignment Operators
print("\nAssignment Operators")
x = a
print("x =", x)

x += b
print("x += b:", x)

x -= b
print("x -= b:", x)

x *= b
print("x *= b:", x)