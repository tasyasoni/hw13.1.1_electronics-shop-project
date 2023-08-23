import pytest

from src.item import Item
from src.phone import Phone



@pytest.fixture
def src_phone():
    src_phone = Phone("Супер-пупер-фон",5000, 1, 70)
    return src_phone


item1 = Item("Телефончик", 6000, 22)
def test_add(src_phone):
    assert src_phone.__add__(7688) == "Объект не принадлежит к Phone` или `Item` классу"
    assert src_phone.__add__(item1) == 23

def test_repr(src_phone):
    assert repr(src_phone) == "Phone('Супер-пупер-фон', 5000, 1, 70)"


def test_str(src_phone):
    assert str(src_phone) == "Супер-пупер-фон"


def test_number_of_sim(src_phone):
    assert src_phone.number_of_sim == 70
