class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print ("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

class FunctionalList:
    '''Класс-обёртка над списком с добавлением некоторой функциональной магии: head,
    tail, init, last, drop, take.'''

    def __init__(self, num, values=None):
        self.__number__ = num
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __round__(self, n):
        return round(self.__number__, n)

if __name__ == "__main__":
    word = Word('Привет')
    new_word = Word('Пока')
    print (word >= new_word)

    n_list = FunctionalList(2.3452453, ('Привет', 'Пока'))
    print (len(n_list))
    print (round(n_list, 2))