# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
# This method find outlier 



def find_outlier(integers):
    
    is_even = True if (integers[0] % 2 == integers[1] % 2 == 0) or (integers[1] % 2 == integers[2] % 2 == 0) or (integers[0] % 2 == integers[2] % 2 == 0)  else False

    for num in integers:
        if is_even and num % 2 != 0:
            return num
        elif not is_even and num % 2 == 0:
            return num
        

def make_integers(list):

    numbers =[]

    for number in list:
        number = int(number)
        numbers.append(number)

    return numbers

user_input = (input("enter your numbers (at least 3 numbers and all of them must be odd or even instead of one of them) --> ")).split()

numbers = make_integers(user_input)
result = find_outlier(numbers)

print(f"the outlier in {numbers} is ({result})")