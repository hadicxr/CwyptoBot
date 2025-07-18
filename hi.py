import discord
from discord.ext import commands

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hello", "hey", "nihao", "namaste", "hola", "bonjour", "greetings", "aloha", "merhaba"])
    async def hi(self, ctx):
        await ctx.send(f"Ni Hao Fine Shyt {ctx.author.mention} :chair:")

async def setup(bot):
    await bot.add_cog(Hi(bot))
    print("Hi Cog Loaded")