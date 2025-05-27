#یک رشته از کاربر دریافت کنید و سپس تابعی بنویسید که بررسی کند آیا این رشته
#یک پالیندرم (کلمه‌ای است که از ابتدا به انتها و از انتها به ابتدا یکسان باشد) است یا خیر. 
#خروجی تابع باید True یا False باشد.


def is_palindrome(input_string):

    cleaned_string = input_string.replace(" ", "").lower()

    return cleaned_string == cleaned_string[::-1]


user_input = input("please enter an str ==> ")


result = is_palindrome(user_input)

if result:
    print(user_input , " is palindrome")
    
else:
    print(user_input , " is not palindrome")
