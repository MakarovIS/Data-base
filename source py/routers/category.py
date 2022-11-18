from fastapi import APIRouter
from sql_base.models import Category
import resolvers.category
category_router = APIRouter()


@category_router.get('/')
def get_categories():
    return f'Response: {{text: Страница со списком залов}}'


@category_router.post('/')
def new_category(category: Category,):
    new_id = resolvers.category.new_category(category)
    return f'{{code: 201, id: {new_id}}}'


@category_router.get('/{category_id}')
def get_category(category_id: int):
  return 'Category: {hall_id: id зала, row: ряд, price: цена}'


@category_router.put('/{category_id}')
def update_category(category_id: int):
    return f'Update category {category_id}'


@category_router.delete('/{ category_id}')
def delete_category(category_id: int):
    return f'delete category {category_id}'