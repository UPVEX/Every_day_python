#این برنامه از کاربر یه کلمه گرفته و ان را به صورت فردی که لکنت زبان دارد چاپ میکند



def stutter(word):
    if len(word) >= 2:
        stuttered_word = word[:2] + '... ' + word[:2] + '... ' + word + '?'
        return stuttered_word
    else:
        return "Word must have at least two letters."

# دریافت ورودی از کاربر
user_input = input("Enter a word: ")

# فراخوانی تابع و نمایش خروجی
result = stutter(user_input)
print(result)
