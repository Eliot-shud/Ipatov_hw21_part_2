from typing import Dict

from classes.abs_storage import AbstractStorage
from classes.courier import Courier
from classes.exceptions import BaseError
from classes.request import Request
from classes.shop import Shop
from classes.store import Store

store = Store(
    items={'мылов': 10,
           'шилов': 10,
           'рыбов': 20,
           },
    capacity=100,
)
shop = Shop(
    items={'мылов': 5,
           'шилов': 5,
           'рыбов': 5,
           'стулов_с_предметом_1': 1,
           'стулов_с_предметом_2': 1
           },
    capacity=20,
)
storages: Dict[str, AbstractStorage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    print('Добрый день \n')
    while True:
        for name, storage in storages.items():
            print(f'В {name} хранится: \n{storage.get_items()}')

        request = input('Введите запрос в формате "Доставить 3 рыбов из склад в магазин"\n'
                        'Введите "стоп" чтобы закончить\n')

        if request == 'стоп':
            break

        try:
            request = Request(request=request, storage=storages)
        except BaseError as e:
            print(e.message)

        courier = Courier(request=request, storages=storages)

        try:
            courier.transport()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
