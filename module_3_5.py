def get_multiplied_digits(number):
    str_number = str(number)
    if not str_number:
        return 1

    if len(str_number) == 1:
        if int(str_number) == 0:
            return 1
        else:
            return int(str_number)

    first = int(str_number[0])
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))
    else:
        rest = get_multiplied_digits(int(str_number[1:]))
        if rest == 0:
            return 0
        else:
            return first * rest


print(get_multiplied_digits(420))

