from src.item import Item


class MixinLog:


    def __init__(self):
        self.count = 0


    def change_lang(self):
        self.count += 1
        if self.count % 2 != 0:
            self.language = "RU"
            return(self)
        else:
            self.language = "EN"
            return(self)




class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity, *language):
        super().__init__(name, price, quantity)
        self.language = "EN"
















