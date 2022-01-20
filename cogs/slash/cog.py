import nextcord.utils
from nextcord.ext import commands


class SlashSample(commands.Cog, name="sample cog"):
    """Here goes description"""

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("cog loaded")

    @nextcord.slash_command(name="test", description="test slash command", guild_ids=[])
    async def testSlash(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Slash command is working!")


def setup(bot: commands.Bot):
    bot.add_cog(SlashSample(bot))
