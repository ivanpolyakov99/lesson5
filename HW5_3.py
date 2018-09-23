def decorator_decorator(str1, str2):
        def inner(func_to_dec):
            print(str1)
            func_to_dec()
            print(str2)
        return inner


@decorator_decorator('1-ая строка до функции', '2-ая строка после функции')
def func_to_dec():
    print('Какой-то рандомный текст')
