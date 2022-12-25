from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.halls import hall_router
from routers.posts import pst_router
from routers.workers import wrk_router
from routers.genres import gnr_router
from routers.spectacles import spec_router
from routers.speechs import spch_router
from routers.employment_of_actors import eoa_router
from routers.ticket_price_categories import tpc_router
from routers.tickets import tick_router

base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()


@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}


app.include_router(hall_router, prefix='/halls')
app.include_router(pst_router, prefix='/posts')
app.include_router(wrk_router, prefix='/workers')
app.include_router(gnr_router, prefix='/genres')
app.include_router(spec_router, prefix='/spectacles')
app.include_router(spch_router, prefix='/speechs')
app.include_router(eoa_router, prefix='/employment_of_actors')
app.include_router(tpc_router, prefix='/ticket_price_categories')
app.include_router(tick_router, prefix='/tickets')



