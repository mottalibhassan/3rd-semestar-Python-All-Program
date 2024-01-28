# Menu for the user to choose conversion
print("Choose conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter choice (1 or 2): "))

# Perform the chosen conversion
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
else:
    print("Invalid choice. Please enter 1 or 2.")
