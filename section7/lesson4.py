class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.what_is_your_kind())
b = Person
print(b.what_is_your_kind())


Person.about(1999)

class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        self.text.lower() + word.text.lower()

w = Word('text')
w2 = Word('###########')
print(len(w + w2))