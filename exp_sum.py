#




def exp_sum(n):
    # ایجاد یک آرایه برای ذخیره نتایج مرحله‌های قبلی
    dp = [0] * (n + 1)
    dp[0] = 1  # تعداد تقسیم برای عدد صفر برابر با یک است

    # محاسبه تعداد تقسیم‌ها برای اعداد 1 تا n
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]

# مثال‌ها
print(exp_sum(1))    # 1
print(exp_sum(2))    # 2
print(exp_sum(4))    # 5
print(exp_sum(5))    # 7
print(exp_sum(10))   # 42
print(exp_sum(50))   # 204226
print(exp_sum(80))   # 15796476
print(exp_sum(100))  # 190569292
