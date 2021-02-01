def edit(string: str):
    string = string.split(' ')
    output = []
    for word in string:
        if word.isalpha() and word.isascii():
            output.append(word.capitalize())
    return ' '.join(output)


print(edit(input("enter some text\n")))
