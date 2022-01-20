import os
import nextcord
from nextcord.ext import commands

import config


def main():
    bot = commands.Bot(command_prefix=config.PREFIX)

    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            bot.load_extension(f"cogs.{folder}.cog")

    bot.run(config.TOKEN)


if __name__ == "__main__":
    main()
