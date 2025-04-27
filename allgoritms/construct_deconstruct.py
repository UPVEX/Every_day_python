# در این سوال ابتداز کاربر یک استرینگ گرفته و سپس ان را از نوع میسازیم و بعد مجددا ان را از هم میپاچیم


def construct_deconstruct(input_str):
    result = []
    length = len(input_str)

    # ایجاد رشته به حرف به حرف
    for i in range(1, length + 1):
        result.append(input_str[:i])

    # گسستن رشته به حرف به حرف
    for i in range(length - 1, 0, -1):
        result.append(input_str[:i])

    return result


user_input = input("please enter your text : ")
print(construct_deconstruct(user_input))