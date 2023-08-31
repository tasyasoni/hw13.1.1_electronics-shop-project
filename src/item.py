import csv


class InstantiateCSVError(Exception):
    pass




class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        #super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other,Item):
            return "Объект не принадлежит к Phone` или `Item` классу"
        else:
            return self.quantity + other.quantity


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_long):
        if len(name_long) > 10:
            self.__name = name_long[:10]
        else:
            self.__name = name_long
        return self.name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.quantity * self.price
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
      try:
          file = open('../src/item.csv')
      except FileNotFoundError:
          print('_Отсутствует файл item.csv_')
      finally:
          try:
              with open('../src/item1.csv') as csvfile:
                  reader = csv.DictReader(csvfile)
                  for line in reader:
                      if "quantity" in line:
                          item = cls(line['name'], line['price'], line["quantity"])
                      else:
                          raise InstantiateCSVError
          except InstantiateCSVError:
              print("_Файл item1.csv поврежден_")



    @staticmethod
    def string_to_number(number):
        number = number.split(".")[0]
        return (int(number))





