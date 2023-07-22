use reqwest;

use tokio;

use crate::Error;

use crate::utils::mangadex::structs::{Cover, Manga, Relationship, RelationshipType};

const BASE_URL: &str = "https://api.mangadex.org/";

pub fn get_cover_from_relationship(
    relationships: &Vec<Relationship>,
) -> Result<&Relationship, Error> {
    loop {
        for relationship in relationships {
            println!("{:#?}", relationship.relationship_type);

            if relationship.relationship_type == RelationshipType::cover_art {
                return Ok(relationship);
            } else {
                continue;
            }
        }
    }
}

pub struct MangadexClient {
    pub http: reqwest::Client,
}

impl MangadexClient {
    pub fn new() -> Self {
        Self {
            http: reqwest::Client::new(),
        }
    }

    pub async fn get_manga(&self, title: String) -> Result<Manga, Error> {
        let manga_query = [("title", title), ("order[relevance]", "desc".to_string())];

        let manga_req = self
            .http
            .get(format!("{}/manga", BASE_URL))
            .query(&manga_query)
            .send()
            .await?
            .text()
            .await?;

        let json: serde_json::Value = serde_json::from_str(&manga_req).unwrap();

        let mangas = json["data"].as_array().unwrap();

        let manga = serde_json::from_value::<Manga>(mangas.get(0).unwrap().to_owned()).unwrap();

        Ok(manga)
    }

    pub async fn get_manga_statistics(
        &self,
        manga_id: &String,
    ) -> Result<serde_json::Value, Error> {
        let req = self
            .http
            .get(format!("{BASE_URL}/statistics/manga/{}", manga_id))
            .send()
            .await?
            .json::<serde_json::Value>()
            .await?;

        println!("{req:#?}");
        Ok(req)
    }

    pub async fn get_cover(&self, cover_id: &String) -> Result<Cover, reqwest::Error> {
        let req = &self
            .http
            .get(format!("{}/cover/{}", BASE_URL, cover_id))
            .send()
            .await?
            .text()
            .await?;

        let cover: serde_json::Value = serde_json::from_str(&req).unwrap();
        let cover = serde_json::from_value::<Cover>(cover["data"].to_owned()).unwrap();

        Ok(cover)
    }
}
