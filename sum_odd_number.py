#این مسئله به شما می‌گوید که یک عدد صحیح مثبت را به عنوان ورودی دریافت کنید و سپس مجموع تمام اعداد فردی
# (اعدادی که بر 2 قابل قسمت نیستند) از 1 تا آن عدد را محاسبه کنید و برگردانید



def sum_odd_number(x):

    total = 0

    for i in range(1,x+1,2):
        print (i)
        total = total + i

    return total

x = int(input("enter your number -> "))

print("sum of odd number is -> ", sum_odd_number(x))
