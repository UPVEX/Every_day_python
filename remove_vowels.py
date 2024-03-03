# codewars challenge
# https://www.codewars.com/kata/52fba66badcd10859f00097e




def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result


input_text = input("enter your senteces --> ")
output_text = remove_vowels(input_text)
print(f"result for ({input_text}) is --> {output_text}")  
