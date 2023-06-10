"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)


    assert item1.price == 10000  # Price test Item1
    assert item2.price == 20000  # Price test Item2

    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000  # Price discount test
    assert item2.apply_discount() == 16000  # Price discount test

    assert Item.all != []