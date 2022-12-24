from fastapi import APIRouter
from sql_base.models import Genres
import resolvers.genres

gnr_router = APIRouter()


@gnr_router.get('/')
def get_genres():
    return f'Response: {{text: Страница со списком жанров}}'


@gnr_router.post('/')
def new_genre(genre: Genres,):
    new_id = resolvers.genres.new_genre(genre)
    return f'{{code: 201, id: {new_id}}}'


@gnr_router.get('/{gnr_id}')
def get_genre(gnr_id: int):
    ticket = resolvers.get_genre(gnr_id)
    return f'Genre: {{name: название, id: {gnr_id}}}'


@gnr_router.put('/{gnr_id}')
def update_genre(gnr_id: int):
    return f'Update genre {gnr_id}'


@gnr_router.delete('/{gnr_id}')
def delete_genre(gnr_id: int):
    return f'delete genre {gnr_id}'