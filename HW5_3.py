def decorator_decorator(str1, str2):
        def inner(func_to_dec):
                def inner1(*args, **kwargs):
                        print(str1)
                        func_to_dec(*args, **kwargs)
                        print(str2)
                return inner1
        return inner


@decorator_decorator('1-ая строка до функции', '2-ая строка после функции')
def func():
    print('Какой-то рандомный текст')

func()
