# این برنامه از کاربر یک عبارت میگیرد و ان را یکی در میان به بزرگ و کوچک تقسیم میکند



def modify_string(input_str):
    words = input_str.split()

    modified_words = []
    for word in words:
        modified_word = ''.join(
            char.upper() if idx % 2 == 0 else char.lower()
            for idx, char in enumerate(word)
        )
        modified_words.append(modified_word)

    result = ' '.join(modified_words)
    return result


user_input = input("enter your sentence : ")
result  = modify_string(user_input)
print(f"the result for {user_input} is --> {result}")