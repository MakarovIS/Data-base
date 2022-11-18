from fastapi import APIRouter
from sql_base.models import Spectacle
import resolvers.spectacle
spectacle_router = APIRouter()


@spectacle_router.get('/')
def get_spectacles():
    return f'Response: {{text: Страница со списком спектакля}}'


@spectacle_router.post('/')
def new_spectacle(spectacle: Spectacle,):
    new_id = resolvers.spectacle.new_spectacle(spectacle)
    return f'{{code: 201, id: {new_id}}}'


@spectacle_router.get('/{spectacle_id}')
def get_spectacle(spectacle_id: int):
  return 'Spectacle: {name: название спектакля, genre_id: id жанра, length: длительность}'


@spectacle_router.put('/{spectacle_id}')
def update_spectacle(spectacle_id: int):
    return f'Update spectacle {spectacle_id}'


@spectacle_router.delete('/{ spectacle_id}')
def delete_spectacle(spectacle_id: int):
    return f'delete spectacle {spectacle_id}'