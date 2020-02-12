# 80文字以上は次の行へ改行する
s = "aaaaaaaaa"\
    + "bbbbbbbbb"
print(s)

x = 0

# 次の行は4つスペースを空ける
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')


y = [1, 2, 3]
x = 1
if x in y:
    print('in')
# >> in


# is は　None　オブジェクトで用いられる
is_empty = None
if is_empty is None:
    print('None!!!')


count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1


while True:
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')