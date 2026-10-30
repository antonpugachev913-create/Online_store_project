import pathlib
import json
from src.catalog import Product, Category

def get_roof():
    loger_script = pathlib.Path(__file__).resolve()
    project_root = next(p for p in loger_script.parents if p.name == "Online_store_project")
    return project_root

project_roof = get_roof()
file_path = project_roof / 'data' / 'products.json'

def read_data_file(path=file_path):
    with open(path, 'r', encoding='utf-8') as file:
        catalog = json.load(file)
    categories = []

    for category in catalog:
        products = category['products']
        list_products = []
        for product in products:
            inited_product =Product.new_product(product)
            list_products.append(inited_product)
        name = category['name']
        description = category['description']
        inited_category = Category(name, description, list_products)
        categories.append(inited_category)
    return categories



# pprint(read_data_file(), indent=4)
