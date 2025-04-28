# یک مجموعه خاص در این تمرین مجموعه ای است که هر ایندکس فرد در آن شامل یک عدد فرد باشد و هر ایندکس زوج شامل یک عدد زوج.


def khass(numbers):

    for i, num in enumerate(numbers):

        if i%2 == 0 and num%2 != 0:
            return False
        
        elif i%2 != 0 and num%2 == 0:
            return False
        
    return True


input_numbers = input("please enter your numbers by using space bottom ==> ")
numbers = [int(num) for num in input_numbers.split()]

result = khass(numbers)

if result:
    print(numbers, " are khass")

else:
    print(numbers, " are not khass")
