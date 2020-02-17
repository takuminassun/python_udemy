from lesson_package.tools import utils
# 相対パスはあまり勧められていない
# from ..tools import utils


def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')