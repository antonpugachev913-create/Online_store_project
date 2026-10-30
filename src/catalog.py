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
        return f'Product(name={self.name}, description={self.description}, price={self.__price}, quantity={self.quantity})\n'

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


class Category:
    """Класс для представления категории"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    def __repr__(self) -> str:
        return f'Category(name={self.name}, description={self.description}, products={self.__products})\n'

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        list_products = self.__products
        new_list_products = []
        for product in list_products:
            name = product.name
            price = product.price
            rest = product.quantity
            product_string = f"{name}, {price} руб. Остаток: {rest} шт.\n"
            new_list_products.append(product_string)
        string_products = "".join(new_list_products)
        return string_products

    @property
    def get_list_products(self) -> list[str]:
        return self.__products
