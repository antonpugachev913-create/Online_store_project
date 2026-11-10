from src.product import Product
from src.smartphone import Smartphone
from src.grass import Grass

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
        return f"Category(name={self.name}, description={self.description}, products={self.__products})\n"

    def __str__(self):
        quantity_products = sum(cnt.quantity for cnt in self.get_list_products)
        return f"{self.name}, количество продуктов: {quantity_products} шт.\n"

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print('Продукта нет в списке допустимых категорий!')

    @property
    def products(self) -> str:
        list_products = self.__products
        new_list_products = []
        for product in list_products:
            product_string = str(product)
            new_list_products.append(product_string)
        string_products = "".join(new_list_products)
        return string_products

    @property
    def get_list_products(self) -> list[str]:
        return self.__products

    def __len__(self):
        return len(self.__products)
