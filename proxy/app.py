from __future__ import annotations

from typing import TYPE_CHECKING

from starlette.applications import Starlette
from starlette.routing import Route

from views import get_image

from aiohttp import ClientSession

routes = [
    Route(
        "/image/{id:str}/{file_name:str}" ,
        get_image,
    ),
]

class App(Starlette):
    if TYPE_CHECKING:
        session: ClientSession


    def __init__(self):
        super().__init__(debug=True, routes=routes)

app = App()


@app.on_event("startup")
async def on_startup():
    app.session = ClientSession()

