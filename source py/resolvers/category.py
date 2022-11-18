from sql_base import base_worker
from sql_base import models


def new_category(category: models.Category) -> int:
    new_id = base_worker.insert_data("INSERT INTO category(hall_id,row,price)", (category.hall_id, category.row, category.price))
    return new_id