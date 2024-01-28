# Input an array
array = input("Enter elements of the array (space-separated): ").split()

# Convert the elements to integers
array = [int(element) for element in array]

# Input the element to insert
element_to_insert = int(input("Enter the element to insert: "))

# Input the position to insert the element
position = int(input(f"Enter the position to insert {element_to_insert} (1 to {len(array) + 1}): "))

# Insert the element into the array
array.insert(position - 1, element_to_insert)

# Print the updated array
print("Updated Array:", array)
