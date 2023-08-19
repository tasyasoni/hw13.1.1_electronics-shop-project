import pytest
from src.item import Item


@pytest.fixture


def src_inf():
    src_inf = Item("Супер-пупер-смарт",34700, 1)
    return src_inf

def test_repr(src_inf):
    assert repr(src_inf) == "Item('Супер-пупер-смарт', 34700, 1)"



def test_str(src_inf):
    assert str(src_inf) == "Супер-пупер-смарт"



@pytest.fixture


def src_string():
    src_string = Item("",0, 0)
    return src_string
def test_string_to_number(src_string):
    assert src_string.string_to_number("10.0") == 10
    assert src_string.string_to_number("0.0") == 0
    assert src_string.string_to_number("10.265") == 10
    assert src_string.string_to_number("5.5") == 5


@pytest.fixture


def src_name():
    src_name = Item("_",0, 0)
    return src_name

def test_name(src_name):
    src_name.name = "СуперСмартфон"
    assert src_name.name == "СуперСмарт"
    src_name.name = "Телевизор"
    assert src_name.name == "Телевизор"

@pytest.fixture


def src_items1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


Item.pay_rate = 0.5


def test_calculate_total_price1(src_items1):
    assert src_items1.calculate_total_price() == 200000


def test_apply_discount1(src_items1):
    assert src_items1.apply_discount() == 5000


@pytest.fixture


def src_items2():
    item2 = Item("Ноутбук", 20000, 5)
    return item2


def test_calculate_total_price2(src_items2):
    assert src_items2.calculate_total_price() == 100000


def test_apply_discount2(src_items2):
    Item.pay_rate = 0.5
    assert src_items2.apply_discount() == 10000






