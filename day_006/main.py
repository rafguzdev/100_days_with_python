def funA(num, let = 'default'):
    print(num)
    print(let)

funA(2)
print('\n')
funA(2, 'test')


def funB(*args):
    for arg in args:
        print(arg)

funB(1,2,3,4,5,'test')


def funC(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

funC(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)