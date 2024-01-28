# Input the number of terms
terms = int(input("Enter the number of Fibonacci terms: "))

# Check if the input is valid
if terms <= 0:
    print("Number of terms should be a positive integer.")
else:
    # Fibonacci series without using a separate function
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b
