from fastapi import APIRouter
from sql_base.models import Speechs
import resolvers.speechs

spch_router = APIRouter()


@spch_router.get('/')
def get_speechs():
    return f'Response: {{text: Страница со списком выступлений}}'


@spch_router.post('/')
def new_speech(speech: Speechs,):
    new_id = resolvers.speechs.new_speech(speech)
    return f'{{code: 201, id: {new_id}}}'


@spch_router.get('/{spch_id}')
def get_speech(spch_id: int):
    speech = resolvers.get_speech(spch_id)
    return f'speech: {{date_and_time: дата и время, id: {spch_id}}}'


@spch_router.put('/{spch_id}')
def update_speech(spch_id: int):
    return f'Update speech {spch_id}'


@spch_router.delete('/{spch_id}')
def delete_speech(spch_id: int):
    return f'delete speech {spch_id}'