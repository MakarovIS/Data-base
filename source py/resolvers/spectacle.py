from sql_base import base_worker
from sql_base import models


def new_spectacle(spectacle: models.Spectacle) -> int:
    new_id = base_worker.insert_data("INSERT INTO spectacle(name,genre_id,length)"(spectacle.name,spectacle.genre_id,spectacle.length))
    return new_id