import logging
from typing import TYPE_CHECKING
from starlette.requests import Request
from starlette.responses import (
    JSONResponse,
    Response,
    HTMLResponse
)

from aiohttp import ClientResponse


from io import BytesIO

if TYPE_CHECKING:
    from starlette.datastructures import UploadFile, MultiDict



content_type = {
    "png":"image/png",
    "jpeg":"image/jpeg",
    "jpg":"image/jpg",
}

async def get_image(request: Request) -> Response:
    file_id: str = request.path_params["id"]
    file_name: str = request.path_params["file_name"]


    print(f"{file_id}\n{file_name}")

    resp: ClientResponse = await request.app.session.get(f"https://uploads.mangadex.org/covers/{file_id}/{file_name}")

    resp_bytes = await resp.read()

    mime = content_type.get(resp.content_type)

    return Response(
        resp_bytes,
        status_code=200,
        media_type=mime
    )

    