import nextcord
import os
import nextcord.ext
from nextcord.ext import commands
import logging
import _helper as hp
from os import getenv

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"), intents=intents)
cogs = []


"""
Events
"""
@bot.event
async def on_ready():
    print(f"----------\nLogged in as {bot.user}({bot.user.id}).\n----------")


for file in os.listdir("./cogs"):
    """
    Load all cogs in cogs directory.
    """

    if file.endswith(".py"):
        name = file[:-3]
        cog = f"cogs.{name}"
        cogs.append(cog)
        bot.load_extension(cog)
        print(f"Loaded cog {name}.")


#keep_alive.keep_alive()
bot.run(getenv("TOKEN"))
