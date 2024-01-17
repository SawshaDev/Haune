from __future__ import annotations

import discord

import asyncio

from discord import app_commands
from discord.ext import commands

from bot import Haune

from utils.mangadex import get_cover_from_relationship


class MangaCog(commands.Cog):
    def __init__(self, bot: Haune):
        self.bot = bot
        self.mangadex = self.bot.mangadex

    @app_commands.command()
    async def manga(self, interaction: discord.Interaction, title: str):
        manga = await self.mangadex.get_manga(title)

        tags = '\n'.join(tag.attributes.name["en"] for tag in manga.attributes.tags)

        manga_url = f"https://mangadex.org/title/{manga.id}/{manga.attributes.title['en'].replace(' ', '-').lower()}"

        cover_rl = get_cover_from_relationship(manga.relationships)

        self.bot.logger.info("cover: %s", cover_rl)

        cover = await self.mangadex.get_cover(cover_rl.id)

        embed = discord.Embed(description=f"**[{manga.attributes.title['en']}]({manga_url})**", colour=0xAFE2FF)
        embed.add_field(name="Description", value=manga.attributes.description["en"])
        embed.add_field(name="Tags", value=tags, inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot: Haune):
    await bot.add_cog(MangaCog(bot))