# این برنامه یک ورودی از کاربر میگیرد و تمام اعداد فیبوناچی قبل از ان را نمایش میدهد 


def fibo_numbers(n):
    
    fibo_list =[]
    a, b = 0, 1

    while a <= n : 

        fibo_list.append(a)
        a, b = b, a+b

    return fibo_list


number = int(input("please enter your number ==> "))

print("the fibonachi number before ", number, " is ==> ", fibo_numbers(number))

