import json
import random

from discord.ext import commands
from datetime import datetime

class listening(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        urls = open(r"json/urls.json")

        self.urls = json.load(urls)

    
    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content.lower()
        if "hope" in content or "hoping" in content:
            await message.channel.send(random.choice(self.urls))


def setup(bot):
    bot.add_cog(listening(bot))
