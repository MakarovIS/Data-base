from sql_base import base_worker
from sql_base import models


def new_employment_of_actors(employment_of_actors: models.Employment_of_actors) -> int:
    new_id = base_worker.insert_data("INSERT INTO employment_of_actors(actor_id,spectacle_id)"(employment_of_actors.actor_id, employment_of_actors.spectacle_id, employment_of_actors.role))
    return new_id