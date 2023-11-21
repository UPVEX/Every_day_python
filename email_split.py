# این برنامه از کاربر یک ایمیل میگیرد و دامین و یوزرنیم ان را جدا میکند


def email_split(email):
    # جدا کردن قسمت username و domain
    username, domain = email.split('@')

    # ساخت یک دیکشنری با اطلاعات مربوط به username و domain
    result = {'username': username, 'domain': domain}

    return result



user_email = input("please enter your email address ==> ")

result = email_split(user_email)

print(result)
