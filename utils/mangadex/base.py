from __future__ import annotations

from aiohttp import ClientSession
from typing import Optional, Dict, Any, List

from .models import Manga, Relationship, RelationshipType, Cover

import logging


logger = logging.getLogger(__name__)

BASE_API_URL = "https://api.mangadex.org/"


def get_cover_from_relationship(relationships: List[Relationship]) -> Relationship:
    for relationship in relationships:
        logger.info("Relationship: %s", relationship.type)

        if relationship.type != "cover_art":
            continue

        logger.info(relationship)

        return relationship


class MangaDexApi:
    def __init__(self, *, session: ClientSession):
        self.session = session

    async def get_manga(self, title: str) -> Manga:
        params = {"title": title, "order[relevance]": "desc"}

        resp = await self.session.get(f"{BASE_API_URL}/manga", params=params)

        json = await resp.json()

        manga = Manga(json["data"][0])

        return manga

    async def get_cover(self, cover_id: str) -> Cover:
        resp = await self.session.get(f"{BASE_API_URL}/cover/{cover_id}")

        json = await resp.json()

        cover = Cover(json["data"])

        return cover