from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: int,
        quantity: int,
        efficiency: int,
        model: str,
        memory: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # print(repr(self))
