from fastapi import APIRouter
from sql_base.models import Hall
import resolvers.hall
hall_router = APIRouter()


@hall_router.get('/')
def get_halls():
    return f'Response: {{text: Страница со списком залов}}'


@hall_router.post('/')
def new_hall(hall: Hall,):
    new_id = resolvers.hall.new_hall(hall)
    return f'{{code: 201, id: {new_id}}}'


@hall_router.get('/{hall_id}')
def get_hall(hall_id: int):
  return 'Hall: {name: название зала}'


@hall_router.put('/{hall_id}')
def update_hall(hall_id: int):
    return f'Update hall {hall_id}'


@hall_router.delete('/{ hall_id}')
def delete_hall(hall_id: int):
    return f'delete hall {hall_id}'