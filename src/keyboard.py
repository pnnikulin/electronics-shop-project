from src.item import Item


class MixinLog:
    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'
