# _list = [1, 2, 3]
# print(_list)
# del(_list[1])
# print(_list)
# del _list[:]
# print(_list)

# _dict = {'key1': 1, 'key2': 2}
# del _dict['key1']
# print(_dict)

# FUNCTIONS


# def foo_params(param1=True, param2=True):
# pass


# foo_params(False, False)
# foo_params(param2=False, param1=True)
# foo_params(False, param2=True) низя


# def foo_args(*args):
# print(args)

# foo_args(1, 2, 3, 4, 5)


# def foo_kwargs(**kwargs):
# print('Foo kwargs', kwargs)

# foo_kwargs(a=1, b=2)


# def foo_ar_kw(*args, **kwargs):
# print('Foo args', args)
# print('Foo kwargs', kwargs)

# foo_ar_kw(1, 2, 3, 4, 5, a=1, b=2, c=3)


# (lambda a, b: a + b)(3, 4)


# def foo_arr(_list, operation=None):
  #  result = 0
   # for elem in _list:
    #    result = operation(result, elem)
    #return result


# print(foo_arr([1, 2, 3], operation=lambda x, y: x + y))

def foo1(x):
    return x ** 2

def foo2(x):
    return 2 * x - 1

def foo3(x):
    return 2 * x

def foo_res(x):
    if -5 <= x <= 5:
        res = foo1(x)
    elif x < -5:
        res = foo2(x)
    elif x > 5:
        res = foo3(x)

    return res

for i in range(-10, 10, 1)
    print(foo_res(i))

#new line branch_1
