from fastapi import APIRouter
from sql_base.models import Workers
import resolvers.workers

wrk_router = APIRouter()


@wrk_router.get('/')
def get_workers():
    return f'Response: {{text: Страница со списком персонала}}'


@wrk_router.post('/')
def new_worker(worker: Workers,):
    new_id = resolvers.workers.new_worker(worker)
    return f'{{code: 201, id: {new_id}}}'


@wrk_router.get('/{wrk_id}')
def get_worker(wrk_id: int):
    worker = resolvers.get_worker(wrk_id)
    return f'Worker: {{name: имя, surname: фамилия, id: {wrk_id}}}'


@wrk_router.put('/{wrk_id}')
def update_worker(wrk_id: int):
    return f'Update student {wrk_id}'


@wrk_router.delete('/{wrk_id}')
def delete_worker(wrk_id: int):
    return f'delete worker {wrk_id}'