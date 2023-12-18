# این برنامه از کاربر یک یک عدد میگیرد و گسترده ان را برمیگرداند



def expanded_form(num):

    number_string = str(num)

    count = len(number_string)

    expanded_numbers = []

    for i, n in enumerate(number_string):

        if n == '0':
            continue
        
        else:
            expand_number = int(n) * (10 ** (count - i - 1)) 

            expanded_numbers.append(str(expand_number))
    
    result = ' + '.join(expanded_numbers)
    return result


user_input = input("enter a number to expand : ")
result = expanded_form(user_input)

print(f"the expanded form for {user_input} is --> {result}")