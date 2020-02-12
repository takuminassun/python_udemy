# # ラムダ
# l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

# def change_words(words, func):
#     for word in words:
#         print(func(word))

# def sample_func(word):
#     return word.capitalize()

# def sample_func2(word):
#     return word.lower()
# # sample_func = lambda word: word.capitalize()

# change_words(l, lambda word: word.capitalize())
# change_words(l, lambda word: word.lower())

# ジェネレーター
# def counter(num= 10):
#     for _ in range(num):
#         yield 'run'

# def greeting():
#     yield 'Good mornig'
#     yield 'Good afternoon'
#     yield 'Good night'

# g = greeting()
# c = counter()
# print(next(g))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print('@@@@@@@')
# print(next(g))
# print('@@@@@@@')
# print(next(g))

# リスト内包表記 短いfor文等
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

# 1と2は同じ
# 1
r = []
for i in t:
    if i % 2 == 0:
      r.append(i)
print(r)

# 2
r = [i for i in t if i % 2 == 0]
print(r)

# 3と4は同じ
# 3
r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

# 4
r = [i * j for i in t for j in t2]
print(r)