# coding: UTF-8

# 位置引数とキーワード引数
# def menu(entree='beef', drink='wine', dessert='ice'):
#     print(entree)
#     print(drink)
#     print(dessert)

# menu()


# # pythonはデフォルト引数で空のリストやディクショナリーを用いない
# def test_func(x, l=[]):
#     l.append(x)
#     return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# def say_something(word, *args):
#     print('word = ', args)
#     for arg in args:
#         print(arg)

# say_something('Hi!', 'Mike', 'Nance')

# キーワード引数と辞書化
# def menu(food, *args, **kwargs):
#     print(food)
#     print(args)
#     print(kwargs)

# menu('banana', 'apple', 'orange', entree='beef', drink='coffee')


def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)