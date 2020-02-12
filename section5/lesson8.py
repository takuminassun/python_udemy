# 辞書内包表記
# w = ['mon', 'tue', 'wed']
# f = ['coffee', 'milk', 'water']

# # 1と2は同じ出力結果
# # 1
# d = {}
# for x, y in zip(w, f):
#     d[x] = y
# print(d)
# # 2
# d = {x: y for x, y in zip(w, f)}
# print(d)

# 集合内包表記

# 3と4は同じ出力結果
# 3
# s = set()

# for i in range(10):
#     if i % 2 == 0:
#         s.add(i)
# print(s)

# # 4
# s = {i for i in range(10) if i % 2 == 0}
# print(s)

# ジェネレータ内包表記
# def g():
#     for i in range(10):
#         yield i

# g = g()

# g = (i for i in range(10) if i % 2 == 0)

# for x in g:
#     print(x)


# # 名前空間とスコープ

# animal = 'cat'

# def f():
#     animal = 'dog'
#     print('after:', animal)

# f()
# print('global:', animal )

# >> after: dog
# >> global: cat