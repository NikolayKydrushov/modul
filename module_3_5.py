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
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(420))


#Здравствуйте!
#Задание выполнено почти верно, однако есть небольшая ошибка:
#1) При умножении цифр числа нули должны быть учтены:
# при встрече с 0 функция должна продолжать рекурсию, пропуская этот ноль,
# так как умножение на 0 должно обнулять результат.
# В текущем виде функция не обнуляет результат при наличии нуля.