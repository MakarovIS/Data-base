from fastapi import APIRouter
from sql_base.models import Employment_of_actors
import resolvers.employment_of_actors
employment_of_actors_router = APIRouter()


@employment_of_actors_router.get('/')
def get_employment_of_actors():
    return f'Response: {{text: Страница со списком контрактов актеров}}'


@employment_of_actors_router.post('/')
def new_employment_of_actors(employment_of_actors: Employment_of_actors,):
    new_id = resolvers.employment_of_actors.new_employment_of_actors(employment_of_actors)
    return f'{{code: 201, id: {new_id}}}'


@employment_of_actors_router.get('/{employment_of_actors_id}')
def get_employment_of_actors(employment_of_actorsactor_id: int):
  return 'Employment_of_actors: {employment_of_actorsun_id: id актера, spectacle_id: id спектакля, role: роль}'


@employment_of_actors_router.put('/{employment_of_actors_id}')
def update_employment_of_actors(employment_of_actors_id: int):
    return f'Update employment_of_actors {employment_of_actors_id}'


@employment_of_actors_router.delete('/{ employment_of_actors_id}')
def delete_employment_of_actors(employment_of_actors_id: int):
    return f'delete employment_of_actors {employment_of_actors_id}'