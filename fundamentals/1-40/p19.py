def abbrev_name(name):

    first = name[0].upper()

    second = name.split(" ")

    for names in second:
        initial = names[0]

    upper_initial = initial.upper()

    return first + "." + upper_initial

print(abbrev_name("piotr ruwnoo"))