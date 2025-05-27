#codewars challenge
#https://www.codewars.com/kata/5672682212c8ecf83e000050



def dbl_linear(n):
    u = [1]
    xi, yi = 0, 0

    while len(u) <= n:
        next_x = 2 * u[xi] + 1
        next_y = 3 * u[yi] + 1

        if next_x < next_y:
            u.append(next_x)
            xi += 1
        elif next_x > next_y:
            u.append(next_y)
            yi += 1
        else:
            u.append(next_x)
            xi += 1
            yi += 1

    return u[n]

user_input = int(input("enter your number --> "))

result = dbl_linear(user_input)
print(result)  
