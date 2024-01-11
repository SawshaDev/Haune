from __future__ import annotations

import discord

from discord import app_commands
from discord.ext import commands

from bot import Haune


class MangaCog(commands.Cog):
    def __init__(self, bot: Haune):
        self.bot = bot

    @app_commands.command( )
    async def manga(self, interaction: discord.Interaction, *, title: str):
        pass

async def setup(bot: Haune):
    await bot.add_cog(MangaCog(bot))