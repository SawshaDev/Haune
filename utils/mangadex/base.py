from __future__ import annotations

from aiohttp import ClientSession
from typing import Optional, Dict, Any

from .models import Manga

import logging


logger = logging.getLogger(__name__)

BASE_API_URL = "https://api.mangadex.org/"


class MangaDexApi:
    def __init__(self, *, session: ClientSession):
        self.session = session

    async def get_manga(self, title: str) -> Manga:
        params = {"title": title, "order[relevance]": "desc"}

        resp = await self.session.get(f"{BASE_API_URL}/manga", params=params)

        json = await resp.json()

        manga = Manga(json["data"][0])

        return manga


