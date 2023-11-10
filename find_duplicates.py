# در این برنامه از کاربر یک لیست از اعداد میگیریم و اعداد تکراری را برمیگردانیم

def find_duplicates(input_numbers):

    seen_numbers = set()
    duplicates = set()

    for number in input_numbers:

        if number in seen_numbers:
            duplicates.add(number)

        else:
            seen_numbers.add(number)
    
    return duplicates


user_input = input("please enter the number by using SPACE buttom ==> ")
input_numbers = [int(num) for num in user_input.split()]

print("the dupliacates numbers are ==> ", find_duplicates(input_numbers))

    