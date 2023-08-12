import pytest
from src.item import Item


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
