import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def init_fruits_products() -> dict[str, Product]:
    apple = Product("apple", "red fruit", 20, 100)
    banana = Product("banana", "sweet yellow fruit", 30, 50)
    cherry = Product("cherry", "purple berry", 100, 250)
    products = [apple, banana, cherry]
    return {product.name: product for product in products}


@pytest.fixture
def category_fruits() -> Category:
    apple = Product("apple", "red fruit", 20, 100)
    banana = Product("banana", "sweet yellow fruit", 30, 50)
    cherry = Product("cherry", "purple berry", 100, 250)
    return Category("fruits", "fresh fruits", [apple, banana, cherry])


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0
