
#این برنامه تعداد نقاط جمله ای که شما به فارسی وارد میکنید رو حساب میکنه و در خروجی چاپ میکنه

def sum_dots(text: str) -> int:
    total_dots = 0
    for index, letter in enumerate(text):
        if letter in ['ب', 'ج', 'خ', 'ذ', 'ز', 'ض', 'ظ', 'غ', 'ف', 'ن']:
            total_dots += 1
        elif letter in ['ت', 'ق', 'ی']:
            if len(text) <= index + 1:
                continue
            if (letter == 'ی' and (text[index - 1] not in ['', ' '] or text[index + 1] not in ['', ' '])):
                if text[index - 1] not in ['', ' '] and text[index + 1] in ['', ' ']:
                    continue
                if text[index + 1] not in ['', ' ']:
                    total_dots += 2
                continue
            else:
                total_dots += 2
        elif letter in ['پ', 'ث', 'چ', 'ژ', 'ش']:
            total_dots += 3
    return total_dots

user_input = input("enter a persian sentense please : ")
dots_count = sum_dots(user_input)
print(f"the number of dots is : {dots_count}")

