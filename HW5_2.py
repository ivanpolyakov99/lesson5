# Task_2
try:
    size = int(input('Size of array: '))
    if size <= 0:
        raise ValueError
    _list = []
    for i in range(size):
        _list.append(int(input('Input element of array %d: ' % i)))
except ValueError:
    print('Array can not be negative, try again')
    exit()


def check(x):
    return len(set(x))


print(str('-----')*8)
print('Your array: ', _list)
print('Numb of different elements in the array: ', check(_list))

# Task_3
a = str(input('\nInput string: '))
a = ' '.join(a.title().split())
print('Format string:', str(a))
