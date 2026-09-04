#Create a menu-driven calculator and calculate the area of common geometric shapes using input and conditional statements.
print("MENU DRIVEN PROGRAM")

print("\n1. Calculator")
print("2. Area of Circle")
print("3. Area of Rectangle")
print("4. Area of Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    op = int(input("Enter operation: "))

    if op == 1:
        print("Result =", a + b)
    elif op == 2:
        print("Result =", a - b)
    elif op == 3:
        print("Result =", a * b)
    elif op == 4:
        print("Result =", a / b)
    else:
        print("Invalid operation")

elif choice == 2:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of Circle =", area)

elif choice == 3:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)

elif choice == 4:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

else:
    print("Invalid choice")