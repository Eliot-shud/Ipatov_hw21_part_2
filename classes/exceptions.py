class BaseError(Exception):
    message = 'Что-то пошло не так'


class NoCapacityError(BaseError):
    message = 'Не хватает места'


class NoItemsError(BaseError):
    message = 'Не хватает такого товара'


class ExcessProductsError(BaseError):
    message = 'Слишком большое количество товара'


class BadRequestError(BaseError):
    message = 'Запрос составлен неверно'


class WrongStorageError(BaseError):
    message = 'Неправильное место доставки'