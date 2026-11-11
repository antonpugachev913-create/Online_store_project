import pytest

from src.base_product import BaseProduct
from src.grass import Grass
from src.product import Product
from src.smartphone import Smartphone


def test_announce_obj_raise_error() -> None:
    with pytest.raises(TypeError):
        _ = BaseProduct()


def test_create_right_hierarchy() -> None:
    assert issubclass(Product, BaseProduct)
    assert issubclass(Grass, BaseProduct)
    assert issubclass(Smartphone, BaseProduct)
