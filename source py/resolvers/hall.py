from sql_base import base_worker
from sql_base import models


def new_hall(hall: models.Hall) -> int:
    new_id = base_worker.insert_data("INSERT INTO hall(name)", (hall.name))
    return new_id