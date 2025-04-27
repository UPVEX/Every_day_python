# این برنامه از کاربر  یه ورودی میگیرد و اولین حرفی که در  کل جمله تکرار نشده باشد رو بر میگرداند



def first_non_repeating_letter(s):
    s_lower = s.lower()
    result = False
    for char in s:
        count = s_lower.count(char.lower())
        if count == 1:
            result = True
            return char, result
    return '', result

user_input = input("please enter a sentece or word --> ")
input_result, result = first_non_repeating_letter(user_input)


if result == True:
    print(f"the result for {user_input} is --> {input_result}")
else:
    print("nothing")