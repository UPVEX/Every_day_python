# این برنامه از کاربر یک جمله میگیرد و بزرگترین  کلمه رو برمیگرداند



def longest_word(sentence):
    words = sentence.split()

    if not words:
        return None  # اگر جمله حاوی هیچ کلمه‌ای نباشد

    # حذف کاراکترهای خاص از ابتدا و انتهای هر کلمه
    clean_words = [word.strip(".,!?") for word in words]

    # پیدا کردن طولانی‌ترین کلمه
    longest_word = max(clean_words, key=len)

    return longest_word

# گرقتن ورودی از کاربر

user_input = input("please enter your sentence : ")

result = longest_word(user_input)
print(result)


