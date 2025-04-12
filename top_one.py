# برنامه زیر بیشترین تعداد تکرار رو برمیگرداند 
# [1,2,3,3,3,4,4,1,1] -> [1,3]


def top(arr):

    values = {}
    result = []
    maxim = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
    
    maxim = max(values.values())

    for i in values:
        if values[i] == maxim:
            result.append(i)

    return result


print(top([1,2,3,3,3,4,4,1,1]))