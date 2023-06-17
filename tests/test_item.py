"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
from src.phone import Phone


item1 = Item("Смартфон", 10000, 20)
item2 = Item('Ноутбук', 20000, 5)
phone1 = Phone("Motorola", 70000, 10, 1)
phone2 = Phone("iPhone", 100000, 15, 2)



def test_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)


    assert item1.price == 10000  # Price test Item1
    assert item2.price == 20000  # Price test Item2

    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000  # Price discount test
    assert item2.apply_discount() == 16000  # Price discount test

    assert Item.all != []

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.4') == 5
    assert Item.string_to_number('5.5') == 5

def test_instantiate_from_csv():
    lists = Item.instantiate_from_csv()
    assert type(lists) == list

def test_repr():
    assert item1.__repr__() == "Item('Смартфон', 10000, 20)"
    assert item2.__repr__() == "Item('Ноутбук', 20000, 5)"

def test_str():
    assert item1.__str__() == 'Смартфон'
    assert item2.__str__() == 'Ноутбук'

def test__add__():
    assert item1 + phone1 == 30
    assert item2 + phone1 == 15
    assert item1 + phone2 == 35
    assert phone1 + phone1 == 20