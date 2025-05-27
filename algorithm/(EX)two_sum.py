"""
در این برنامه یک لیست میگیریم و یک تارگت
هدف این هستش که جمع دو عدد در لیست که مساوی تارگت بشه ایندکسش رو برگردونیم

[2, 7, 11, 15], 18 ==> [1, 2]

"""

def two_sum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return [p1, p2]

        elif s > target:
            p2 -= 1

        else:
            p1 += 1

print(two_sum([2, 7, 11, 15], 18))

