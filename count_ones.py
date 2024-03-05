# codewars challenge
# https://www.codewars.com/kata/526571aae218b8ee490006f4



def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

user_input = int(input("enter an number --> "))
result = count_ones(user_input)

print(f"the result for ({user_input}) is {result}")

# second method

'''

def countBits(n):
    return bin(n).count("1")

'''