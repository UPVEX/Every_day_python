#codewars challenge
#I have four positive integers, A, B, C and D, where A < B < C < D. 
# The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order. 
# Your task is to return the value of D.




def find_D(numbers):
    # ابتدا لیست اعداد را مرتب می‌کنیم
    sorted_numbers = sorted(numbers)
    
    # کوچکترین عددها، کاندیدهای A، B، C و D هستند
    for A in sorted_numbers:
        for B in sorted_numbers:
            if A >= B:
                continue
            for C in sorted_numbers:
                if B >= C:
                    continue
                for D in sorted_numbers:
                    if C >= D:
                        continue
                    # بررسی می‌کنیم که حاصل‌ضرب‌ها در لیست وجود داشته باشند
                    if (A * B in sorted_numbers and
                        B * C in sorted_numbers and
                        C * D in sorted_numbers and
                        D * A in sorted_numbers):
                        return D

# مثال استفاده:
numbers = [2, 6, 7, 3, 14, 35, 15, 5]
print(find_D(numbers))  # خروجی باید 6 باشد (زیرا A=2، B=3، C=4، D=6)
