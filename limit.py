'''
[1,2,3,4,5]
    min 3 =>> [3,4,5]
    max 3 =>> [1,2,3]
    max, min 3 =>> [3]
'''

def limit(arr, min=None, max=None):

    min_cheak = lambda val : True if min is None else (val >= min)
    max_cheak = lambda val : True if max is None else (val <= max)

    return [val for val in arr if min_cheak(val) and  max_cheak(val)]



print(  limit([1,2,3,4,5], 3, 3))