from fastapi import APIRouter
from sql_base.models import Speech
import resolvers.speech
speech_router = APIRouter()


@speech_router.get('/')
def get_speeches():
    return f'Response: {{text: Страница со списком выступлений}}'


@speech_router.post('/')
def new_speech(speech: Speech,):
    new_id = resolvers.speech.new_speech(speech)
    return f'{{code: 201, id: {new_id}}}'


@speech_router.get('/{speech_id}')
def get_speech(speech_id: int):
  return 'Speech: {spectacle_id: id спектакля, hall_id: id зала, date: дата, time: время}'


@speech_router.put('/{speech_id}')
def update_speech(speech_id: int):
    return f'Update speech {speech_id}'


@speech_router.delete('/{ speech_id}')
def delete_speech(speech_id: int):
    return f'delete speech {speech_id}'