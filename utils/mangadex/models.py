from __future__ import annotations

from typing import Dict, Any, List 

from enum import Enum

import logging



class Manga:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

        self._from_data(self._payload)

    def _from_data(self, payload: Dict[str, Any]):


        self.id = payload["id"]
        self.manga_type = payload["type"]

        self.attributes = MangaAttributes(payload["attributes"])


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
