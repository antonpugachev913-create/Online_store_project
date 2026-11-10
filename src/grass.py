from src.product import Product


class Grass(Product):
    """Класс для представления травы для газона"""

    country: str
    germination_period: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: int,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
