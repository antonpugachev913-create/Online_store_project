import pytest


def test_init_smartphone_success(init_smartphone_dict) -> None:
    iphone = init_smartphone_dict["iphone"]

    assert iphone.name == "Blue iphone"
    assert iphone.description == "Powerful phone"
    assert iphone.price == 100_000
    assert iphone.quantity == 250

    assert iphone.efficiency == 150
    assert iphone.model == "Iphone 18"
    assert iphone.memory == "32 Гб"
    assert iphone.color == "Blue"
