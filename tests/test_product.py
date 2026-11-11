from typing import Any

import pytest

from src.product import Product


def test_product_init_success(init_fruits_products) -> None:
    apple = init_fruits_products["apple"]
    assert apple.name == "apple"
    assert apple.description == "red fruit"
    assert apple.price == 20
    assert apple.quantity == 100


def test_product_raise_error() -> None:
    with pytest.raises(TypeError):
        Product("sweet fruit", 500, 10)  # type: ignore


@pytest.fixture
def init_prodict_dict() -> dict[str, Any]:
    iphone = {
        "name": "iphone",
        "description": "expensive phone",
        "price": 100_000,
        "quantity": 1000,
    }
    return iphone


def test_init_product_dict_success(init_prodict_dict) -> None:
    last_iphone = Product.new_product(init_prodict_dict)
    assert last_iphone.name == "iphone"
    assert last_iphone.description == "expensive phone"
    assert last_iphone.price == 100_000
    assert last_iphone.quantity == 1000


@pytest.fixture
def init_bad_prodict_dict() -> dict[str, Any]:
    iphone = {
        "name": "iphone",
        "description": "expensive phone",
        "price": 100_000,
        "quantity": 1000,
        "bad": 11,
    }
    return iphone


def test_raise_product_dict_error(init_bad_prodict_dict) -> None:
    with pytest.raises(TypeError):
        Product.new_product(init_bad_prodict_dict)


def test_get_price(init_fruits_products, capsys) -> None:
    apple = init_fruits_products["apple"]

    apple.price = -100
    assert apple.price == 20

    output = capsys.readouterr()
    captured = output.out.strip()
    assert captured == "Цена не должна быть нулевая или отрицательная"

    apple.price = 0
    assert apple.price == 20

    output = capsys.readouterr()
    captured = output.out.strip()
    assert captured == "Цена не должна быть нулевая или отрицательная"

    apple.price = 100
    assert apple.price == 100


def test_add_same_class_success(init_grass_dict, init_smartphone_dict) -> None:
    emerald_grass = init_grass_dict["emerald_grass"]
    shadow_grass = init_grass_dict["shadow_grass"]
    total_grasses = emerald_grass + shadow_grass

    assert total_grasses == 279_000

    iphone = init_smartphone_dict["iphone"]
    poco = init_smartphone_dict["poco"]
    total_smartphones = iphone + poco

    assert total_smartphones == 85_000_000


def test_add_same_class_raise_error(init_grass_dict, init_smartphone_dict) -> None:
    emerald_grass = init_grass_dict["emerald_grass"]
    shadow_grass = init_grass_dict["shadow_grass"]

    iphone = init_smartphone_dict["iphone"]
    poco = init_smartphone_dict["poco"]

    with pytest.raises(TypeError):
        _ = shadow_grass + poco
    with pytest.raises(TypeError):
        _ = emerald_grass + iphone
