from fastapi import APIRouter
from sql_base.models import Actor
import resolvers.actor
actor_router = APIRouter()


@actor_router.get('/')
def get_actors():
    return f'Response: {{text: Страница со списком актеров}}'


@actor_router.post('/')
def new_actor(actor: Actor,):
    new_id = resolvers.actor.new_actor(actor)
    return f'{{code: 201, id: {new_id}}}'


@actor_router.get('/{actor_id}')
def get_actor(actor_id: int):
  return 'Actor: {name_and_surname: название зала, date_of_birth: дата рождения, experience: стаж работы}'


@actor_router.put('/{actor_id}')
def update_actor(actor_id: int):
    return f'Update actor {actor_id}'


@actor_router.delete('/{ actor_id}')
def delete_actor(actor_id: int):
    return f'delete actor {actor_id}'