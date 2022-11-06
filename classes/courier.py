from typing import Dict

from classes.abs_storage import AbstractStorage
from classes.exceptions import BaseError


class Courier:
    def __init__(self, request, storages: Dict[str, AbstractStorage]):
        self.__request = request
        self.departure = storages[self.__request.departure]
        self.destination = storages[self.__request.destination]

    def transport(self):
        self.departure.remove(name=self.__request.goods, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount}{self.__request.goods} из {self.__request.departure}')
        try:
            self.destination.add(name=self.__request.goods, amount=self.__request.amount)
            print(f'Курьер доставил {self.__request.amount}{self.__request.goods} в {self.__request.destination}')
        except BaseError as e:
            self.departure.add(name=self.__request.goods, amount=self.__request.amount)
            print(e.message)
            print(f'Курьер вернул {self.__request.amount} {self.__request.goods} в {self.__request.departure}')
