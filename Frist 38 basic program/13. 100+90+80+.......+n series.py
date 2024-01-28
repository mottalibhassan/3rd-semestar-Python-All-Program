n = int(input("Enter a positive integer (n): "))

# Initialize the sum
sum_series = 0

# Use a for loop to subtract multiples of 10 from 100 down to n
for i in range(100, n - 1, -10):
    sum_series += i

# Print the result
print(f"The sum of the series 100+90+80+...+{n} is: {sum_series}")