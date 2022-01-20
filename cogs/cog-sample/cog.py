import nextcord.utils
from nextcord.ext import commands


class SampleCog(commands.Cog, name="sample cog"):
    """Here goes description"""

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog loaded")


def setup(bot: commands.Bot):
    bot.add_cog(SampleCog(bot))
