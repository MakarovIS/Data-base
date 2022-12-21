from sql_base import base_worker
from sql_base import models


def new_ticket_price_category(ticket_price_category: models.Ticket_price_categories) -> int:
    new_id = base_worker.execute("INSERT INTO ticket_price_categories(id, hall, row, price) "
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (ticket_price_category.id, ticket_price_category.hall, ticket_price_category.row, ticket_price_category.price))
    return