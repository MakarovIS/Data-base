from sql_base import base_worker
from sql_base import models


def new_post(post: models.Posts) -> int:
    new_id = base_worker.execute("INSERT INTO posts(id, name) "
                                     "VALUES(?,?) "
                                     "RETURNING id",
                                     (post.id, post.name))
    return