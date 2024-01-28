# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the minimum of the two numbers
min_num = min(num1, num2)

# Initialize the GCD to the smaller number
gcd = min_num

# Check for GCD
while gcd > 1:
    if num1 % gcd == 0 and num2 % gcd == 0:
        break
    gcd -= 1

# Print the result
print(f"The GCD of {num1} and {num2} is: {gcd}")
