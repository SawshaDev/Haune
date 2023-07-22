use crate::{Command, Context, Error};

use poise::serenity_prelude::{self as serenity};

#[poise::command(prefix_command)]
pub async fn about(ctx: Context<'_>) -> Result<(), Error> {
    ctx.send(|cr| {
        cr.embed(|ce| {
            ce.description("hi")
        })
    }).await?;
    Ok(())
}

pub fn commands() -> [Command; 1] {
    [about()]
}
