num_terms = int(input("Enter the number of terms for Fibonacci series: "))

a, b = 0, 1
print("Fibonacci Series:")
for _ in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b