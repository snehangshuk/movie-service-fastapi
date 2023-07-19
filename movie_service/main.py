import azure.functions as func
from fastapi import FastAPI

from movie_service.api.movies import movies
from movie_service.api.db import database, engine, metadata

description = """
This is a sample API based on Azure Functions and FastAPI.

This API is used to illustrate how a potential
 API with Azure Functions and FastAPI
 could look like, it is a demo API only.
I hope you like it and help you to build
 awesome projects based on these great frameworks!

## Movies
* Add Movies
* Retrieve movies
* Retrieve a specific movies by ID
* Update existing movies
* Delete moviess by ID
"""
metadata.create_all(engine)

app = FastAPI(
    title="Azure Function Demo FastAPI",
    description="This API is used to illustrate how a potential API"
                " with Azure Functions and FastAPI could look like,"
                " it is a demo API only."
                "I hope you like it and help you to build awesome"
                " projects based on these great frameworks!",
    version="0.1",
    contact={
        "name": "Snehangshu Karmakar",
        "email": "snehnagshu@gmail.com"
    }
)
app.include_router(movies)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """
    Azure function entry point.
    All web requests are handled by FastAPI.
    Args:
        req (func.HttpRequest): Request
        context (func.Context): Azure Function Context

    Returns:
        func.HttpResponse: HTTP Response
    """
    return func.AsgiMiddleware(app).handle(req, context)
