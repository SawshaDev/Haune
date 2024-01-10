import discord

from discord.ext import commands

import os
import aiohttp
import logging

from utils.mangadex import MangaDexApi

class Haune(commands.Bot):
    def __init__(
        self,*,
        session: aiohttp.ClientSession, 
        mangadex: MangaDexApi
    ):

        self.logger = logging.getLogger(__name__)

        self.mangadex = mangadex
        
        self.session = session

        self.loaded_cogs = 0

        os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
        os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 

        super().__init__(command_prefix="erm ", intents=discord.Intents.all())

    async def on_ready(self):
        self.logger.info("Successfully loaded %s %s", self.loaded_cogs, 'cogs' if self.loaded_cogs < 1 else 'cog')

    async def setup_hook(self):
        # Load Cogs

        cogs = ["jishaku"] + [
            f"cogs.{ext if not ext.endswith('.py') else ext[:-3]}"
            for ext in os.listdir("cogs")
            if not ext.startswith("_")
        ] 

        for ext in cogs:
            self.loaded_cogs =+ 1

            await self.load_extension(ext)
        
