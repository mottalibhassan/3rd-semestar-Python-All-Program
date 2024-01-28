# Input a number
number = int(input("Enter a number: "))

# Print the multiplication table
print(f"Multiplication Table of {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")