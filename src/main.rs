mod commands;

mod utils;

use tokio;

use poise::serenity_prelude as serenity;

use crate::utils::mangadex::client::MangadexClient;


pub struct Data {
    pub http: reqwest::Client,
    pub mangadex: MangadexClient,
}

pub type Error = Box<dyn std::error::Error + Send + Sync>;
pub type Context<'a> = poise::Context<'a, Data, Error>;
pub type Command = poise::Command<Data, Error>;

#[tokio::main]
async fn main() {
    env_logger::init();

    let framework = poise::Framework::builder()
        .options(poise::FrameworkOptions {
            prefix_options: poise::PrefixFrameworkOptions {
                prefix: Some("erm ".into()),
                case_insensitive_commands: true,
                ..Default::default()
            },
            commands: commands::get_commands(),
            ..Default::default()
        })
        .token(std::env::var("DISCORD_TOKEN").expect("missing DISCORD_TOKEN"))
        .intents(serenity::GatewayIntents::all())
        .setup(|ctx, _ready, framework| {
            Box::pin(async move {
                poise::builtins::register_globally(ctx, &framework.options().commands).await?;
                let http = reqwest::Client::new();

                let mangadex = MangadexClient::new();

                let data = Data { http, mangadex };

                Ok(data)
            })
        });

    framework.run().await.unwrap();
}
