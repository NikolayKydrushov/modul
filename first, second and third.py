first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")

if first != second and first != third and second != third:
    print(0)
elif first == second and first == third:
    print(2)
elif first == second or first == third or second == third:
    print(3)
#else:
#    print(0)