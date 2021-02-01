def power(x: float, y: int):
    x = 1/x if y < 0 else x
    y = abs(y)
    res = 1
    for i in range(y):
        res = res*x
    return res


print(f'{power(float(input("x= ")), int(input("y= ")))}')
