# این برنامه از کاربر تعداد طبقات هرم را میگیرد و یک هرم با کارکتر * میسازد



def build_pyramid(num_floors):
    pyramid = []
    
    for floor in range(1, num_floors + 1):
        spaces = " " * (num_floors - floor)
        stars = "*" * (2 * floor - 1)
        row = spaces + stars + spaces
        pyramid.append(row)

    return pyramid


user_input = int(input("please enter your pyramid floors number : "))

result = build_pyramid(user_input)
for row in result:
    print(row)