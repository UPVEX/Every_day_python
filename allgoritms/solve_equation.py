#این برنامه از کاربر به عنوان ورودی یک معادله میگیرد و در خروجی چاپ میکند



def solve_equation(equation):
    try:
        result = eval(equation)  # eval change str to a equation in python
        return result
    except Exception as e:  # exception is show eror in python
        return f"Error: {str(e)}" 


user_input = input("please enter your moadele for example(1+1) : ")
print(solve_equation(user_input))