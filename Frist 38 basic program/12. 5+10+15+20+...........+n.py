n = int(input("Enter a positive integer (n): "))

# Initialize the sum
sum_series = 0

# Use a for loop to add multiples of 5 up to n
for i in range(5, n + 1, 5):
    sum_series += i

# Print the result
print(f"The sum of the series 5+10+15+...+{n} is: {sum_series}")
