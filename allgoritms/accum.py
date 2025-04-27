# codewars challenge
# این برنامه الگو زیر را اجرا میکند
# nima --> N-Ii-Mmm-Aaaa



def accum(s):

    result = ""

    for i ,char in enumerate(s):

        result += char.upper() + char.lower() * i 

        if i < len(s) - 1:
            result += "-"

    return result


user_input = input("please enter your word: ")
result = accum(user_input)

print(f"result for {user_input} is --> {result}")  