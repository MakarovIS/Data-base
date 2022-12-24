from sql_base import base_worker
from sql_base import models


def new_speech(speech: models.Speechs) -> int:
    new_id = base_worker.execute("INSERT INTO speechs(id, spectacle_id, hall_id, date_and_time) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (speech.id, speech.spectacle_id, speech.hall_id, speech.date_and_time))
    return