# این برنامه یک لیست اعداد از کاربر میگیرد و بزرگترین و کوچکترین ان را نمایش میدهد

def find_max_min(numbers):
    
    if not numbers:
        return None, None

    maxi = mini = numbers[0]

    for number in numbers:

        if number > maxi:
            maxi = number

        elif number < mini:
            mini = number

    return maxi, mini
      

user_input = input("please enter your number by using SPACE buttom ==> ")
numbers = [int(num) for num in user_input.split()]


max_num, min_num = find_max_min(numbers) 

if max_num is not None and min_num is not None:
    print("the max number is ==> ",max_num, "  and the min number is ==> ", min_num)

else:
    print("you must enter your numbers correctly first")
