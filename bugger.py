# این برنامه یک عدد از کاربر گرفته و انقدر ارقام ان را با هم ضرب میکند تا  حاصل یک رقمی شود و در اخر تعداد دفعات ضرب را نمایش میدهد 



def bugger(num):
    # تعداد عملیات ضرب
    count = 0
    
    # تا زمانی که عدد بیش از یک رقمی است
    while num >= 10:
        # ضرب رقم‌های عدد با یکدیگر
        result = 1
        for digit in str(num):
            result *= int(digit)
        
        # به روزرسانی عدد با نتیجه ضرب
        num = result
        
        # افزایش تعداد عملیات ضرب
        count += 1
    
    return count


user_input = int(input("please enter a number : "))
result = bugger(user_input)

print(result)
