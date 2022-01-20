import nextcord.utils
from nextcord.ext import commands


class CommandsSample(commands.Cog, name="Sample commands"):
    """Here goes description"""

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog loaded")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Simple reply"""
        await ctx.reply("pong!")

    @commands.command()
    async def embedPing(self, ctx: commands.Context):
        """Simple embed reply"""
        embed = nextcord.Embed(description="Pong!")
        await ctx.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(CommandsSample(bot))
