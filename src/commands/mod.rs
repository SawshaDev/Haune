mod anime;
mod misc;

pub fn get_commands() -> Vec<crate::Command> {
    anime::commands()
        .into_iter()
        .chain(misc::commands())
        .collect()
}
