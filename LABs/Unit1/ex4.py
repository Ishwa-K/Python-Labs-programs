#A practical unit-conversion program using functions, input/output, and conditional selection.
print("===== UNIT CONVERTER =====")

print("\n1. Kilometres to Metres")
print("2. Metres to Kilometres")
print("3. Metres to Centimetres")
print("4. Centimetres to Metres")
print("5. Kilograms to Grams")
print("6. Grams to Kilograms")

choice = int(input("\nEnter your choice: "))
value = float(input("Enter value: "))

if choice == 1:
    result = value * 1000
    print("Result =", result, "metres")

elif choice == 2:
    result = value / 1000
    print("Result =", result, "kilometres")

elif choice == 3:
    result = value * 100
    print("Result =", result, "centimetres")

elif choice == 4:
    result = value / 100
    print("Result =", result, "metres")

elif choice == 5:
    result = value * 1000
    print("Result =", result, "grams")

elif choice == 6:
    result = value / 1000
    print("Result =", result, "kilograms")

else:
    print("Invalid choice")