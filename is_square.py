# این برنامه از کاربر یک عدد میگیرد و به کاربر میگه ایا عدد مربع است یا خیر 



def is_square(number):

    if number < 0:
        return False
    
    square_root = int(number ** 0.5)

    if square_root ** 2 == number:
        return True
    
    else:
        return False
    
user_input = int(input("please enter a number : "))

result = is_square(user_input)

if result:
    print(f"({user_input}) is a SQURE number")

else:
    print(f"({user_input}) its not a SQURE!!! ")