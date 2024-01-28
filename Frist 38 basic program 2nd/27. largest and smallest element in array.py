# Input an array
array = input("Enter elements of the array (space-separated): ").split()

# Convert the elements to integers
array = [int(element) for element in array]

# Find the largest and smallest elements
largest_element = max(array)
smallest_element = min(array)

# Print the results
print("Array:", array)
print("Largest Element:", largest_element)
print("Smallest Element:", smallest_element)
