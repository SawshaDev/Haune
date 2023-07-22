use crate::utils::mangadex::{
    client::get_cover_from_relationship,
    structs::{Cover, Manga, Relationship, Tag},
};
use crate::{Context, Error};

use crate::Command;

use serde_json;

use poise::serenity_prelude::{self as serenity, CacheHttp};

pub fn make_tag_string(tags: &Vec<Tag>) -> Result<String, Error>{
    let mut tag_names: Vec<String> = vec![];

    for tag in tags.iter() {
        tag_names.push(tag.attributes.name["en"].to_owned())
    }

    Ok(tag_names.join(", "))
}


#[poise::command(prefix_command)]
pub async fn test(ctx: Context<'_>) -> Result<(), Error> {
    ctx.say(format!("{:#?}", ctx.author().avatar_url())).await?;

    Ok(())
}

#[poise::command(slash_command)]
pub async fn manga(ctx: Context<'_>, #[rest] title: String) -> Result<(), Error> {
    let data = ctx.data();

    let manga: Manga = data.mangadex.get_manga(title).await?;

    let tags = make_tag_string(&manga.attributes.tags)?;

    let cover_rl = get_cover_from_relationship(&manga.relationships)?;

    let cover = data.mangadex.get_cover(&cover_rl.id).await?;

    let manga_url: String = format!(
        "https://mangadex.org/title/{}/{}",
        &manga.id,
        manga.attributes.title["en"]
            .replace(' ', "-")
            .to_lowercase()
    );

    println!("https://uploads.mangadex.org/covers/{}/{}", &manga.id, &cover.attributes.file_name);

    ctx.send(|cr| {
        cr.embed(|ce| {
            ce.description(format!(
                "**[{}]({})**",
                &manga.attributes.title["en"], manga_url
            ))
            .field("Description", &manga.attributes.description["en"], true)
            .field("Tags", tags, false)
            .color(0xAFE2FF)
            .footer(|cef| cef.text("There are alot of issues with image covers, if the image cover does not appear, its a known issue"))
        })
    })
    .await?;

    Ok(())
}

pub fn commands() -> [Command; 2] {
    [manga(), test()]
}
