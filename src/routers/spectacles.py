from fastapi import APIRouter
from sql_base.models import Spectacles
import resolvers.spectacles

spec_router = APIRouter()


@spec_router.get('/')
def get_spectacles():
    return f'Response: {{text: Страница со списком спектаклей}}'


@spec_router.post('/')
def new_spectacle(spectacle: Spectacles,):
    new_id = resolvers.spectacles.new_spectacle(spectacle)
    return f'{{code: 201, id: {new_id}}}'


@spec_router.get('/{spec_id}')
def get_worker(spec_id: int):
    spectacle = resolvers.get_spectacle(spec_id)
    return f'Spectacle: {{name: имя, genre: жанр, id: {spec_id}}}'


@spec_router.put('/{spec_id}')
def update_spectacle(spec_id: int):
    return f'Update spectacle {spec_id}'


@spec_router.delete('/{spec_id}')
def delete_spectacle(spec_id: int):
    return f'delete spectacle {spec_id}'