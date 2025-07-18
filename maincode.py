import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle
import logging

discord.utils.setup_logging()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot_statuses = cycle(["Made by cwypticles", "Say .hi"])

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

@bot.event
async def on_ready():
    print("Bot Online!")
    change_status.start()
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as e:
        print(f"Failed to sync commands:", e)

with open("token.txt") as file:
    token = file.read()

async def Load():
    for filename in os.listdir("./CwyptoBot/Cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Cogs.{filename[:-3]}")

async def main():
    async with bot:
        await Load()
        await bot.start(token)

asyncio.run(main())