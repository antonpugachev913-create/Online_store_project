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


@pytest.fixture(scope="module")
def category_goods() -> list[Category]:
    return [
        Category("fruits", "fresh fruits", ["apple", "banana", "cherry"]),
        Category("televisions", "smart televisions", ["Huawei", "Samsung", "Appple"]),
    ]


def test_category_init_success(category_fruits) -> None:
    assert category_fruits.name == "fruits"
    assert category_fruits.description == "fresh fruits"
    assert category_fruits.products == ["apple", "banana", "cherry"]


def test_category_raise_error() -> None:
    with pytest.raises(TypeError):
        Category("a", "b")  # type: ignore


def test_category_count_success(category_fruits) -> None:
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_private_work_success(category_fruits) -> None:
    product_1 = Product("Pineapple", "yellow fruit", 100, 5)
    Category.add_product(category_fruits, product_1)
    assert Category.product_count == 4

    product_2 = Product("dragon_fruit", "bright fruit", 300, 3)
    Category.add_product(category_fruits, product_2)
    assert Category.product_count == 5


# def test_category_private_work_success(list_category = category_goods) -> None:
#     product = Product('ASUS', 'Powerful tv', 50_000, 100)
#     tv_category = list_category[1]
#     Category.add_product(tv_category, product)
#     assert Category.product_count == 4

# def test_category_products_get_success(category_fruits) -> None:
#
    # product_1 = Product("Pineapple", "yellow fruit", 100, 5)
    # Category.add_product(category_fruits, product_1)
    # assert Category.product_count == 4
    #
    # product_2 = Product("dragon_fruit", "bright fruit", 300, 3)
    # Category.add_product(category_fruits, product_2)
    # assert Category.product_count == 5
