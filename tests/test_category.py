from typing import Any

import pytest

from src.category import Category
from src.product import Product


def test_category_init_success(init_fruits_products, category_fruits) -> None:
    assert category_fruits.name == "fruits"


def test_category_raise_error() -> None:
    with pytest.raises(TypeError):
        Category("a", "b")  # type: ignore


def test_category_count_success(category_fruits) -> None:
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_private_work_success(category_fruits) -> None:
    product_1 = Product("Pineapple", "yellow fruit", 100, 5)
    category_fruits.add_product(product_1)
    assert Category.product_count == 4

    product_2 = Product("dragon_fruit", "bright fruit", 300, 3)
    category_fruits.add_product(product_2)
    assert Category.product_count == 5


def test_category_output_products(category_fruits) -> None:
    list_products = category_fruits.products.splitlines()
    assert list_products[0] == "apple, 20 руб. Остаток: 100 шт."
    assert list_products[1] == "banana, 30 руб. Остаток: 50 шт."
    assert list_products[2] == "cherry, 100 руб. Остаток: 250 шт."


def test_category_raise_products_error() -> None:
    with pytest.raises(TypeError):
        Product("red fruit", 20, 100)  # type: ignore
        Product("banana", "sweet yellow fruit", 30, 50)
