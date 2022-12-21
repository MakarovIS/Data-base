from fastapi import APIRouter
from sql_base.models import Ticket_price_categories
import resolvers.ticket_price_categories

tpc_router = APIRouter()


@tpc_router.get('/')
def get_ticket_price_categories():
    return f'Response: {{text: Страница со списком категорий цен на билеты}}'


@tpc_router.post('/')
def new_ticket_price_category(ticket_price_category: Ticket_price_categories,):
    new_id = resolvers.get_ticket_price_categories.new_ticket_price_category(ticket_price_category)
    return f'{{code: 201, id: {new_id}}}'


@tpc_router.get('/{tpc_id}')
def get_ticket_price_category(tpc_id: int):
    ticket_price_category = resolvers.get_ticket_price_category(tpc_id)
    return f'ticket_price_category: {{price: цена, id: {tpc_id}}}'


@tpc_router.put('/{tpc_id}')
def update_ticket_price_category(tpc_id: int):
    return f'Update ticket_price_category {tpc_id}'


@tpc_router.delete('/{tpc_id}')
def delete_ticket_price_category(tpc_id: int):
    return f'delete ticket_price_category {tpc_id}'