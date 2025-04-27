#این برنامه یک تکست از کابر میگیرد و تعداد حروف الفبا و  اعداد رو بر میگرداند


def count_letters_and_numbers(text):
    
    count_letters = 0
    count_numbers = 0

    
    for char in text:
        
        if char.isalpha():
            count_letters += 1
        
        elif char.isdigit():
            count_numbers += 1

    
    return count_letters, count_numbers


user_input = input("enter a text ==> ")


letters, numbers = count_letters_and_numbers(user_input)
print("alphabet: ", letters)
print("numbers ", numbers)
