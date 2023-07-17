use crate::{Command, Context, Error};

use poise::serenity_prelude::{self as serenity};

#[poise::command(prefix_command)]
pub async fn about(ctx: Context<'_>) -> Result<(), Error> {
    Ok(())
}

pub fn commands() -> [Command; 1] {
    [about()]
}
