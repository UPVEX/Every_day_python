# این برنامه هر عددی که بگیرد را به توان دو میرساند و به هم متصل میکند
# اگر ورودی 21 باشد خروجی مییشود 41
# 123 --> 149






def square_digits(number):
    
    digits = str(number)
    
    squared_digits = []
    
    
    for digit in digits:
        squared_digits.append(str(int(digit) ** 2))
    
    
    result = int(''.join(squared_digits))
    
    return result


print(square_digits(9119))  # result : 811181
print(square_digits(765))   # result : 493625
