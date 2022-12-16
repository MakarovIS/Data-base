from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.workers import wrk_router


base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()


@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}


app.include_router(wrk_router, prefix='/workers')

