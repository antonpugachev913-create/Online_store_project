import pytest
from src.category import Category
from src.read_data import read_data_file


@pytest.fixture
def init_categories() -> list[Category]:
    data = read_data_file()
    return data


def test_read_data_file_success(init_categories) -> None:
    smartphones = init_categories[0]
    televisions = init_categories[1]

    assert smartphones.name == "Смартфоны"
    assert (
        smartphones.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )

    assert televisions.name == "Телевизоры"
    assert (
        televisions.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
