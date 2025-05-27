# این برنامه یک ورودی از اعداد میگیره و ان رو به فرمت شماره تبدیل میکنه
# codewars challenge
# https://www.codewars.com/kata/525f50e3b73515a6db000b83



def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

user_input = input("Enter 10 digits (0-9) for the phone number: ")
user_numbers = [int(digit) for digit in user_input if digit.isdigit()]

if len(user_numbers) == 10:

    print("Generated phone number:", create_phone_number(user_numbers))
else:
    print("Invalid input. Please enter 10 digits.")