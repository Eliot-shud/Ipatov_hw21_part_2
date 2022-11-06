from typing import Dict, List

from classes.abs_storage import AbstractStorage
from classes.exceptions import BadRequestError, WrongStorageError


class Request:
    def __init__(self, request: str, storage: Dict[str, AbstractStorage]):

        split_request: List[str] = request.strip().lower().split(' ')
        if len(split_request) != 7:
            raise BadRequestError

        self.amount = int(split_request[1])
        self.goods = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]

        if self.departure not in storage or self.destination not in storage:
            raise WrongStorageError
