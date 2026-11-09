from typing import Any


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    __price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product(name={self.name}, description={self.description}, price={self.__price}, quantity={self.quantity})\n"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    @classmethod
    def new_product(cls, product: dict[str, Any]) -> "Product":
        # name = product['name']
        # description = product['description']
        # price = product['price']
        # quantity = product['quantity']
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @property
    def total_amount(self):
        total_amount = self.price * self.quantity
        return total_amount

    def __add__(self, other):
        # return (self.price * self.quantity) + (other.price * other.quantity)
        return self.total_amount + other.total_amount
