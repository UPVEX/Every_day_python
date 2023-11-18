#این برنامه از کاربر ثانیه میگیره و اون رو به روز و ساعت و دقسقه تبدیل میکنه 


def conversion(seconds):
    # محاسبه تعداد روزها
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    
    # محاسبه تعداد ساعت‌ها
    hours = seconds // 3600
    seconds %= 3600
    
    # محاسبه تعداد دقیقه‌ها
    minutes = seconds // 60
    seconds %= 60
    
    # بازگرداندن نتیجه به صورت رشته
    return f"{days}-day {hours}-hour {minutes}-min {seconds}-second"


input_second = int(input("please enter a second : "))
print(conversion(input_second)) 