# این برنامه یه لیست از اعداد از کاربر گرفته و ان هارا از بزرگ به کوچک مرتب میکند


def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                # جابجایی عنصرها اگر نیاز باشد
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers

# نمونه ورودی و فراخوانی تابع
user_input = input("please enter your number list by using space : ")
input_list = [int(num) for num in user_input.split()]
sorted_list = bubble_sort(input_list)

# نمایش خروجی
print(sorted_list)
