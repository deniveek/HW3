def sum_two(a, b, c):
    list_1 = [a, b, c]
    list_1.remove(min)
    return sum(list_1)


print(sum_two(int(input("a ")), int(input("b ")), int(input("c "))))
