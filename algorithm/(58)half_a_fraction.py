#


from fractions import Fraction

def half_a_fraction(fraction_str):

    # تبدیل رشته به شیء کسر
    fraction = Fraction(fraction_str)
    
    # نصف کردن کسر
    half_fraction = fraction / 2
    
    # تبدیل نتیجه به رشته
    result_str = str(half_fraction)
    
    return result_str



user_input = input("please enter your kasr like thise (1/3) ==> ")

result = half_a_fraction(user_input)

print("result for ", user_input, " is ==> ", result)
