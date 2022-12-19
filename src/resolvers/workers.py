from sql_base import base_worker
from sql_base import models


def new_worker(worker: models.Workers) -> int:
    new_id = base_worker.execute("INSERT INTO workers(id, surname, name, date_of_birth) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (worker.id, worker.surname, worker.name, worker.date_of_birth))
    return