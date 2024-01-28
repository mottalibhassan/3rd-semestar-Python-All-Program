# Input an array
array = input("Enter elements of the array (space-separated): ").split()

# Convert the elements to integers
array = [int(element) for element in array]

# Reverse the array
reversed_array = array[::-1]

# Print the reversed array
print("Original Array:", array)
print("Reversed Array:", reversed_array)