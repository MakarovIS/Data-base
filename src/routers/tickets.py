from fastapi import APIRouter
from sql_base.models import Tickets
import resolvers.tickets

tick_router = APIRouter()


@tick_router.get('/')
def get_tickets():
    return f'Response: {{text: Страница со списком билетов}}'


@tick_router.post('/')
def new_ticket(ticket: Tickets,):
    new_id = resolvers.tickets.new_ticket(ticket)
    return f'{{code: 201, id: {new_id}}}'


@tick_router.get('/{tick_id}')
def get_ticket(tick_id: int):
    ticket = resolvers.get_ticket(tick_id)
    return f'Ticket: {{ticket_price_category: категория, status: статус, id: {tick_id}}}'


@tick_router.put('/{tick_id}')
def update_ticket(tick_id: int):
    return f'Update ticket {tick_id}'


@tick_router.delete('/{tick_id}')
def delete_ticket(tick_id: int):
    return f'delete ticket {tick_id}'