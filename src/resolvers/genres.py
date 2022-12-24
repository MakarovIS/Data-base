from sql_base import base_worker
from sql_base import models


def new_genre(genre: models.Genres) -> int:
    new_id = base_worker.execute("INSERT INTO genres(id, name) "
                                     "VALUES(?,?) "
                                     "RETURNING id",
                                     (genre.id, genre.name))
    return