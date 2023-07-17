use std::collections::HashMap;

use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize)]
pub struct MangaResponse {
    pub result: String,
    pub response: Vec<String>,
    pub data: Vec<Manga>,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct Manga {
    pub id: String,
    #[serde(rename = "type")]
    pub manga_type: String,

    pub relationships: Vec<Relationship>,

    pub attributes: MangaAttributes,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct MangaAttributes {
    pub title: HashMap<String, String>,
    #[serde(rename = "altTitles")]
    pub alt_titles: Vec<HashMap<String, String>>,
    pub description: HashMap<String, String>,
    pub tags: Vec<Tag>,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct Relationship {
    pub id: String,
    #[serde(rename = "type")]
    pub relationship_type: String,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct Cover {
    #[serde(rename = "type")]
    pub cover_type: String,
    pub attributes: CoverAttributes,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct CoverAttributes {
    pub volume: Option<String>,
    #[serde(rename = "fileName")]
    pub file_name: String,
    pub description: Option<String>,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct Tag {
    pub id: String,
    #[serde(rename = "type")]
    pub tag_type: String,
    pub attributes: TagAttribute,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct TagAttribute {
    pub name: HashMap<String, String>,
    pub description: HashMap<String, String>,
    pub group: String,
}
