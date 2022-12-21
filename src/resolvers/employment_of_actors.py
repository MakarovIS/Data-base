from sql_base import base_worker
from sql_base import models


def new_employment_of_actor(employment_of_actor: models.Employment_of_actors) -> int:
    new_id = base_worker.execute("INSERT INTO employment_of_actors(id, worker_id, spectacle_id, role_actor) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (employment_of_actor.id, employment_of_actor.worker_id, employment_of_actor.spectacle_id, employment_of_actor.role_actor))
    return