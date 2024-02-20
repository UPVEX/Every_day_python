# برنامه زیر یک عدد میگیره و حاصل هر کدوم اون هارو حساب میکنه و اگه از 10 بیشتر بشه مجدد اینکارو میکنه
# codewars challenge
# https://www.codewars.com/kata/541c8630095125aba6000c00




def digital_root(n):
    
    digit_sum = sum(int(digit) for digit in str(n))
    
    while digit_sum >= 10:
        digit_sum = sum(int(digit) for digit in str(digit_sum))
    return digit_sum


user_input = input("Enter a non-negative integer: ")


if user_input.isdigit():

    user_number = int(user_input)
  
    print("Digital root:", digital_root(user_number))
else:
    print("Invalid input. Please enter a non-negative integer.")
