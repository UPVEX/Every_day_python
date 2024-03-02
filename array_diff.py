# codewars
# https://www.codewars.com/kata/523f5d21c841566fde000009




def array_diff(a, b):
    result = [item for item in a if item not in b]
    return result


print(array_diff([1, 2], [1])) 
print(array_diff([1, 2, 2, 2, 3], [2]))  
