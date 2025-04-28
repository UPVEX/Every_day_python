#این برنامه یک عدد از کاربر میگیرد و ان را به حروف نمایش میدهد. این برنامه تا یک میلیارد را جواب میدهد


def convert_to_words(num):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def convert_below_thousand(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + " " + convert_below_thousand(n % 10)
        else:
            return units[n // 100] + " Hundred " + convert_below_thousand(n % 100)

    if num == 0:
        return "Zero"
    result = ""
    if num >= 1000000000:
        result += convert_below_thousand(num // 1000000000) + " Billion "
        num %= 1000000000
    if num >= 1000000:
        result += convert_below_thousand(num // 1000000) + " Million "
        num %= 1000000
    if num >= 1000:
        result += convert_below_thousand(num // 1000) + " Thousand "
        num %= 1000
    result += convert_below_thousand(num)
    return result.strip()


number = int(input("Enter a number: "))
result = convert_to_words(number)
print(result)
