def division(number1, number2):
    try:
        return float(number1)/float(number2)
    except (ZeroDivisionError, ValueError) as err:
        print(err)


print(division(input("делимое "), input("делитель ")))
