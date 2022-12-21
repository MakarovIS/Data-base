from sql_base import base_worker
from sql_base import models


def new_spectacle(spectacle: models.Spectacles) -> int:
    new_id = base_worker.execute("INSERT INTO spectacles(id, name, genre, length) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (spectacle.id, spectacle.name, spectacle.genre, spectacle.length))
    return