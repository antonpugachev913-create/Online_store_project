class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        return self.__products

    @property
    def get_list_products(self) -> list[Product]:
        list_products = self.__products
        string_products = []
        for product in list_products:
            name = product.name
            price = product.price
            rest = product.quantity
            ans = f'{name}, {price}. Остаток: {rest} шт.'
            string_products.append(ans)
        return 0
