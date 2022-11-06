from classes.base_storage import BaseStorage
from classes.exceptions import NoCapacityError


class Shop(BaseStorage):
    def __init__(self, items, capacity):
        super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            raise NoCapacityError
        super().add(name, amount)
