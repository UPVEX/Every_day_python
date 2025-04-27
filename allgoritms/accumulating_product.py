# این برنامه لیستی از اعداد میگیره و ضریب انباشته انهارو برمیگردونه


def accumulating_product(numbers):
    result = []
    product = 1

    for num in numbers:
        product *= num
        result.append(product)

    return result



user_input = input("please enter your number list .(using space between your numbers) : ")
numbers = [int(num) for num in user_input.split()]

print("the result is ==> ", accumulating_product(numbers))



