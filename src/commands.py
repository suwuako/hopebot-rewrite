from datetime import datetime
from discord.ext import commands

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()
        print("loaded commands")

    @commands.command()
    async def ping(self, message):
        then = datetime.now()

        message = await message.send("<:sip:778194172762128414> Pong!")
        
        latency = datetime.now() - then
        await message.edit(content=f"<:sip:778194172762128414> Pong!\n"
                                   f"[latency: {latency}] ")

        edit_latency = datetime.now() - then
        await message.edit(content=f"<:sip:778194172762128414> Pong!\n"
                                   f"[latency: {latency}] (ms) \n"
                                   f"[edit latency: {edit_latency}] (ms)")

def setup(bot):
    bot.add_cog(commands(bot))
