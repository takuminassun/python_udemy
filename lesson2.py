r = [1,2,3,4,5,1,2,3]
print(r.index(3))

print(r.count(3))

if 5 in r:
  print('exit')

r.sort()
print(r)
r.sort(reverse=True)
print(r)

i = [1 ,2, 3, 4, 5]
j = i
print('j=i', i)

t = 1,
print(t)
# >>(1,)

i = 10
j = 20
print(i, j)
# >>10 20
tmp = i
i = j
j = tmp
print(i, j)
# >>20 10

a = 10
b = 20
print(a, b)
# >>10 20
a, b = b, a
print(a, b)
# >>20 10

#　タプルは中身を変えることはできない
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)