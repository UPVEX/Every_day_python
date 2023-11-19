# در این برنامه سه ورودی از کاربر میگیریم که یکی توان دهنده ماست و دو تا دیگری بازه ما هستند
# این برنامه برسی میکند چند عدد به توان ورودی ائل در بازه ما هستند و انها را نمایش میدهد


def power_range(n,a,b):

    count = 0
    list_number = []
    for i in range(1, b+1):

        if (((i ** n) >= a) and ((i ** n) <= b)):
            count = count + 1
            list_number.append(i)

    return count, list_number


n = int(input("please enter n: "))
a = int(input("please enter a: "))
b = int(input("please enter b: "))


counter, list_num = power_range(n, a, b)
print("the number in range of ", a, "--", b, "in the power of ", n, "are ", counter, " ==> ", list_num)
