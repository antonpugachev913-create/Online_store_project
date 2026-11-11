import pytest


def test_init_success_grass(init_grass_dict) -> None:
    emerald_grass = init_grass_dict["emerald_grass"]

    assert emerald_grass.name == "emerald_grass"
    assert emerald_grass.description == "green grass"
    assert emerald_grass.price == 1500
    assert emerald_grass.quantity == 150
    assert emerald_grass.country == "Germany"
    assert emerald_grass.germination_period == 14
    assert emerald_grass.color == "Dark green"
