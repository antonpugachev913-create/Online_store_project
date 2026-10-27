import pytest

from src.catalog import Category, Product


@pytest.fixture()
def product_apple() -> Product:
    return Product("apple", "sweet fruit", 500, 10)


def test_product_init_success(product_apple) -> None:
    assert product_apple.name == "apple"
    assert product_apple.description == "sweet fruit"
    assert product_apple.price == 500
    assert product_apple.quantity == 10


def test_product_raise_error() -> None:
    with pytest.raises(TypeError):
        Product("sweet fruit", 500, 10)  # type: ignore


@pytest.fixture(scope="module")
def category_fruits() -> Category:
    return Category("fruits", "fresh fruits", ["apple", "banana", "cherry"])


# @pytest.fixture(autouse=True)
# def reset_counters() -> None:
#     Category.category_count = 0
#     Category.product_count = 0


def test_category_init_success(category_fruits) -> None:
    assert category_fruits.name == "fruits"
    assert category_fruits.description == "fresh fruits"
    assert category_fruits.products == ["apple", "banana", "cherry"]


def test_category_raise_error() -> None:
    with pytest.raises(TypeError):
        Category("a", "b") # type: ignore


def test_category_count_success(category_fruits) -> None:
    assert Category.category_count == 1
    assert Category.product_count == 3
