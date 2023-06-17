from src.phone import Phone

phone1 = Phone("Motorola", 70000, 10, 1)
phone2 = Phone("iPhone", 100000, 5, 2)


def test_repr():
    assert phone1.__repr__() == "Phone('Motorola', 70000, 10, 1)"
    assert phone2.__repr__() == "Phone('iPhone', 100000, 5, 2)"


def test_str():
    assert phone1.__str__() == 'Motorola'
    assert phone2.__str__() == 'iPhone'


def test_number_of_sims():
    assert phone1.number_of_sim == 1
    assert phone2.number_of_sim == 2
