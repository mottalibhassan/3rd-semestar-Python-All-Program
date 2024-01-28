# Input an array
array = input("Enter elements of the array (space-separated): ").split()

# Convert the elements to integers
array = [int(element) for element in array]

# Input the element to delete
element_to_delete = int(input("Enter the element to delete: "))

# Check if the element is in the array before deleting
if element_to_delete in array:
    # Delete the element from the array
    array.remove(element_to_delete)
    print(f"{element_to_delete} deleted from the array.")
    print("Updated Array:", array)
else:
    print(f"{element_to_delete} is not in the array.")
