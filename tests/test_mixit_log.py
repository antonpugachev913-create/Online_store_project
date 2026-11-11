import pytest
from src.product import Product


def test_get_correct_output(capsys) -> None:
    _ = Product("apple", "red fruit", 20, 100)

    output = capsys.readouterr()
    captured = output.out.strip()
    assert captured == "Product('apple', 'red fruit', 20, 100)"

    # poco = Smartphone(
    #     "Poco X6 black",
    #     "Big smartphone",
    #     60_000,
    #     1000,
    #     100,
    #     "Poco X6",
    #     "16 Гб",
    #     "Black",
    # )
    #
    # output = capsys.readouterr()
    # captured = output.out.strip()
    # assert (
    #     captured
    #     == "Smartphone('Poco X6 black', 'Big smartphone', 60000, 1000, 100, 'Poco X6', '16 Гб', 'Black')"
    # )

    # shadow_grass = Grass(
    #     "Луговой бархат",
    #     "Травосмесь для затененных участков и парковых зон",
    #     1800,
    #     30,
    #     "Russia",
    #     21,
    #     "Light green",
    # )
    # #
    # # output = capsys.readouterr()
    # # captured = output.out.strip()
