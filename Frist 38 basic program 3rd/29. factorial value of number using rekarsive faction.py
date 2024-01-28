# Input a number
number = int(input("Enter a non-negative integer: "))

# Check if the number is non-negative
if number < 0:
    print("Factorial is undefined for negative numbers.")
else:
    # Calculate factorial without using a function
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i

    print(f"The factorial of {number} is: {factorial_result}")
