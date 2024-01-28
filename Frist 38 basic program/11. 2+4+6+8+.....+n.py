n = int(input("Enter a positive even integer (n): "))

# Initialize the sum
sum_series = 0

# Use a for loop to add even numbers up to n
for i in range(2, n + 1, 2):
    sum_series += i

# Print the result
print(f"The sum of the series 2+4+6+...+{n} is: {sum_series}")