# from termcolor import colored

# print('test')

# print(colored('test', 'red'))


# importは一つずつアルファベット順
# 標準ライブラリ
# import collections
# import os
# import sys

# サードパーティ
# import termcolor

# レッスンパッケージ
# import lesson_package

# ローカルのファイル
# import config

import lesson_package.talk.animal
import config

def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__:':
    main()