# برنامه ماشین حساب پیشرته که یه عبارت ریاضی از کاربر گرفته و نتیجه رو بر میگردونه
#نکته:تابع evalورودی که کاربر میده رو به عنوان برنامه پایتونی اجرا میکنه 



import sympy

def calculate_expression(expression):
    try:
        result = eval(expression)
        return f"result {result}"
    except Exception as e:
        return f"ERORR {e}"

# گرفتن عبارت از کاربر
user_input = input("please enter your math structure")

# محاسبه و نمایش نتیجه
result = calculate_expression(user_input)
print(result)
