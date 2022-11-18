from fastapi import APIRouter
from sql_base.models import Genre
import resolvers.genre
genre_router = APIRouter()


@genre_router.get('/')
def get_genres():
    return f'Response: {{text: Страница со списком жанров}}'


@genre_router.post('/')
def new_genre(genre: Genre,):
    new_id = resolvers.genre.new_genre(genre)
    return f'{{code: 201, id: {new_id}}}'


@genre_router.get('/{genre_id}')
def get_genre(genre_id: int):
  return 'Genre: {name: название жанра}'


@genre_router.put('/{genre_id}')
def update_genre(genre_id: int):
    return f'Update genre {genre_id}'


@genre_router.delete('/{ genre_id}')
def delete_genre(genre_id: int):
    return f'delete genre {genre_id}'