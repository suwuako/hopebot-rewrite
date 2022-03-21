import json
import random

from discord.ext import commands
from datetime import datetime

class listening(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        urls = open(r"json/urls.json")
        hope_count = open(r"json/hopes.json")

        self.urls = json.load(urls)
        self.hopes = json.load(hope_count)[0]

        print("loaded listening module...")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        if "!hopes" in content:
            return

        if "hope" in content or "hoping" in content:
            await message.reply(random.choice(self.urls))
            print(f"Hope requested from {message.author}")
            self.hopes += 1

            with open(r"json/hopes.json", 'w') as file:
                json.dump([self.hopes], file)



def setup(bot):
    bot.add_cog(listening(bot))
