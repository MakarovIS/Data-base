from fastapi import APIRouter
from sql_base.models import Employment_of_actors
import resolvers.employment_of_actors

eoa_router = APIRouter()


@eoa_router.get('/')
def get_employment_of_actors():
    return f'Response: {{text: Страница со списком контрактов}}'


@eoa_router.post('/')
def new_employment_of_actor(employment_of_actor: Employment_of_actors,):
    new_id = resolvers.employment_of_actors.new_employment_of_actor(employment_of_actor)
    return f'{{code: 201, id: {new_id}}}'


@eoa_router.get('/{eoa_id}')
def get_employment_of_actor(eoa_id: int):
    employment_of_actor = resolvers.get_employment_of_actor(eoa_id)
    return f'employment_of_actor: {{role_actor: роль актера, id: {eoa_id}}}'


@eoa_router.put('/{eoa_id}')
def update_employment_of_actor(eoa_id: int):
    return f'Update employment_of_actor {eoa_id}'


@eoa_router.delete('/{eoa_id}')
def delete_employment_of_actor(eoa_id: int):
    return f'delete employment_of_actor {eoa_id}'