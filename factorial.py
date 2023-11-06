#این کد فاکتوریل هر عددی رو حساب میکنه

def factoril(x):

    if x == 0:
        return 1
    else:
        return x * factoril(x-1)
        

x = int(input("enter a number for i give you the factorial -> "))
print(factoril(x))
