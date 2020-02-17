from lesson_package.tools import utils
# 相対パスはあまり勧められていない
# from ..tools import utils


def sing():
    return 'faieojfiorgj'

def cry():
    return utils.say_twice('jfaiojvojrrrrr')


if __name__ == '__main__:':
    print(sing())
    print('animal:', __name__)