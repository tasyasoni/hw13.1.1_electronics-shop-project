from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = None
        self.number_of_sim = number_of_sim


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __call__(self, *args, **kwargs):
        return self.quantity


    def __add__(self, other):
        if not isinstance(other, (Item, Phone)):
            return "Объект не принадлежит к Phone` или `Item` классу"
        else:
            return self.quantity + other.quantity


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int):
            raise ValueError
        if value <= 0:
            raise ValueError
        else:
            self.__number_of_sim = value







