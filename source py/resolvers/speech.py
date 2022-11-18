from sql_base import base_worker
from sql_base import models


def new_speech(speech: models.Speech) -> int:
    new_id = base_worker.insert_data("INSERT INTO speech(spectacle_id,hall_id,date,time)", (speech.spectacle_id, speech.hall_id, speech.date, speech.time))
    return new_id