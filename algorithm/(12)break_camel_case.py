# این برنامه ورودی کمل کیس رو تجزیه میکنه



def break_camel_case(s):
    result = ''

    for i, char in enumerate(s):

        if char.isupper() and i > 0:
            result += ' ' + char

        else:
            result += char

    return result

user_input = input("enter your sentence : ")

print(break_camel_case(user_input))