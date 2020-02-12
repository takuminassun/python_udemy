 # 関数内関数
# def outer(a, b):

#     def plus(c, d):
#         return c + d

#     r = plus(a, b)
#     print(r)

# outer(1, 2)

# クロージャー
# def outer(a, b):
#     def inner():
#         return a + b

#     return inner
# f = outer(1, 2)
# r = f()
# print(r)

# def circle_are_func(pi):
#     def circele_are(radius):
#         return pi * radius * radius
#     return circele_are
# cal1 = circle_are_func(3.14)
# cal2 = circle_are_func(3.141592)

# print(cal1(10))
# print(cal2(10))

# デコレーター 包み込むイメージ
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# イメージ↓
# f = print_info(print_more(add_num))

# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')
# print(r)