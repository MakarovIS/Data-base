from fastapi import APIRouter
from sql_base.models import Ticket
import resolvers.ticket
ticket_router = APIRouter()


@ticket_router.get('/')
def get_tickets():
    return f'Response: {{text: Страница со списком залов}}'


@ticket_router.post('/')
def new_ticket(ticket: Ticket,):
    new_id = resolvers.ticket.new_ticket(ticket)
    return f'{{code: 201, id: {new_id}}}'


@ticket_router.get('/{ticket_id}')
def get_ticket(ticket_id: int):
  return 'Ticket: {category_id: id категории, speech_id: id выступления, status: статус(занят ли)}'


@ticket_router.put('/{ticket_id}')
def update_ticket(ticket_id: int):
    return f'Update ticket {ticket_id}'


@ticket_router.delete('/{ ticket_id}')
def delete_ticket(ticket_id: int):
    return f'delete ticket {ticket_id}'