# این برنامه اعداد فرد رو مرتب کرده ولی اعداد زوج در جایگاه خود باقی میمونه
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] => [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]



def sort_odd_numbers(arr):
    # جدا کردن اعداد فرد و مرتب سازی آنها
    odd_numbers = sorted([num for num in arr if num % 2 != 0])

    # جایگزینی اعداد فرد مرتب شده در آرایه اصلی
    result = [num if num % 2 == 0 else odd_numbers.pop(0) for num in arr]

    return result


user_input = input("please change numbers with (,) : ")
number_list = [int(x) for x in user_input.split(',')]
result = sort_odd_numbers(number_list)

print(f"the final result for {number_list} is --> {result}")
