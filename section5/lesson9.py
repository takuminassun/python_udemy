# エラー処理
# l = [1, 2, 3]
# i = 5

# try:
#     l[0]
# except IndexError as exc:
#     print("Don't worry: {}".format(exc))
# except NameError as exc:
#     print(exc)
# except Exception as exc:
#     print('other:{}'.format(exc))
# else:
#     print('done')
# finally:
#     print('clean up')



# 独自例外
class UppercaseError(Exception):
  pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
  check()
except UppercaseError as exc:
    print('This is my fault. Go next' )