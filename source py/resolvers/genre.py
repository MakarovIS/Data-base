from sql_base import base_worker
from sql_base import models


def new_genre(genre: models.Genre) -> int:
    new_id = base_worker.insert_data("INSERT INTO genre(name)"(genre.name))
    return new_id