from sql_base import base_worker
from sql_base import models


def new_actor(actor: models.Actor) -> int:
    new_id = base_worker.insert_data("INSERT INTO actor(name_and_surname,date_of_birth,experience)"(actor.name_and_surname, actor.date_of_birth, actor.experience))
    return new_id