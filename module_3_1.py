#from module_2_5 import result1



def cout_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    tuple_ = len(string), string.upper(), string.lower()
    cout_calls()
    return tuple_

def is_contains(string, arr):
    flag = False
    cout_calls()
    string = string.lower()
    for i in range(len(arr)):
        arr[i] = arr[i].lower()
        if arr[i] == string:
            flag = True

    if flag == True:
        return True
    else:
        return False


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)

