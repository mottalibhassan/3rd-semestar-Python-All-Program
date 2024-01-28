# Input a character
char = input("Enter a character: ")

# Check if the character is a vowel
if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"The character '{char}' is a vowel.")
else:
    print(f"The character '{char}' is not a vowel.")