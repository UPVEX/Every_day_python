'''
buy_sell stock
    [7, 1, 5, 6, 4] --> 5
    [9, 7, 6, 4, 3, 1] --> 0

* this program show you in which price you have to sell your stock

'''

def max_profit(prices):
    cur_max, max_so_far = 0, 0

    for i in range(1, len(prices)):
        cur_max = max(0, cur_max + prices[i] - prices[i-1])
        max_so_far = max(max_so_far, cur_max)
        print(f" i ->{i}   curmax {cur_max}   max so far {max_so_far}")

    return max_so_far

print(max_profit([9, 7, 6, 4, 3, 1]))