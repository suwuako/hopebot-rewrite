import json

from datetime import datetime
from discord.ext import commands

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()
        print("loaded commands")

    @commands.command(aliases=["active", "online"])
    async def ping(self, message):
        """
        generic ping comand to check bot's latency && to check if bot is still respondive
        """

        then = datetime.now()

        message = await message.send("<:sip:778194172762128414> Pong!")
        
        latency = datetime.now() - then
        await message.edit(content=f"<:sip:778194172762128414> Pong!\n"
                                   f"[latency: {latency}] ")

        edit_latency = datetime.now() - then
        await message.edit(content=f"<:sip:778194172762128414> Pong!\n"
                                   f"[latency: {latency}] (ms) \n"
                                   f"[edit latency: {edit_latency}] (ms)")

    @commands.command(aliases=["up", "time"])
    async def uptime(self, message):
        """
        generic uptime command to check bot's uptime
        """

        uptime = (datetime.now() - self.start_time)

        output = f"`[{datetime.now().strftime('%H:%M:%S | %d/%m/%Y')}]` I have been online for `{uptime}`, since `{self.start_time} (GMT+8)`"
        await message.reply(output)

    @commands.command(aliases=["count"])
    async def hopes(self, message):
        """
        shows the total amount of times `hope` has been called since 2022-03-22 02:56:48.040721 (GMT+8)
        """

        hopes = json.load(open(r"json/hopes.json"))[0]

        await message.reply(f"Since `2022-03-22 02:56:48.040721 (GMT+8)`, {hopes} hopes have been posted.")




def setup(bot):
    bot.add_cog(commands(bot))
