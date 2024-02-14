# This algorithm takes an array and moves all of the zeros to the end



def move_zero(li):
    
    non_zero_number = [num for num in li if num != 0]

    num_zeros = len(li) - len(non_zero_number)

    return non_zero_number + [0] * num_zeros

def make_integers(list):

    numbers =[]

    for number in list:
        number = int(number)
        numbers.append(number)

    return numbers

user_input = (input("enter your numbers --> ")).split()

numbers = make_integers(user_input)

result = move_zero(numbers)

print(f"the result for {numbers} is --> {result}")