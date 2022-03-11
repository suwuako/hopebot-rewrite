import discord 
import json
import asyncio

from discord.ext import commands


class yuuka:
    def __init__(self):
        secret = open(r"json/secret.json")
        secret = json.load(secret)

        self.token = secret["token"]
        print("yay your bot is live...")
    
    def load_cogs(self):
        bot.load_extension("src.commands")
        bot.load_extension("src.listening")

    def run(self):
        self.load_cogs()
        bot.run(self.token)


if __name__ == "__main__":
    bot = commands.Bot(command_prefix='!')

    yuuka = yuuka()
    yuuka.run()


