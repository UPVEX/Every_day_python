# codewars challenge
# https://www.codewars.com/kata/530e15517bc88ac656000716



def rot13(text):
    result = ''
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to lowercase for simplicity
            char_lower = char.lower()
            # Get the ASCII code of the character
            ascii_code = ord(char_lower)
            # Rotate the character by 13 positions
            rotated_ascii_code = (ascii_code - 97 + 13) % 26 + 97 if char_lower.islower() else (ascii_code - 65 + 13) % 26 + 65
            # Append the rotated character to the result
            result += chr(rotated_ascii_code) if char.islower() else chr(rotated_ascii_code).upper()
        else:
            # If the character is not a letter, append it unchanged
            result += char
    return result

# Example usage
text = "ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet."
encrypted_text = rot13(text)
print(encrypted_text)
