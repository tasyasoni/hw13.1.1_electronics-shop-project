import pytest
from src.keyboard import Keyboard


@pytest.fixture


def src_inf():
    src_inf = Keyboard("Супер-клава",20000, 7)
    return src_inf


def test_change_lang(src_inf):
    assert src_inf.language == "EN"
    src_inf.change_lang()
    assert src_inf.language == "RU"
    src_inf.change_lang()
    assert src_inf.language == "EN"





