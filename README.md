# Online_store_project
## Описание:
Online_store_project - это проект-ядро для онлайн магазина с применением концепций 
ООП.

## Установка
#### Клонируйте репозиторий:
```bash
git clone https://github.com/antonpugachev913-create/Online_store_project
```

#### Установите poetry:
```bash
pip install poetry
```

#### Установите все зависимости:
```bash
poetry install
```

## Тестирование
#### Запуск всех тестов
```bash
poetry run pytest
```

#### Запуск тестов с отчетом о покрытии кода
```bash
poetry run pytest --cov=src --cov-report=html
```

#### Запуск форматеров
```bash
poetry run black .
poetry run isort .
```

#### Запуск линтеров
```bash
poetry run flake8 .
poetry run mypy .
```


## Документация
#### В пакете src содержатся модули:
```category.py``` - содержит класс для категорий магазина

```product.py``` - содержит класс для представления продуктов магазина

```grass.py``` - содержит дочерний класс Product для представления товаров газона

```smartphone.py``` - содержит дочерний класс Product для представления телефонов

```read_data.py``` - содержит функцию, считывающую данные о категории из json file и создающая класс Category



#### Примеры использования category.py and product.py (каталога магазина)
```python
from src.product import Product
from src.category import Category

#Инициализируем классы
product_1 = Product("apple", "sweet fruit", 500, 10) # создаем объект класса Product
product_2 = Product("banana", "sweet yellow fruit", 30, 50)
category_1 = Category("fruits", "fresh fruits", ["apple", "banana", "cherry"]) # создаем объект класса Category


#Получение данных класса
product_1.price = 100 # устанавливаем новую цену для продукта
products = category_1.products #получаем список товаров в виде единой строки

total_amount = product_1.total_amount + product_2.total_amount # вычисляем общую сумму произведений цены на количество у двух объектов.

print(repr(product_1)) # получаем отладочный вывод для инициализации объекта класса Product
```


#### Примеры использования grass.py and smartphone.py:
```python
from src.grass import Grass
from src.smartphone import Smartphone

#Инициализация экземпляров классов
iphone = Smartphone(
    "Blue iphone",
    "Powerful phone",
    100_000,
    250,
    150,
    "Iphone 18",
    "32 Гб",
    "Blue")
poco = Smartphone(
        "Poco X6 black",
        "Big smartphone",
        60_000,
        1000,
        100,
        "Poco X6",
        "16 Гб",
        "Black",
    )

shadow_grass = Grass(
        "Луговой бархат",
        "Травосмесь для затененных участков и парковых зон",
        1800,
        30,
        "Russia",
        21,
        "Light green",
    )

emerald_grass = Grass(
        "emerald_grass", "green grass", 1500, 150, "Germany", 14, "Dark green"
    )

#Вычисляем сумму товаров одной категории (Можем складывать только те товары, которые относят к 1 категории)
total_grasses = emerald_grass + shadow_grass
total_smartphones = iphone + poco
```
