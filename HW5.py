import random


def rg(n, k):
    enigma_numb = random.randint(1, n)
    for i in range(k):
        print('----------------------')
        print('Retry count: ', k - i)
        try:
            num = int(input('Input numb: '))
        except (ValueError, TypeError):
            print('Not numb, try again')
        else:
            if num == enigma_numb:
                print('Yes, you guessed numb, my congratulations')
                exit()
            elif num < enigma_numb:
                print('Numb must be greater')
            elif num > enigma_numb:
                print('Numb must be less')
            elif i == k - 1 and num != enigma_numb:
                print('Numb mot guessed\n'
                      'No more attempts\n'
                      'Guessed numb :', enigma_numb)
                exit()
