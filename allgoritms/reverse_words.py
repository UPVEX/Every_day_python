# برنامه زیر یک جمله از کاربر میگیرد و اگر کلمه ای بیش تر یا مساوی 5 کارکتر باشد ان را برعکس میکند 



def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] if len(word) >= 5 else word for word in words]
    return ' '.join(reversed_words)

user_input = input("please enter your sentence : ")

result = reverse_words(user_input)

print(f"the result for ( {user_input} ) is --> {result}")