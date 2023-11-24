# این برنامه از کاربر یک ورودی دریافت میکنه و ان رو به رمز تبدیل میکنه
# در واقع کد یونیدکد هر کارکتر رو سه واحد زیاد کرده و در خروجی چاپ میکند



def unintelligible_password(s):

    result = ''

    for char in s:
        result += chr(ord(char) + 3)
        
    return result


user_input = input("please enter your string to recive your password : ")

print("your password is ==> ", unintelligible_password(user_input))  