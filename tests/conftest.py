import pytest

from src.category import Category
from src.grass import Grass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def init_smartphone_dict() -> dict[str, Smartphone]:
    iphone = Smartphone(
        "Blue iphone", "Powerful phone", 100_000, 250, 150, "Iphone 18", "32 Гб", "Blue"
    )
    poco = Smartphone(
        "Poco X6 black",
        "Big smartphone",
        60_000,
        1000,
        100,
        "Poco X6",
        "16 Гб",
        "Black",
    )
    return {"poco": poco, "iphone": iphone}


@pytest.fixture
def init_grass_dict() -> dict[str, Grass]:
    emerald_grass = Grass(
        "emerald_grass", "green grass", 1500, 150, "Germany", 14, "Dark green"
    )
    shadow_grass = Grass(
        "Луговой бархат",
        "Травосмесь для затененных участков и парковых зон",
        1800,
        30,
        "Russia",
        21,
        "Light green",
    )
    grasses = {"emerald_grass": emerald_grass, "shadow_grass": shadow_grass}
    return grasses
