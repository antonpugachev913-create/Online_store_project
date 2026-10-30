import pytest
from typing import Any
from src.catalog import Category, Product


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def init_fruits_products() -> dict[str, Product]:
    apple = Product("apple", "red fruit", 20, 100)
    banana = Product("banana", "sweet yellow fruit", 30, 50)
    cherry = Product("cherry", "purple berry", 100, 250)
    products = [apple, banana, cherry]
    return {product.name: product for product in products}


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
def category_fruits() -> Category:
    apple = Product("apple", "red fruit", 20, 100)
    banana = Product("banana", "sweet yellow fruit", 30, 50)
    cherry = Product("cherry", "purple berry", 100, 250)
    return Category("fruits", "fresh fruits", [apple, banana, cherry])


def test_category_init_success(init_fruits_products, category_fruits) -> None:
    products = init_fruits_products
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
        apple = Product("red fruit", 20, 100)  # type: ignore
        banana = Product("banana", "sweet yellow fruit", 30, 50)
    # list_products = category_fruits.products.splitlines()
    # assert list_products[0] == "apple, 20. Остаток: 100 шт."
    # assert list_products[1] == "banana, 30. Остаток: 50 шт."
    # assert list_products[2] == "cherry, 100. Остаток: 250 шт."


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



# def test_category_private_work_success(list_category = category_goods) -> None:
#     product = Product('ASUS', 'Powerful tv', 50_000, 100)
#     tv_category = list_category[1]
#     Category.add_product(tv_category, product)
#     assert Category.product_count == 4


# @pytest.fixture(scope="module")
# def category_goods() -> list[Category]:
#     return [
#         Category("fruits", "fresh fruits", ["apple", "banana", "cherry"]),
#         Category("televisions", "smart televisions", ["Huawei", "Samsung", "Appple"]),
#     ]
