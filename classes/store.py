from classes.base_storage import BaseStorage


class Store(BaseStorage):
    # можно реализовать конструктор, чтобы задать значение capacity: int = 100, но это не обязательно
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)