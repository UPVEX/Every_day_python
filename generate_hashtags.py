# این برنامه یک ورودی میگیردو ان را به یک هشتگ تبدیل میکند
# باید با هشتگ (#) شروع شود.
# تمام کلمات باید با حرف بزرگ شروع شوند.
# اگر نتیجه نهایی طولانی‌تر از ۱۴۰ کاراکتر باشد، باید مقدار false برگرداند.
# اگر ورودی یا نتیجه یک رشته خالی باشد، باید مقدار false برگرداند.




def generate_hashtag(s):

    if not s:
        return False
    
    hashtag = '#' + ''.join(word.capitalize() for word in s.split())
    
    if len(hashtag) > 140:
        return False
    
    return hashtag

user_input = str(input('enter your sentence hear --> '))
result = generate_hashtag(user_input)
print(result)
