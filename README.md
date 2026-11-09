# Online_store_project
## Описание:
Online_store_project - это проект-ядро для онлайн магазина с применением концепций 
ООП.

## Установка
#### Склонируйте репозиторий:
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
```catalog.py``` - содержит классы для каталога магазина

#### Примеры использования catalog.py (каталога магазина)
```python
from src.catalog import Product, Category
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

