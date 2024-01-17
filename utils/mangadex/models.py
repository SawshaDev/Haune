from __future__ import annotations

from typing import Dict, Any, List, Optional

from enum import Enum

import logging


logger = logging.getLogger(__name__)


class RelationshipType(Enum):
    ARTIST = "artist"
    AUTHOR = "author"
    COVER_ART = "cover_art"

class Manga:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)

    def _from_data(self, payload: Dict[str, Any]):


        self.id = payload["id"]
        self.manga_type = payload["type"]

        self.attributes = MangaAttributes(payload["attributes"])

        self.relationships: List[Relationship] = self._make_relationships(payload["relationships"])


    def _make_relationships(self, payload: List[Dict[str, str]]) -> List[Relationship]:
        relationships: List[Relationship] = []
        for relationship in payload:
            new_rl = Relationship(relationship)
            relationships.append(new_rl)

        return relationships
    
class Cover:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)

    def _from_data(self, payload: Dict[str, Any]):
        self.cover_type = payload["type"]
        self.attributes: CoverAttributes = CoverAttributes(payload["attributes"])

class CoverAttributes:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)

    def _from_data(self, payload: Dict[str, Any]):
        self.volume: Optional[str] = payload.get("volume")
        self.file_name = payload["fileName"]
        self.description: Optional[str] = payload.get("description")


class MangaAttributes:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)

    def _from_data(self, payload: Dict[str, Any]):
        self.title: Dict[str, str] = payload["title"]
        self.alt_titles: List[Dict[str, str]] = payload["altTitles"]

        self.description: Dict[str, str] = payload["description"]

        self.tags: List[Tag] = self._make_tags(payload["tags"])

    def _make_tags(self, payload: List[Dict[str, str]]) -> List[Tag]:
        tags = []
        for tag in payload:
            new_tag = Tag(tag)
            tags.append(new_tag)



        return tags

class Relationship:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} Relationship Type: {self.type!r}>"

    def _from_data(self, payload: Dict[str, Any]):
        self.id = payload["id"]

        self.type: str = payload["type"]


class Tag:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)

    def _from_data(self, payload: Dict[str, Any]):

        self.id: str = payload["id"]    
        self.tag_type = payload["type"]

        self.attributes: TagAttributes = TagAttributes(payload["attributes"])
    
class TagAttributes:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)


    def _from_data(self, payload: Dict[str, Any]):
        self.name: Dict[str, str] = payload["name"]

        self.description: Dict[str, str] = payload["description"]

        self.group: str = payload["group"]
