'''
codewars challenge

you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.
Tested years are in range 1600 ≤ year ≤ 4000.

'''




def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


years_to_test = [1600, 1700, 1800, 1900, 2000, 2024, 2100]
for year in years_to_test:
    print(f"Is {year} a leap year? {is_leap_year(year)}")
