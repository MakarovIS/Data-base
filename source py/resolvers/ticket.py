from sql_base import base_worker
from sql_base import models


def new_ticket(ticket: models.Ticket) -> int:
    new_id = base_worker.insert_data("INSERT INTO ticket(category_id, speech_id ,status)", (ticket.category_id, ticket.speech_id, ticket.status))
    return new_id