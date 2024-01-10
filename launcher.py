import aiohttp
import discord
import asyncio

from bot import Haune

from utils.mangadex import MangaDexApi

import os
import dotenv

dotenv.load_dotenv()

discord.utils.setup_logging()

async def main():
    async with aiohttp.ClientSession() as session, Haune(session=session, mangadex=MangaDexApi(session=session)) as bot:
        await bot.start(os.environ["TOKEN"])

asyncio.run(main())