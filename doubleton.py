# یک عدد طبیعی اگر دقیقاً دارای دو رقم متمایز باشد یک “عدد دوبلتون“ است. به عنوان مثال، 23، 35، 100، 12121 اعداد دابلتون هستند و 123 و 114455 نه.
# این برنامه از ورودی یک عدد گرفته و برسی میکند که ایادابلتون هست یا نه و عدد دابلتون بعدی ان را نمایش میدهد


def is_doubleton(num):
    # تابع برای بررسی اینکه یک عدد دابلتون است یا نه
    
    return len(set(str(num))) == 2  #set فقط داده های خاص و یکتا رو در خودش ضخیره میکنه 

def doubleton(n):
    # پیدا کردن عدد دابلتون بعدی پس از n
    next_number = n + 1
    while not is_doubleton(next_number):
        next_number += 1
    return next_number


user_input = int(input("please enter your number: "))

if is_doubleton(user_input):
    print("your number is doubleton and the next doubleton is ==> ", doubleton(user_input))

else:
    print("next doubleton number is ==> ", doubleton(user_input))