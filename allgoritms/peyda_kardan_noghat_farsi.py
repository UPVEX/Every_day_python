# برنامه زیر تعداد نقاطجمله ورودی را بر میگرداند



def sum_dots(text: str) -> int:

    sum = 0

    for index, letter in enumerate(text):

        if letter in ['ب', 'ج', 'خ', 'ذ', 'ز', 'ض', 'ظ', 'غ', 'ف', 'ن']:
            sum += 1

        elif letter in ['ت', 'ق', 'ی']:
            
            if len(text) < index + 1:
                continue

            if (letter == 'ی' and (text[index - 1] not in ['', ' '] or text[index + 1] not in ['', ' '])):

                if text[index - 1] not in ['', ' '] and text[index + 1] in ['', ' ']:
                    continue

                if text[index + 1] not in ['', ' ']:
                    sum += 2
                continue

            else:
                sum += 2

        elif letter in ['پ', 'ث', 'چ', 'ژ', 'ش']:
            sum += 3

    return sum


print(sum_dots("به نام خدا"))
