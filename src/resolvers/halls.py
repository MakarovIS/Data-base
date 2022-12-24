from sql_base import base_worker
from sql_base import models


def new_hall(hall: models.Halls) -> int:
    new_id = base_worker.execute("INSERT INTO halls(id, name) "
                                     "VALUES(?,?) "
                                     "RETURNING id",
                                     (hall.id, hall.name))
    return