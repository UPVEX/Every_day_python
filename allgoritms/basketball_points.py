# این برنامه از کاربر تعداد ضربات دو امتیازی و سه امتیازی در بازیبسکتبال را میگیرد و امتیاز کل رو بر میگرداند




def points(two_pointers, three_pointers):

    # محاسبه امتیازات نهایی بر اساس تعداد پرتاب های 2 امتیازی و 3 امتیازی
    total_points = (2 * two_pointers) + (3 * three_pointers)
    
    return total_points

user_input_two = int(input("please enter how many 2 point you scored :"))
user_input_three = int(input("please enter how many 3 point you scored :"))

result = points(user_input_two, user_input_three)
print("your score is : ", result)