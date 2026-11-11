from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для общего представления продуктов"""

    @abstractmethod
    def __init__(self):
        super().__init__()
        pass
