# این برنامه از کاربر یک رشته میگیرد و فقط اعداد ان را بر میگرداند




def filter_list(lst):
    
    result = [x for x in lst if x.isdigit()]
    return result


user_input = input("enter your message and i fillter it for you ***be sure to use , between char*** : ")
lst = user_input.split(',')

result = filter_list(lst)

print(f"filter of ({user_input}) is --> {result}")
