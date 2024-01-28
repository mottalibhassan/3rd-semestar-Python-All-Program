# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the maximum of the two numbers
max_num = max(num1, num2)

# Initialize the LCM to the larger number
lcm = max_num

# Check for LCM
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max_num

# Print the result
print(f"The LCM of {num1} and {num2} is: {lcm}")
