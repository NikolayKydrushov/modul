def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 1.5, True]
values_dict = {'a' : 2, 'b' : 4.32, 'c' : 7}
print_params(* values_list)
print_params(** values_dict)

values_list_2 = [True, 2]
print_params(* values_list_2, 33)

