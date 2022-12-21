from sql_base import base_worker
from sql_base import models


def new_ticket(ticket: models.Tickets) -> int:
    new_id = base_worker.execute("INSERT INTO tickets(id, ticket_price_category_id, speech_id, status) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (ticket.id, ticket.ticket_price_category_id, ticket.speech_id, ticket.status))
    return