import pytest
from src.smartphone import Smartphone


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
