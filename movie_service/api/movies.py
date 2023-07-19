from fastapi import HTTPException, APIRouter
from typing import List

from movie_service.api.models import MovieIn, MovieOut
from movie_service.api import db_manager


movies = APIRouter(
    prefix='/movies',
    tags=['movies']
)


@movies.get('/', response_model=List[MovieOut])
async def index():
    return await db_manager.get_all_movies()


@movies.get('/{id}')
async def get_movie_by_id(id: int):
    return await db_manager.get_movie(id)


@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    movie_id = await db_manager.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.model_dump()
    }

    return response


@movies.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = payload.model_dump()
    return await db_manager.update_movie(id, movie)


@movies.delete('/{id}')
async def delete_movie(id: int):
    movie = await db_manager.delete_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await db_manager.delete_movie(id)
