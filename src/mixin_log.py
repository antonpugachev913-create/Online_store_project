class MixinLog:
    """Класс для вывода информации о создании продукта"""

    def __init__(self, *args, **kwargs):
        print(repr(self))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        class_name = self.__class__.__name__
        dict_attributes = vars(self).values()

        attributes = map(repr, dict_attributes)
        attributes_str = ", ".join(attributes)
        return f"{class_name}({attributes_str})"
