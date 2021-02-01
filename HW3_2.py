def collect_info(**kwargs):
    string = ""
    for key, value in kwargs.items():
        string += f"{key:13} {value}\n"
    return string


print(collect_info(name="denis", surname="milonov", birthday="not telling", city="moscow", email="samletext@mail.ru",
                   phone_number="not telling"))
