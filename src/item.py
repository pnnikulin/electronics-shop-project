import csv
import os


"""Создаём путь к файлу items.csv"""
PATH = os.path.abspath('..')
PATH_TO_FILE = os.path.join(PATH, 'src', 'items.csv')


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        return int(self.quantity) + int(other.quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name
        else:
            print('Больше 10-ти символов')

    @classmethod
    def instantiate_from_csv(cls, path_to_csv=PATH_TO_FILE):
        cls.all.clear()
        try:
            with open(path_to_csv, encoding='cp1251') as csvfile:
                items_csv = csv.DictReader(csvfile)
                items_csv_list = [cls(i['name'], i['price'], i['quantity']) for i in items_csv]
            return items_csv_list
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {path_to_csv}')
        except KeyError:
            raise InstantiateCSVError(f'Файл {path_to_csv} поврежден')

    @staticmethod
    def string_to_number(digit):
        """статический метод для проверки числа"""
        if '.' in digit:
            return int(float(digit))
        elif digit.isdigit():
            return int(digit)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price


class InstantiateCSVError(Exception):
    """Класс для вывода ошибки при повреждении файла"""

    def __str__(self):
        if self.args:
            return f'{self.args[0]}'
        return f'Файл поврежден'


if __name__ == '__main__':
    item = Item.instantiate_from_csv()
    print(item)