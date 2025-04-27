# این برنامه یک عبارت از کاربر میگیرد و ان را به فورم کمل کیس بر میگرداند
# nima mollayi --> NimaMollayi


def to_camel_case(input_string):
    words = input_string.split()
    camel_case_words = [word.capitalize() for word in words]
    camel_case_string = ''.join(camel_case_words)
    return camel_case_string


user_input = input("enter your sentence to turn camel form : ")
result = to_camel_case(user_input)

print(f"the camel form of {user_input} is --> {result} ")