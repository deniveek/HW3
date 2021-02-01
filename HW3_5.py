def split_and_add():
    res = 0
    while True:
        in_str = input('enter some numbers\n').split(' ')
        for element in in_str:
            if element == 'quit':
                print(res)
                return
            else:
                try:
                    res += int(element) if '.' not in element else float(element)
                except ValueError:
                    print('incorrect input; to exit enter "quit"\n')
        print(res)


split_and_add()
