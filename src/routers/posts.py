from fastapi import APIRouter
from sql_base.models import Posts
import resolvers.posts

pst_router = APIRouter()


@pst_router.get('/')
def get_posts():
    return f'Response: {{text: Страница со списком постов}}'


@pst_router.post('/')
def new_post(post: Posts,):
    new_id = resolvers.posts.new_post(post)
    return f'{{code: 201, id: {new_id}}}'


@pst_router.get('/{pst_id}')
def get_post(pst_id: int):
    post = resolvers.get_post(pst_id)
    return f'Post: {{name: название, id: {pst_id}}}'


@pst_router.put('/{pst_id}')
def update_post(pst_id: int):
    return f'Update post {pst_id}'


@pst_router.delete('/{pst_id}')
def delete_post(pst_id: int):
    return f'delete post {pst_id}'