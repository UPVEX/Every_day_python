# 



import math

def circle_or_square(radius, area_square):
    # محیط دایره
    circumference_circle = 2 * math.pi * radius

    # طول ضلع مربع
    side_square = math.sqrt(area_square) / 2

    # محیط مربع
    circumference_square = 4 * side_square

    # بررسی کدام یک از دو مقدار بزرگتر است
    return circumference_circle > circumference_square


radius = int(input("enter your radius: "))
area_square = int(input("enter your area_square: "))

result = circle_or_square(radius, area_square)

if result == True:
    print("mohit dayere is biger than mohit square")

else:
    print("it seems mohit dayere is smaller than mohit square")