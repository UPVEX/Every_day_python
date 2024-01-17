# این برنامه از کاربر یک ورودی دریافت میکنه (مثلا 2) و تمامحالت های ممکن برای ساخت پرانتز رو با دو پرانتز میسازه
# :مثال
# the result for 3 is ['((()))', '(()())', '(())()', '()(())', '()()()']



def balanced_parens(n):
    def generate_parentheses(current, left, right):
        if left == 0 and right == 0:
            result.append(current)
            return
        if left > 0:
            generate_parentheses(current + '(', left - 1, right)
        if right > left:
            generate_parentheses(current + ')', left, right - 1)

    result = []
    generate_parentheses('', n, n)
    return result


user_input = int(input("please enter number : "))
result = balanced_parens(user_input)
print(f"the result for {user_input} is {result} .")